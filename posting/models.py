from django.db import models

# Create your models here.

# class EventManager(models.Manager):
#   def by_event(self, event):
#     qlookup = Q(event)


class Event(models.Model):
  name = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
class Message(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  message = models.CharField(max_length=50)
  event = models.ForeignKey('Event', on_delete=models.CASCADE)
  
  