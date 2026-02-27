from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import accounts


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts
        fields = ["email", "password", "full_name", "role"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return accounts.objects.create(**validated_data)


class accountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts
        fields = ["id", "email", "full_name", "role", "is_active", "created_at"]