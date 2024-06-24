from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin

from account.mixins import UpdateProfileMixin
from account.serializers import ProfileSerializer


class UserProfileView(GenericAPIView, RetrieveModelMixin, UpdateProfileMixin):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs, partial=True)
