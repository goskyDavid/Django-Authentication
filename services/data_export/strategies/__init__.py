from typing import Union

from .company import CompanyDataExportStrategy
from .person import PersonDataExportStrategy


DATA_EXPORT_STRATEGY = Union[CompanyDataExportStrategy, PersonDataExportStrategy]


class DataExportStrategyFactory:
    strategies = {
        "company": CompanyDataExportStrategy,
        "person": PersonDataExportStrategy,
    }

    @classmethod
    def get_strategy(cls, label: str) -> DATA_EXPORT_STRATEGY:
        return cls.strategies[label]
