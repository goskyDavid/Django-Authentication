from django.conf import settings
from django.db import models
from django.utils import timezone


class SocketToken(models.Model):
    user = models.OneToOneField(
        "account.User", verbose_name="User", related_name="socket_token", on_delete=models.CASCADE
    )

    token = models.CharField(max_length=63, verbose_name="Token")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "socket_tokens"

    def __str__(self) -> str:
        return self.user.email

    def is_valid(self) -> bool:
        now = timezone.now()
        expire_date = self.updated_at + timezone.timedelta(days=settings.WEBSOCKET_TOKEN_LIFETIME)
        return expire_date > now
