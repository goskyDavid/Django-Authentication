import json

from django.contrib.auth.models import AnonymousUser

from channels.generic.websocket import AsyncWebsocketConsumer

from websocket.constants import NOTIFICATION_GROUP_NAME


class NotificationConsumer(AsyncWebsocketConsumer):
    group_name = NOTIFICATION_GROUP_NAME

    async def connect(self):
        self.user = self.scope["user"]

        if isinstance(self.user, AnonymousUser):
            await self.close()

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_send(
            self.group_name, {"type": "group.message", "message": json.loads(text_data), "author": self.user.user_id}
        )

    async def group_message(self, event):
        author = event.get("author")
        if author == self.user.pk:
            return

        await self.send(text_data=json.dumps(event.get("message", {})))
