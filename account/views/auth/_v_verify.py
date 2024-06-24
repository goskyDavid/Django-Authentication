from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.models import User
from account.services import UserEmailVerifyService
from services.exceptions import BadRequest


class VerifyView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get_user(self) -> User:
        email = self.request.data.get("email", "")
        user = User.objects.filter(email=email).first()
        if not user:
            raise BadRequest(detail="User does not exist")
        return user

    def post(self, request, *args, **kwargs):
        data = request.data
        user = self.get_user()
        if user.is_active:
            raise BadRequest(detail="Your email is now verified, please log in.")
        UserEmailVerifyService(user).verify(data.get("code"))
        return Response({}, status=HTTP_200_OK)
