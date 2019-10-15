from django.shortcuts import render
from posting.models import Event, Message
from posting.forms import MessageForm

# Create your views here.

def user_list(request):
  return render(request, 'user_list.html')

# List all the events

def event_list(request):
  events = Event.objects.all()
  context = {
    "events": events,
  }
  return render(request, 'event_list.html', context)

# Monitor the event being watched

def event_monitor(request, event_pk):
  event = Event.objects.get(pk=event_pk)
  messages = reversed(Message.objects.filter(event=event).order_by('-created_on')[:3])
  
  context = {
    "event": event,
    "messages": messages,
  }
  
  return render(request, 'event_monitor.html', context)

# Send messages sending to event

def post_info(request, event_pk):
  event = Event.objects.get(pk = event_pk)

  
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
     
      message = Message(
        message=form.cleaned_data["message"],
        event=event
      )
      message.save()
      
  form = MessageForm()
  messages = reversed(Message.objects.filter(event=event).order_by('-created_on')[:100])
  
  context = {
    "event": event,
    "messages": messages,
    "form": form,
  }
  return render(request, 'post_info.html', context)

