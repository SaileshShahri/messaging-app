from django.contrib import admin

# Register your models here.

from .models import Connection, Message

admin.site.register(Connection)
admin.site.register(Message)