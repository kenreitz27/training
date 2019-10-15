import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Event, Message

class MessageConsumer(AsyncConsumer):
  async def websocket_connect(self, event):
    print("connected", event)
    await self.send({
      "type": "websocket.accept"
    })
    
    event_pk = self.scope['url_route']['kwargs']['event_pk']
    me = self.scope['user']
   # print(event_pk, me)
   # golf_event = await self.get_event_name(event_pk) 
   # print(golf_event)
    
    #await asyncio.sleep(10)
    await self.send({
        "type": "websocket.send",
        "text": "Hello Socket"
    })
  
  async def websocket_receive(self, event):
    # When a message is received from websocket_receive
    print("received", event)
    # {'type': 'websocket.receive', 'text': '{"message":"this is a test"}'}
    front_text = event.get('text', None)
    if front_text is not None:
      loaded_dict_data = json.loads(front_text)
      msg = loaded_dict_data.get('message')
      print(msg)
      
      await self.send({
          "type": "websocket.send",
          "text": msg
      })

      
      
      
  async def websocket_disconnect(self, event):
    # When socket disconnects
    print("disconnected", event)

  @database_sync_to_async  
  async def get_event_name(self, event_pk):
    return Event.objects.get(pk=event_pk)
   