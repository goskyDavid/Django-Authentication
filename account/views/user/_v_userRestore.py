from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.constants import UserAuditTypes
from services.mixins import UserAuditMixin

from ._v_userBase import BaseUserView


class UserRestoreView(BaseUserView, UserAuditMixin):
    model_permission_dict = {"POST": "account.delete_user"}
    MODEL_NAME = "user"
    ACTION_TYPE = UserAuditTypes.RESTORE.value

    def get_object(self):
        return self.get_user()

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        user.deleted = False
        user.deleted_at = None
        user.save()
        self.create_user_audit(user)
        return Response({}, status=HTTP_200_OK)
