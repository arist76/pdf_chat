from django.contrib import admin
from chat.models import *

admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(PDF)