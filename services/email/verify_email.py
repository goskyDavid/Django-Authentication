from django.template.loader import get_template

from .base import EmailBaseService


class SendVerifyEmailService(EmailBaseService):
    subject = "Verificacion de email"

    @property
    def content(self) -> str:
        html_template = get_template("email/verify_email.html").render(
            {
                "verification_code": self.kwargs["verification_code"],
            }
        )
        

        return html_template
