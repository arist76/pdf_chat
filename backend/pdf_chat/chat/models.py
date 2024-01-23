from collections.abc import Iterable
import os
from django.db import models
from django.contrib.auth.models import User
from pdf_chat import settings
from langchain.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from pdf_chat.settings import CHAT_EMBEDDING_MODEL, MEDIA_ROOT
import chromadb
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)

    def __str__(self) -> str:
        return f"{self.user.username}'s chat"

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=[
        ("ai", "ai"),
        ("user", "user")
    ])
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.chat.user.username}'s message ({self.type})"


def pdfUploadPath(instance, filename : str):
    return f"{instance.grade}/{instance.subject}/{filename.replace(' ', '')}"

class PDF(models.Model):
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)
    pdf = models.FileField(upload_to=pdfUploadPath)

    __embedded = False
    __client = chromadb.PersistentClient()

    def embed(self):
        if not self.__embedded:
            # load pdf file
            docs = PyPDFLoader(
                os.path.join(
                    MEDIA_ROOT, 
                    self.pdf.name
                )
            ).load()

            # split the file
            splited_docs = CharacterTextSplitter(
                chunk_size=1000, chunk_overlap=0
            ).split_documents(docs)

            # embed the file and persist locally
            collection = self.__client.get_or_create_collection(
                f"{self.grade}_{self.subject}", 
                embedding_function=CHAT_EMBEDDING_MODEL
            )

            collection.add(
                ids=[str(splited_docs.index(x)) for x in splited_docs],
                documents=splited_docs,
            )

            self.__embedded = True
    
    def query(self, q):
        collection = self.__client.get_or_create_collection(
            f"{self.grade}_{self.subject}", 
            embedding_function=CHAT_EMBEDDING_MODEL
        )
        docs = collection.query(q)
        return docs
    
    def __str__(self) -> str:
        return f"{self.pdf.name}"
    
    class Meta:
        unique_together = ["subject", "grade"]