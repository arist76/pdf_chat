from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from chat.models import Chat, ChatMessage, PDF
from chat.serializers import ChatMessageSerializer, ChatSerializer
from pdf_chat import settings


class ChatView(ListCreateAPIView):
    serializer_class = ChatMessageSerializer
    filterset_fields = ["chat__subject", "chat__grade"]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ChatMessage.objects.filter(chat__user=self.request.user)


    def create(self, request : Request, *args, **kwargs):
        
        # create chat message
        chat_message_s = ChatMessageSerializer(
            data=request.data, 
            context={"request":request}
        )
        chat_message_s.is_valid(raise_exception=True)
        chat_message : ChatMessage = chat_message_s.save()
        
        # make a query
        q = chat_message.pdf.query(chat_message.text, request.user)

        # save the ai response 
        ai_reponse = ChatMessage.objects.create(
            chat=chat_message.chat,
            type="Ai",
            text=q,
        )

        # return to user
        return Response({"answer" : q})