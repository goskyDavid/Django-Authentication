from django.utils.crypto import get_random_string

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from websocket.models import SocketToken


class SocketTokenView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        socket_token = getattr(user, "socket_token", None)
        token = get_random_string(length=32)
        if socket_token:
            if socket_token.is_valid():
                return Response({"token": socket_token.token}, status=HTTP_200_OK)
            socket_token.token = token
            socket_token.save()
        else:
            socket_token = SocketToken.objects.create(user=user, token=token)
        return Response({"token": token}, status=HTTP_200_OK)
