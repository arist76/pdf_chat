from django.db import models
from django.contrib.auth.models import User
from pdf_chat import settings

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=[
        ("ai", "ai"),
        ("user", "user")
    ])
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
