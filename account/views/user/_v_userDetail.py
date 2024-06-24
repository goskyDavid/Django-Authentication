from account.constants import UserAuditTypes
from account.mixins import UpdateUserMixin
from account.serializers import UserSerializer
from services.mixins import SoftDeleteModelWithUserAuditMixin

from ._v_userBase import BaseUserView


class UserDetailView(BaseUserView, UpdateUserMixin, SoftDeleteModelWithUserAuditMixin):
    serializer_class = UserSerializer
    model_permission_dict = {"PUT": "account.change_user", "DELETE": "account.delete_user"}
    MODEL_NAME = "user"

    def get_object(self):
        return self.get_user()

    def get_user_audit_action_type(self) -> str:
        if self.request.method == "PUT":
            return UserAuditTypes.UPDATE.value
        return UserAuditTypes.SOFT_DELETE.value

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
