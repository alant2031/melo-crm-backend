from core.models import Sale, SaleHistory
from django.conf import settings
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "username"]


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            "id",
            "client",
            "estimated_value",
            "chance",
            "status",
            "funnel_stage",
            "expected_date",
            "in_charge",
            "notes",
            "created_at",
            "updated_at",
        ]

    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    in_charge = UserSerializer(read_only=True)


class SaleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleHistory
        read_only_fields = "__all__"
