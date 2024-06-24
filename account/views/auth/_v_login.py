from django.contrib.auth import authenticate

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from account.models import User
from account.services import TokenService, UserEmailVerifyService
from account.serializers import LoginSerializer
from services.exceptions import BadRequest, AccountNotActivated
from django.core.mail import send_mail


class LoginView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data["email"]
        password = data["password"]

        user = User.objects.filter(email=email).first()
        if not user:
            raise BadRequest(detail="User does not exist")

        user: User = authenticate(email=email, password=password)

        if user is None:
            raise BadRequest(detail="Incorrect password")

        if user.is_active:
            token = TokenService(user).get_token()
            return Response(token, status=HTTP_200_OK)

        print(user.email + str(user.is_active) )

        # UserEmailVerifyService(user).send_code()
        subject = 'Welcome!'
        message = 'Thank you for creating an account!'
        from_email = 'ldin13198@gmail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
        
        
        raise AccountNotActivated()

