from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from pdf_chat import settings
# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    subject = models.CharField(max_length=150, choices=settings.DEFAULT_SUBJECTS)
    grade = models.CharField(max_length=2, choices=settings.GRADES)

    def save(self, *args, **kwargs):
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Room {self.id}, Owner {self.owner.id}"

class ChatMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def upvote(self):
        self.upvote += 1
        self.save()

    def downvote(self):
        self.upvote += 1
        self.save()

    def __str__(self):
        return f"Message {self.id}, Room {self.room.id}"

