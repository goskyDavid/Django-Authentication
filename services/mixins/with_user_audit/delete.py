from rest_framework.mixins import DestroyModelMixin

from account.constants import UserAuditTypes

from .base import UserAuditMixin


class DeleteModelWithUserAuditMixin(DestroyModelMixin, UserAuditMixin):
    ACTION_TYPE = UserAuditTypes.DELETE.value

    def perform_destroy(self, instance):
        self.create_user_audit(instance)
        return super().perform_destroy(instance)
