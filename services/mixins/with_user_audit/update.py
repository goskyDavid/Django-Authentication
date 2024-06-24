from django.db.models import Q

from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

from account.constants import UserAuditTypes

from .base import UserAuditMixin


class UpdateModelWithUserAuditMixin(UpdateModelMixin, UserAuditMixin):
    ACTION_TYPE = UserAuditTypes.UPDATE.value

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.old_data = serializer.data

        if getattr(self, "queryset_class", None):
            partial = kwargs.pop("partial", False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            instance = self.perform_update(serializer)

            get_qs = self.queryset_class(filter_query=Q(pk=instance.pk))
            instance = get_qs().first()
            serializer = self.get_serializer(instance)

            return Response(serializer.data)

        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        self.create_user_audit(instance, old_data=self.old_data, new_data=serializer.data)

        if hasattr(self, "callback_after_update"):
            self.callback_after_update(instance)

        return instance
