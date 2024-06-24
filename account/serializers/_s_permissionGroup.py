from django.contrib.auth.models import Group
from rest_framework import serializers
from ._s_permission import ProfilePermissionSerializer


class ProfilePermissionGroupSerializer(serializers.ModelSerializer):
    permissions = ProfilePermissionSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ("permissions",)
