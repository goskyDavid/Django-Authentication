from abc import ABC

from websocket.services import SendNotificationService


class SendNotificationMixin(ABC):
    NOTIFICATION_TYPE = None

    def send_notification(self, instance=None):
        try:
            author = self.request and self.request.user and self.request.user.pk
            notification_data = {
                "type": self.NOTIFICATION_TYPE,
                "data": {
                    "id": instance and instance.pk,
                    "name": str(instance) if instance else "",
                    "author": author,
                },
            }

            send_notification = SendNotificationService(data=notification_data, author=author)
            send_notification()
        except Exception as e:
            print(f"Sending notification failed with reason - {str(e)}")
