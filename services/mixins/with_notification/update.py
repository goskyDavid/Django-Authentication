from rest_framework.mixins import UpdateModelMixin

from .base import SendNotificationMixin


class UpdateModelWithNotificationMixin(UpdateModelMixin, SendNotificationMixin):
    def perform_update(self, serializer):
        instance = serializer.save()
        self.send_notification(instance=instance)
        return instance
