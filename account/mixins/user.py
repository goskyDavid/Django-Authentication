from services.mixins import UpdateModelWithNotificationAndUserAuditMixin
from websocket.constants import NotificationTypes


class UpdateUserMixin(UpdateModelWithNotificationAndUserAuditMixin):
    NOTIFICATION_TYPE = NotificationTypes.UPDATE_USER.value
    MODEL_NAME = "user"
