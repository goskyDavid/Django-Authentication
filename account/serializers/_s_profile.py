from rest_framework import serializers
from account.models import User

from ._s_permissionGroup import ProfilePermissionGroupSerializer


class ProfileSerializer(serializers.ModelSerializer):
    groups = ProfilePermissionGroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        exclude = (
            "updated_at",
            "user_permissions",
            "is_active",
            "is_staff",
            "last_login",
            "deleted",
            "deleted_at",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
        }

    def update(self, instance: User, validated_data: dict):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        super().update(instance, validated_data)
        return instance
