import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .  models import *
from  django.contrib.auth.models import User
from django.contrib.auth import get_user_model



    
class PersonalChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def update_user_status(self,my_id,status):
        print(my_id,status)
        User = get_user_model()
        obj=User.objects.get(pk=my_id)
        print(obj)
        obj.statuss=status
        obj.save()
        return  0
    
    async def connect(self):
        print("Hello")
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
       
        print(my_id, "=\==", other_user_id)
      
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
            print("if condition")
            await self.update_user_status(my_id,True)
        else:
            self.room_name = f'{other_user_id}-{my_id}'
            print("else condition")
            await self.update_user_status(my_id,True)

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
            
        )
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': "online",
                'username': str(self.scope['user']),
            }
        )


    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        
        await self.save_message(username, self.room_group_name, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
    async def disconnect(self, code):
        my_id = self.scope['user'].id
        print("Disconect")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': "offline",
                'username': str(self.scope['user']),
            }
        )
        await self.update_user_status(my_id,False)
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
            
        )
        
    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name)
