from django.contrib.auth.models import AnonymousUser

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

from websocket.models import SocketToken


@database_sync_to_async
def get_user(token):
    socket_token = SocketToken.objects.filter(token=token).first()
    if socket_token:
        return socket_token.user
    return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            token = (dict((x.split("=") for x in scope["query_string"].decode().split("&")))).get("token", None)
        except ValueError:
            token = None
        scope["user"] = AnonymousUser() if token is None else await get_user(token)
        return await super().__call__(scope, receive, send)
