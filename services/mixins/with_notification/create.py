from rest_framework.mixins import CreateModelMixin

from .base import SendNotificationMixin


class CreateModelWithNotificationMixin(CreateModelMixin, SendNotificationMixin):
    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notification(instance=instance)
        return instance
