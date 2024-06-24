from django.db import models
from django.utils import timezone

from account.constants import DataRequestStatus


class DataRequest(models.Model):
    user = models.ForeignKey("account.User", blank=True, related_name="data_requests", on_delete=models.CASCADE)

    motive = models.TextField()
    intended_use = models.TextField()

    request_model = models.CharField(max_length=255)
    request_detail = models.JSONField(blank=True, null=True)
    file_link = models.CharField(max_length=1023, null=True, blank=True)

    status = models.CharField(
        max_length=31, default=DataRequestStatus.PENDING.value, choices=DataRequestStatus.choices()
    )
    admin_note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    status_updated_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "data_requests"

    def __str__(self):
        return f"{self.user} - {self.request_model} - {self.status}"

    def approve(self, file_link: str) -> None:
        self.status = DataRequestStatus.APPROVED.value
        self.file_link = file_link
        self.status_updated_at = timezone.now()
        self.save()

    def reject(self, admin_note: str) -> None:
        self.status = DataRequestStatus.REJECTED.value
        self.admin_note = admin_note
        self.status_updated_at = timezone.now()
        self.save()
