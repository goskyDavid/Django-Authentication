from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.models import User
from account.services import UserEmailVerifyService
from services.exceptions import BadRequest

class SendVerifyCodeView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get_object(self):
        email = self.request.data.get("email", "")
        user = User.objects.filter(email=email).first()
        if not user:
            raise BadRequest(detail="User does not exist")
        return user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        UserEmailVerifyService(user).send_code()
        return Response({}, status=HTTP_200_OK)


class PasswordResetView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get_object(self):
        email = self.request.data.get("email", "")
        user = User.objects.filter(email=email).first()
        if not user:
            raise BadRequest(detail="User does not exist")
        return user

    def post(self, request, *args, **kwargs):
        data = request.data
        user = self.get_object()
        if UserEmailVerifyService(user).is_valid_code(data["code"]):
            user.set_password(data["password"])
            user.save()
        else:
            raise BadRequest(detail="The verification code is invalid")
        return Response({}, status=HTTP_200_OK)