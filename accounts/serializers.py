from rest_framework import serializers
from .models import accounts

class accountsSerializer(serializers.Modelserializer):
    class Meta:
        model = accounts
        fields = "__all__"