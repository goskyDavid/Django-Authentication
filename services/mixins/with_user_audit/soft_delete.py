from account.constants import UserAuditTypes

from ..soft_delete import SoftDeleteModelMixin
from .base import UserAuditMixin


class SoftDeleteModelWithUserAuditMixin(SoftDeleteModelMixin, UserAuditMixin):
    ACTION_TYPE = UserAuditTypes.SOFT_DELETE.value

    def perform_destroy(self, instance):
        self.create_user_audit(instance)
        return super().perform_destroy(instance)
