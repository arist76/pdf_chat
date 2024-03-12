from rest_framework import serializers 
from chat.models import ChatMessage, Chat

class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chat
        exclude = ["user"]

class ChatMessageSerializer(serializers.ModelSerializer):    
    chat = ChatSerializer()
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ["type", "date"]

    def create(self, validated_data):
        chat_data = validated_data.pop("chat")
        # get or create chat
        chat_s = ChatSerializer(data=chat_data) 
        chat_s.is_valid(raise_exception=True)

        chat, created = Chat.objects.get_or_create(**chat_s.data, user=self.context["request"].user)

        return ChatMessage.objects.create(
            chat = chat,
            **validated_data
        )
