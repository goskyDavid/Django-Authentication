from django.db.models import Q

from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from account.constants import UserAuditTypes

from ..with_notification import SendNotificationMixin
from ..with_user_audit import UserAuditMixin


class CreateModelWithNotificationAndUserAuditMixin(CreateModelMixin, SendNotificationMixin, UserAuditMixin):
    ACTION_TYPE = UserAuditTypes.CREATE.value

    def create(self, request, *args, **kwargs):
        if "additional_kwargs" in kwargs:
            self.additional_kwargs = kwargs["additional_kwargs"]
        else:
            self.additional_kwargs = None

        if getattr(self, "queryset_class", None):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = self.perform_create(serializer)

            get_qs = self.queryset_class(filter_query=Q(pk=instance.pk))
            instance = get_qs().first()
            serializer = self.get_serializer(instance)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if self.additional_kwargs:
            instance = serializer.save(**self.additional_kwargs)
        else:
            instance = serializer.save()
        self.send_notification(instance=instance)
        self.create_user_audit(instance, new_data=serializer.data)
        return instance
