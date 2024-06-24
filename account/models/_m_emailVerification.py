import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone


class UserEmailVerification(models.Model):
    user = models.ForeignKey(
        "account.User",
        verbose_name="User",
        related_name="email_verifications",
        on_delete=models.CASCADE,
    )
    verification_code = models.CharField(max_length=7, verbose_name="Verification code")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        db_table = "user_email_verifications"

    @property
    def expired(self) -> bool:
        expiry_minutes = datetime.timedelta(minutes=settings.VERIFICATION_MINUTES)
        expiration_date = self.created_at + expiry_minutes
        return expiration_date <= timezone.now()

    def is_same_code(self, code: str) -> bool:
        return self.verification_code == code
