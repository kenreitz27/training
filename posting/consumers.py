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
    print(event_pk, me)
    
    
    #await asyncio.sleep(10)
    await self.send({
        "type": "websocket.send",
        "text": "Hello Socket"
    })
  
  async def websocket_receive(self, event):
    # When a message is received from websocket_receive
    print("received", event)
    
  async def websocket_disconnect(self, event):
    # When socket disconnects
    print("disconnected", event)