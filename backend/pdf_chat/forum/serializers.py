from rest_framework import serializers
from django.utils.text import slugify
from forum.models import Room, ChatMessage


class RoomSerializer(serializers.ModelSerializer):
    
    def to_internal_value(self, data):
        data["title_slug"] = slugify(data["title"])
        return data
    class Meta:
        model = Room
        exclude = ["owner"]
        read_only_fields = ["title_slug", "views", "upvotes", "downvotes"]

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        exclude = ["user"]
        read_only_fields = ["upvotes", "downvotes", "date", "room"]
        