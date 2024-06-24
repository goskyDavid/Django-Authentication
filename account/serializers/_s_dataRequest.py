from rest_framework import serializers

from account.models import DataRequest


class DataRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRequest
        fields = "__all__"
