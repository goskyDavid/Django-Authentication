from django.contrib.auth.models import Permission

from rest_framework import serializers


class ProfilePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("codename",)
