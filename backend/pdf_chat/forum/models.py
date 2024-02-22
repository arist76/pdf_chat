from django.db import models
from django.contrib.auth.models import User
from pdf_chat import settings
# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)
    views = models.IntegerField()



class ChatMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

