from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from account.models import User


class CheckUserEmailView(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get_queryset(self, request, *args,):
        email = request.data.get("email", "")
        return User.objects.filter(email=email)

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        if queryset.exists():
            raise ValidationError
        return Response(dict(), status=status.HTTP_200_OK)
