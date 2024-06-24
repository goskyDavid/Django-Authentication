from django.db.models import Q
from django.utils import timezone
from django.utils.crypto import get_random_string

from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from account.constants import UserAuditTypes
from account.models import User
from account.serializers import UserSerializer
from services.mixins import UserAuditMixin, SendNotificationMixin
from services.views import ModelPermissionRequiredView
from websocket.constants import NotificationTypes


class UserListView(ModelPermissionRequiredView, ListModelMixin, UserAuditMixin, SendNotificationMixin):
    serializer_class = UserSerializer
    model_permission_dict = {
        "GET": "account.view_user",
        "POST": "account.add_user",
    }
    MODEL_NAME = "user"
    ACTION_TYPE = UserAuditTypes.CREATE.value
    NOTIFICATION_TYPE = NotificationTypes.NEW_USER.value

    def get_queryset(self):
        search_key = self.request.GET.get("searchKey")
        gender = self.request.GET.get("gender")
        status = self.request.GET.get("status")

        filter_query = Q()
        if search_key:
            filter_query &= (
                Q(email__icontains=search_key)
                | Q(first_name__icontains=search_key)
                | Q(last_name__icontains=search_key)
                | Q(phone__icontains=search_key)
                | Q(rut__icontains=search_key)
            )
        if gender:
            filter_query &= Q(gender=gender)
        if status:
            if status == "active":
                filter_query &= Q(deleted=False)
            elif status == "deleted":
                filter_query &= Q(deleted=True)

        return User.objects.filter(filter_query).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data

        password = get_random_string(length=8)
        data["password"] = password

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_active=True, email_verified_at=timezone.now())

        # TODO: Send email
        self.send_notification(user)
        self.create_user_audit(user, new_data=data)

        return Response(serializer.data, status=HTTP_201_CREATED)
