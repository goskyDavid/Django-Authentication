from abc import ABC, abstractproperty

from django.db.models import Q, QuerySet


class ModelQuerysetService(ABC):
    model = None

    def __init__(self, filter_query: Q = None) -> None:
        self.filter_query = filter_query

    def __call__(self) -> QuerySet:
        return self.queryset.annotate(**self.annotate).distinct()

    @property
    def queryset(self) -> QuerySet:
        qs = self.model.objects.all()
        if self.filter_query:
            qs = qs.filter(self.filter_query)
        return qs

    @abstractproperty
    def annotate(self) -> dict:
        pass
