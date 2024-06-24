# from account.models import DataRequest

# from .strategies import DataExportStrategyFactory


# class DataExportService:
#     def __init__(self, data_request: DataRequest) -> None:
#         self.data_request = data_request

#     def __call__(self) -> str:
#         strategy = DataExportStrategyFactory.get_strategy(self.data_request.request_model)
#         export_data = strategy(self.data_request)
#         return export_data()
