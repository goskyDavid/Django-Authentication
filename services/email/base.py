from django.conf import settings
from django.core.mail import send_mail


class EmailBaseService:
    subject = None

    def __init__(self, receiver_email: str, **kwargs) -> None:
        self.receiver_email = receiver_email
        self.kwargs = kwargs

    def __call__(self) -> bool:
        return self.send()

    @property
    def content(self) -> str:
        pass

    def send(self, html_message: str = None) -> bool:
        send_mail(
            subject=self.subject,
            message="" if html_message else self.content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            html_message=html_message or self.content,
            recipient_list=[self.receiver_email],
        )
        
