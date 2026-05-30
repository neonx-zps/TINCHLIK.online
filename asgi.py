import json
from channels.generic.websocket import AsyncWebsocketConsumer

ONLINE_USERS = set()

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.username = self.scope["user"].username if self.scope["user"].is_authenticated else "Guest"

        ONLINE_USERS.add(self.username)

        await self.channel_layer.group_add("chat", self.channel_name)
        await self.accept()

        await self.broadcast_users()

    async def disconnect(self, close_code):
        ONLINE_USERS.discard(self.username)

        await self.channel_layer.group_discard("chat", self.channel_name)
        await self.broadcast_users()

    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data["message"]

        await self.channel_layer.group_send(
            "chat",
            {
                "type": "chat_message",
                "message": message,
                "user": self.username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def broadcast_users(self):
        from channels.layers import get_channel_layer
        layer = get_channel_layer()

        await layer.group_send(
            "chat",
            {
                "type": "user_list",
                "users": list(ONLINE_USERS)
            }
        )

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            "type": "users",
            "users": event["users"]
        }))