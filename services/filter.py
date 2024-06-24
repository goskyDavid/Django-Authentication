from abc import ABC, abstractmethod

from django.db.models import Q


class ModelListFilterService(ABC):
    def __init__(self, filter: dict):
        self.filter = filter

    def __call__(self) -> tuple:
        return self.filter_query, self.order_by

    @property
    @abstractmethod
    def filter_query(self) -> Q:
        pass

    @property
    def order_by(self) -> str:
        sort_key = self.filter.get("sortKey")
        sort_direction = self.filter.get("sortDirection")

        ob = "-created_at"
        if sort_key and sort_direction:
            ob = sort_key
            if sort_direction == "desc":
                ob = f"-{ob}"

        return ob
