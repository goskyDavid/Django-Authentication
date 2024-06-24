from django.db.models import QuerySet

from .base import AbstractDataExportStrategy


class CompanyDataExportStrategy(AbstractDataExportStrategy):
    def get_queryset(self, filter: dict) -> QuerySet:
        from company.services import CompanyListFilterService, CompanyListQuerysetService

        get_filter_query = CompanyListFilterService(filter=filter)
        filter_query, order_by = get_filter_query()

        get_qs = CompanyListQuerysetService(filter_query=filter_query)
        return get_qs().order_by(order_by)

    def get_excel_data(self, queryset: QuerySet) -> list:
        d = [
            [
                "ID",
                "Nombre legal",
                "Nombre comercial",
                "Teléfono1",
                "Teléfono2",
                "Rango de empleados",
                "Sitio web",
                "Industria",
                "Sector económico",
                "Financiado en",
                "Estado",
                "Creado en",
            ]
        ]
        for company in queryset:
            d.append(
                [
                    company.pk,
                    company.legal_name,
                    company.trade_name or "N/A",
                    company.phone1 or "N/A",
                    company.phone2 or "N/A",
                    company.employee_range_str,
                    company.website or "N/A",
                    company.industry or "N/A",
                    (company.economic_sector and company.economic_sector.name) or "N/A",
                    (company.funded_at and company.funded_at.strftime("%Y-%m-%d %H:%M:%S")) or "N/A",
                    company.status_str,
                    (company.created_at and company.created_at.strftime("%Y-%m-%d %H:%M:%S")) or "N/A",
                ]
            )
        return d
