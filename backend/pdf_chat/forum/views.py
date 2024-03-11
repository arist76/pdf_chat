from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from forum.serializers import RoomSerializer, ChatMessageSerializer
from forum.models import Room, ChatMessage

class RoomListView(ListCreateAPIView):
    serializer_class = RoomSerializer
    authentication_classes = [IsAuthenticated]

    def get_queryset(self):
        return Room.objects.all() 

class ChatMessageSerializer():
    serializer_class = ChatMessageSerializer
    authentication_classes = [IsAuthenticated]