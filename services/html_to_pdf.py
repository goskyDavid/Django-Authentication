import os
import pdfkit

from django.conf import settings

from pyvirtualdisplay import Display

os.environ["DISPLAY"] = ":99"


PDFKIT_OPTIONS = {
    "page-size": "A4",
    "margin-top": "0.75in",
    "margin-right": "0.75in",
    "margin-bottom": "0.75in",
    "margin-left": "0.75in",
    "encoding": "UTF-8",
}


class HtmlToPDFService:
    def __init__(self, html_string: str, file_name: str, folder_path: str = "tmp/") -> None:
        self.html_string = html_string
        self.file_name = file_name
        self.folder_path = folder_path

        if not self.folder_path.endswith("/"):
            self.folder_path += "/"
        if not os.path.exists(settings.MEDIA_ROOT + self.folder_path):
            os.makedirs(settings.MEDIA_ROOT + self.folder_path)

    def __call__(self) -> str:
        file_path = f"{self.folder_path}{self.file_name}"

        if settings.HAS_DISPLAY:
            pdfkit.from_string(self.html_string, settings.MEDIA_ROOT + file_path, options=PDFKIT_OPTIONS)
        else:
            with Display() as display:
                pdfkit.from_string(self.html_string, settings.MEDIA_ROOT + file_path, options=PDFKIT_OPTIONS)
                display.stop()

        return file_path
