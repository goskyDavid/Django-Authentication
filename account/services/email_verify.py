from django.conf import settings
from django.utils import timezone
from django.utils.crypto import get_random_string


from account.models import User, UserEmailVerification
from services import SendVerifyEmailService
from services.exceptions import BadRequest


class UserEmailVerifyService:
    def __init__(self, user: User) -> None:
        self.user = user

    @property
    def verification_code(self):
        if settings.DEBUG:
            return "000000"
        return get_random_string(length=6, allowed_chars="1234567890")

    def remove_prev(self) -> None:
        self.user.email_verifications.all().delete()

    def is_valid_code(self, code: str) -> bool:
        email_verification = self.user.email_verifications.first()
        if email_verification.expired:
            raise BadRequest(detail="El código de verificación ha caducado")
        return email_verification.is_same_code(code)

    def send_code(self) -> None:
        self.remove_prev()
        verification_code = self.verification_code
        UserEmailVerification.objects.create(user=self.user, verification_code=verification_code)
        send_verify_email = SendVerifyEmailService(self.user.email, verification_code=verification_code)
        send_verify_email()

    def verify(self, code: str) -> None:
        if self.user.is_active:
            return

        if self.is_valid_code(code):
            self.remove_prev()
            self.user.is_active = True
            self.user.email_verified_at = timezone.now()
            self.user.save(update_fields=("is_active", "email_verified_at"))
        else:
            raise BadRequest(detail="El código de verificación no es válido")
