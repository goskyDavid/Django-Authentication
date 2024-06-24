from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class BaseSendMessageService:
    group_name = None

    def __init__(self, data: dict, group_name: str = None, author: str = None) -> None:
        self.data = data
        if group_name:
            self.group_name = group_name
        self.author = author

    def __call__(self) -> None:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            self.group_name, {"type": "group.message", "message": self.data, "author": self.author}
        )
