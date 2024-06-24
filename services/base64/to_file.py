import base64
import os

from django.conf import settings


class Base64ToFileService:
    def __init__(self, base64_string: str, folder_path: str, file_name: str) -> None:
        self.base64_string = base64_string
        self.folder_path = folder_path
        self.file_name = file_name

    def __call__(self) -> str:
        data_bytes = self.base64_string.encode("utf-8")

        if not os.path.exists(settings.MEDIA_ROOT + self.folder_path):
            os.makedirs(settings.MEDIA_ROOT + self.folder_path)

        file_path = self.folder_path + self.file_name
        with open(settings.MEDIA_ROOT + file_path, "wb") as file_decoded:
            file_decoded.write(base64.decodebytes(data_bytes))

        return file_path
