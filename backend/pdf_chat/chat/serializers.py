from rest_framework import serializers 
from chat.models import ChatMessage, Chat

class ChatMessageSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ChatMessage
        exclude = ["chat"]

class ChatSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = "__all__"