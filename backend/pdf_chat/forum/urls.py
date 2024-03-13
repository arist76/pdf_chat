from django.urls import path
from forum.views import RoomListView, RoomMessageView, room_message_upvote, room_message_downvote


urlpatterns = [
    path("", RoomListView.as_view()),
    path("<slug:title_slug>/", RoomMessageView.as_view()),
    path("<slug:title_slug>/upvote", room_message_upvote),
    path("<slug:title_slug>/downvote", room_message_downvote)
]
