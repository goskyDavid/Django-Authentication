from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from account.services import TokenService
from account.serializers import UserRegistrationSerializer
from account.services import UserRenderer


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = TokenService(user).get_token()
        return Response(
            {"token": token, "msg": "Registration Success"},
            status=HTTP_201_CREATED,
        )
