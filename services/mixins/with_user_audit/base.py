from abc import ABC

from account.models import UserAudit


class UserAuditMixin(ABC):
    MODEL_NAME = None
    PRINCIPLE_MODEL_NAME = None
    PRINCIPLE_MODEL_PK_FIELD = None
    ACTION_TYPE = None

    def get_user_audit_action_type(self) -> str:
        pass

    def create_user_audit(self, instance, old_data: dict = None, new_data: dict = None) -> UserAudit:
        u = self.request and self.request.user
        if u:
            try:
                action_type = self.ACTION_TYPE
                if hasattr(self, "get_user_audit_action_type"):
                    if self.get_user_audit_action_type():
                        action_type = self.get_user_audit_action_type()
                return UserAudit.objects.create(
                    user=u,
                    type=action_type,
                    model_name=self.MODEL_NAME,
                    model_id=(instance and str(instance.pk)) or "-",
                    principle_model_name=self.PRINCIPLE_MODEL_NAME,
                    principle_model_id=getattr(instance, self.PRINCIPLE_MODEL_PK_FIELD, None)
                    if self.PRINCIPLE_MODEL_PK_FIELD and instance
                    else None,
                    old_data=old_data,
                    new_data=new_data,
                )
            except Exception as e:
                print(f"UserAudit creation failed with reason - `{str(e)}`")
        print("UserAudit creation failed because user instance is `None`")
