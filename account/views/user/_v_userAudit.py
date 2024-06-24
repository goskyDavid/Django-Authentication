from rest_framework.mixins import ListModelMixin

from account.models import UserAudit
from account.serializers import UserAuditSerializer
from services.permissions import IsSuperUser

from ._v_userBase import BaseUserView


class UserAuditListView(BaseUserView, ListModelMixin):
    permission_classes = [IsSuperUser]
    serializer_class = UserAuditSerializer

    def get_queryset(self):
        user = self.get_user()
        return UserAudit.objects.filter(user=user).order_by("-created_at")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
