from websocket.constants import NOTIFICATION_GROUP_NAME

from .base import BaseSendMessageService


class SendNotificationService(BaseSendMessageService):
    group_name = NOTIFICATION_GROUP_NAME
