from rest_framework.generics import ListCreateAPIView
from chat.models import Chat, ChatMessage
from chat.serializers import ChatSerializer

class ChatView(ListCreateAPIView):
    serializer_class = ChatSerializer
    
    def get_queryset(self):
        chat = Chat.objects.get(pk=1)
        chat.messages = ChatMessage.objects.all()

        return [chat]

    def create(self, request, *args, **kwargs):
        return "hello"