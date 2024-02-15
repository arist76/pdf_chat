from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from pdf_chat import settings
from pdf_chat.settings import MEDIA_ROOT
from chat.chain import RESPONSE_TEMPLATE, TogetherLLM
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os


def pdfUploadPath(instance, filename : str):
    return f"{instance.grade}/{instance.subject}/{filename.replace(' ', '')}"
class PDF(models.Model):
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)
    pdf = models.FileField(upload_to=pdfUploadPath)

    class Meta:
        unique_together = ["subject", "grade"]

    __embedded = False

    # TODO : add pdf deletion side effect on PDF deletion

    def embed(self):
        print(self.__embedded)
        if not self.__embedded:
            # load pdf file
            print("splitting pdf")
            docs = PyPDFLoader(
                os.path.join(
                    MEDIA_ROOT, 
                    self.pdf.name.replace(' ', '')
                )
            ).load_and_split()
            print("pdf splitted")


            vectordb = Chroma.from_documents(
                collection_name = f"{self.subject}_{self.grade}",
                documents = docs, 
                embedding = settings.CHAT_EMBEDDING_MODEL,
                persist_directory=settings.CHROMA_DB_DIR
            )
            print("pdf embedding done")
            self.__embedded = True
    
    def query(self, q, user):
        chat = [
            HumanMessage(content=message.text)
                if message.type == "Human"
                else AIMessage(content="Large language model") 
                    for message in ChatMessage.objects.filter(
                        chat__user=user,
                        chat__subject=self.subject,
                        chat__grade=self.grade
                    )
        ]



        contextualize_q_system_prompt = """Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is."""
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        contextualize_q_chain = contextualize_q_prompt | TogetherLLM() | StrOutputParser()

        repharsed_q = contextualize_q_chain.invoke(
            {
                "chat_history": chat,
                "question": q,
            }
        )

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", RESPONSE_TEMPLATE),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )

        def contextualized_question(input: dict):
            if input.get("chat_history"):
                return contextualize_q_chain
            else:
                return input["question"]
            

        vectordb = Chroma(
            persist_directory=settings.CHROMA_DB_DIR, 
            embedding_function = settings.CHAT_EMBEDDING_MODEL,
            collection_name = f"{self.subject}_{self.grade}"
        ).as_retriever()

        docs = vectordb.get_relevant_documents(q)
        format_docs = "\n\n".join(doc.page_content for doc in docs)

        rag_chain = (
            RunnablePassthrough.assign(
                context=(lambda input : contextualize_q_chain if input.get("chat_history") else input["question"] | vectordb | format_docs)
            )
            | qa_prompt
            | TogetherLLM()
        )


        return rag_chain.invoke({"question": q, "chat_history": chat})

    
    def save(self, *args, **kwargs):
        print("saving pdf...")
        super().save(*args, **kwargs)
        print("pdf saved")
        try:
            self.embed()
        except Exception as e:
            self.delete()

            raise
       
    
    def __str__(self) -> str:
        return f"{self.pdf.name}"
    
    class Meta:
        unique_together = ["subject", "grade"]
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)

    def __str__(self) -> str:
        return f"{self.user.username}'s chat"

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=[
        ("Ai", "Ai"),
        ("Human", "Human")
    ], default="Human")
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date"]

    def __str__(self) -> str:
        return f"{self.chat.user.username}'s message ({self.type})"
    
    @property
    def pdf(self) -> PDF:
        return PDF.objects.get(subject=self.chat.subject, grade=self.chat.grade)

