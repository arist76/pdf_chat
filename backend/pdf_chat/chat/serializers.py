from rest_framework import serializers 
from models import ChatMessage, Chat


class ChatSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Chat


class ChatMessageSerializer():
    
    class Meta:
        model = ChatMessage