from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from forum.serializers import RoomSerializer, ChatMessageSerializer
from forum.models import Room, ChatMessage
from rest_framework.response import Response

class RoomListView(ListCreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["title_slug", "owner", "subject", "grade", "views",]
    
    def get_queryset(self):
        return Room.objects.all() 

    def perform_create(self, serializer):
        room_s = RoomSerializer(data=self.request.data)
        room_s.is_valid(raise_exception=True)
        room = Room.objects.create(**room_s.data, owner=self.request.user)
    
class RoomMessageView(ListCreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["room__title_slug"]
    
    def get_queryset(self):
        return ChatMessage.objects.filter(room__title_slug=self.kwargs.get("title_slug"))
    
    def perform_create(self, serializer):
        chat_message_s = ChatMessageSerializer(data=self.request.data)
        chat_message_s.is_valid(raise_exception=True)
        
        title_slug = self.kwargs.get("title_slug")
        room = Room.objects.get(title_slug=title_slug)

        chat_message = ChatMessage.objects.create(**chat_message_s.data, user = self.request.user, room = room)