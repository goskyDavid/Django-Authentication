from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from account.serializers import UserRegisterSerializer
from account.services import UserEmailVerifyService


class RegisterView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        UserEmailVerifyService(user).send_code()

        return Response({}, status=HTTP_201_CREATED)
