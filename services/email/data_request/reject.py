from django.template.loader import get_template

from ..base import EmailBaseService


class SendDataRequestRejectEmailService(EmailBaseService):
    subject = "Solicitud de datos rechazada"

    @property
    def content(self) -> str:
        html_template = get_template("email/data_request_rejected.html").render(
            {
                "motive": self.kwargs["motive"],
                "intended_use": self.kwargs["intended_use"],
                "admin_note": self.kwargs["admin_note"],
            }
        )

        return html_template
