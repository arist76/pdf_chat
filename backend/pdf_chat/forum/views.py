from rest_framework.generics import ListCreateAPIView
from forum.serializers import RoomSerializer, ChatMessageSerializer


class RoomListView(ListCreateAPIView):
    serializer_class = RoomSerializer
    authentication_classes = [IsAuthenticated]

class ChatMessageSerializer():
    pass