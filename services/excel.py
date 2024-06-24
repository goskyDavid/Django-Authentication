import openpyxl
import os

from django.conf import settings

from .helpers import get_uuid


class GenerateExcelFileService:
    def __init__(self, data: list, file_name: str = None, folder_path: str = None):
        self.data = data
        self.file_name = file_name or get_uuid() + ".xlsx"
        self.folder_path = folder_path or "tmp/"

        if not os.path.exists(settings.MEDIA_ROOT + self.folder_path):
            os.makedirs(settings.MEDIA_ROOT + self.folder_path)

    def __call__(self) -> str:
        wb = openpyxl.Workbook()
        ws = wb.active
        for item in self.data:
            ws.append(item)
        file_path = f"{self.folder_path}{self.file_name}"
        wb.save(filename=f"{settings.MEDIA_ROOT}{file_path}")
        return file_path
