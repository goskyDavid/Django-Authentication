from django.db.models import Q

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response


class RetrieveModelWithQuerysetClassMixin(RetrieveModelMixin):
    queryset_class = None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        filter_query = Q(pk=instance.pk)
        get_qs = self.queryset_class(filter_query=filter_query)
        instance = get_qs().first()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
