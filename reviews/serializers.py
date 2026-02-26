from rest_framework import serializers
from .models import Reviews

class ReviewSerializer(serializers.Modelserializer):
    class Meta:
        model = Reviews
        fields = "__all__"
        