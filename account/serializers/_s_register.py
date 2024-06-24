from rest_framework import serializers
from account.models import User
from services.exceptions import BadRequest


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if User.objects.filter(email=attrs.get("email")).exists():
            raise BadRequest("El usuario con el mismo correo electrónico ya existe.")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
