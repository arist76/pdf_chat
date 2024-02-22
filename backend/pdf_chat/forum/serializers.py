from rest_framework.serializers import ModelSerializer
from pdf_chat.models import Room, ChatMessage


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class ChatMessageSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"