from django.db import models

from account.constants import UserAuditTypes


class UserAudit(models.Model):
    user = models.ForeignKey(
        "account.User", verbose_name="User", related_name="audits", on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=31, default=UserAuditTypes.CREATE.value, verbose_name="Type", choices=UserAuditTypes.choices()
    )
    model_name = models.CharField(max_length=127, verbose_name="Model name")
    model_id = models.CharField(max_length=127, verbose_name="Model ID")
    principle_model_name = models.CharField(max_length=127, blank=True, null=True, verbose_name="Principle model name")
    principle_model_id = models.CharField(max_length=127, blank=True, null=True, verbose_name="Principle model ID")
    old_data = models.JSONField(blank=True, null=True, verbose_name="Old data")
    new_data = models.JSONField(blank=True, null=True, verbose_name="New data")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_audits"

    def __str__(self) -> str:
        return f"{self.model_name}-{self.model_id}-{self.type}"
