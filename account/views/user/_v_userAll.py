from rest_framework.mixins import ListModelMixin

from account.models import User
from account.serializers import UserSimpleSerializer
from services.views import ModelPermissionRequiredView


class UserAllView(ModelPermissionRequiredView, ListModelMixin):
    serializer_class = UserSimpleSerializer
    model_permission_dict = {
        "GET": "account.view_user",
    }

    def get_queryset(self):
        return User.objects.filter(deleted=False).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
