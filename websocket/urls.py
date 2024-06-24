from django.urls import re_path

from websocket.views import SocketTokenView


urlpatterns = [
    re_path(r"token/$", SocketTokenView.as_view(), name="websocket.token"),
]
