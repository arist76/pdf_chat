from django.urls import path
from forum.views import RoomListView, RoomMessageView


urlpatterns = [
    path("", RoomListView.as_view()),
    path("<slug:title_slug>/", RoomMessageView.as_view()),
]
