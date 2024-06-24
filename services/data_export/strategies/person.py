from django.db.models import QuerySet

from account.constants import Gender
from person.services import PersonListQuerysetService

from .base import AbstractDataExportStrategy


class PersonDataExportStrategy(AbstractDataExportStrategy):
    def get_queryset(self, filter: dict) -> QuerySet:
        from person.services import PersonListFilterService

        get_filter_query = PersonListFilterService(filter=filter)
        filter_query, order_by = get_filter_query()

        get_qs = PersonListQuerysetService(filter_query=filter_query)
        return get_qs().order_by(order_by)

    def get_excel_data(self, queryset: QuerySet) -> list:
        d = [
            [
                "ID",
                "RUT",
                "Nombre completo",
                "Nombre paterno",
                "Nombre materno",
                "Cumpleaños",
                "Género",
                "Comuna",
                "Empresas Relacionadas",
                "Intereses",
                "Latitud",
                "Longitud",
                "Creado en",
            ]
        ]
        for person in queryset:
            d.append(
                [
                    person.pk,
                    person.rut or "N/A",
                    person.full_name or "N/A",
                    person.paternal_name or "N/A",
                    person.maternal_name or "N/A",
                    (person.birth_date and person.birth_date.strftime("%Y-%m-%d")) or "N/A",
                    (person.gender and str(Gender(person.gender))) or "N/A",
                    (person.commune and person.commune.name) or "N/A",
                    person.company_number or 0,
                    person.interest_number or 0,
                    person.latitude or "N/A",
                    person.longitude or "N/A",
                    (person.created_at and person.created_at.strftime("%Y-%m-%d %H:%M:%S")) or "N/A",
                ]
            )
        return d
