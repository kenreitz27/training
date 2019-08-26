from django.contrib import admin
from posting.models import Event, Message

# Register your models here.

class EventAdmin(admin.ModelAdmin):
  pass

class MessageAdmin(admin.ModelAdmin):
  pass

admin.site.register(Event, EventAdmin)
admin.site.register(Message, MessageAdmin)

