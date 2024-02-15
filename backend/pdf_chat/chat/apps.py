from django.apps import AppConfig
from pdf_chat import settings

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    # def ready(self) -> None:
    #     client = chromadb.PersistentClient()
    #     collection = client.get_or_create_collection("pdf", embedding_function=settings.CHAT_EMBEDDING_MODEL)