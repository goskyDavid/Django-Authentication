from django.template.loader import get_template

from ..base import EmailBaseService


class SendDataRequestApproveEmailService(EmailBaseService):
    subject = "Solicitud de datos aprobada"

    @property
    def content(self) -> str:
        html_template = get_template("email/data_request_approved.html").render(
            {
                "motive": self.kwargs["motive"],
                "intended_use": self.kwargs["intended_use"],
                "file_link": self.kwargs["file_link"],
            }
        )

        return html_template
