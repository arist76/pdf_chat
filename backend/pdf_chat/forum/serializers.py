from rest_framework import serializers
from django.utils.text import slugify
from forum.models import Room, ChatMessage


class RoomSerializer(serializers.ModelSerializer):
    
    def to_internal_value(self, data):
        data["title_slug"] = slugify(data["title"])
        return super().to_internal_value(data)
    class Meta:
        model = Room
        fields = "__all__"
        read_only_fields = ["title_slug", "views", "upvotes", "downvotes", "owner"]

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ["upvotes", "downvotes", "date", "room", "user"]
        