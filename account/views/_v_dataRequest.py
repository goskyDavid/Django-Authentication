from rest_framework.generics import GenericAPIView

from account.constants import DataRequestStatus
from account.models import DataRequest
from account.serializers import DataRequestSerializer
from services.exceptions import BadRequest
from services.mixins import CreateModelWithUserAuditMixin


class DataRequestListView(GenericAPIView, CreateModelWithUserAuditMixin):
    serializer_class = DataRequestSerializer
    MODEL_NAME = "data_request"

    def post(self, request, *args, **kwargs):
        data = request.data
        if DataRequest.objects.filter(
            user=request.user, status=DataRequestStatus.PENDING.value, request_model=data["request_model"]
        ).exists():
            raise BadRequest("Tiene solicitud pendiente, espere la aprobación del administrador")

        return self.create(request, *args, **kwargs, additional_kwargs={"user": request.user})

    def callback_after_create(self, instance: DataRequest):
        # TODO: Send email to admins
        ...
