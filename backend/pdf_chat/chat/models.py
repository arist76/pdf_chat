from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from pdf_chat import settings
from pdf_chat.settings import MEDIA_ROOT
from chat.chain import RESPONSE_TEMPLATE, TogetherLLM
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI
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
            # load pdf fileuuuuu
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
        vectordb = Chroma(
            collection_name = f"{self.subject}_{self.grade}",
            embedding_function = settings.CHAT_EMBEDDING_MODEL,
            persist_directory=settings.CHROMA_DB_DIR
        )
        docs = vectordb.similarity_search(q, k=5)

        chain = load_qa_chain(ChatOpenAI(), chain_type="stuff")
        output = chain.run(input_documents=docs, question=q)

        return output
    
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
    
    class Meta:
        unique_together = ["user", "subject", "grade"]

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

