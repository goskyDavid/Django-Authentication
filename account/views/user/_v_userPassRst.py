from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.serializers import PasswordResetRequestValidator

from ._v_userBase import BaseUserView


class UserPasswordResetView(BaseUserView):
    serializer_class = PasswordResetRequestValidator
    model_permission_dict = {"POST": "account.change_user"}

    def post(self, request, *args, **kwargs):
        data = request.data
        user = self.get_user()

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user.set_password(data["password"])
        user.save()

        return Response({}, status=HTTP_200_OK)
