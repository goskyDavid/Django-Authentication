from abc import ABC, abstractmethod

from django.db.models.query import QuerySet

from account.models import DataRequest

from ...excel import GenerateExcelFileService


class AbstractDataExportStrategy(ABC):
    def __init__(self, data_request: DataRequest):
        self.data_request = data_request

    def __call__(self) -> str:
        filter_data = self.data_request.request_detail or {}
        qs = self.get_queryset(filter_data)
        excel_data = self.get_excel_data(qs)
        return self.generate_file(excel_data)

    @abstractmethod
    def get_queryset(self, filter: dict) -> QuerySet:
        pass

    @abstractmethod
    def get_excel_data(self, queryset: QuerySet) -> list:
        pass

    def generate_file(self, excel_data: list) -> str:
        generate_excel = GenerateExcelFileService(excel_data, folder_path=f"excel/{self.data_request.request_model}/")
        file_path = generate_excel()
        return file_path
