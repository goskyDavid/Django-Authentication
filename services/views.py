from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import ModelPermissionRequired, IsSuperUser


class ModelPermissionRequiredView(GenericAPIView):
    model_permission_dict = dict()
    permission_classes = [IsAuthenticated, ModelPermissionRequired]


class SuperUserRequiredView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
