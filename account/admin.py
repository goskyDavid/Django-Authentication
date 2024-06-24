from django.contrib import admin

from account.models import UserAudit


class UserAuditAdmin(admin.ModelAdmin):
    list_display = ("id", "model_name", "model_id", "type", "user", "created_at")
    raw_id_fields = ("user",)
    readonly_fields = ("user", "type", "model_name", "model_id", "old_data", "new_data", "created_at")


admin.site.register(UserAudit, UserAuditAdmin)
