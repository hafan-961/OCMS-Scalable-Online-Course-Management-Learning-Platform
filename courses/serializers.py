from rest_framework import serializers
from .models import Category , Course , Module , Lecture

class CategorySerializer(serializers.Modelserilaizer):
    class Meta:
        model = Category
        fields = "__all__"

class CourseSerializer(serializers.Modelserializer):
    class Meta:
        model = Course
        fields = "__all__"

class ModuleSerializer(serializer.Modelserializer):
    class Meta:
        model = Module
        fileds = "__all__"

class LectureSerializer(serializers.Modelserializer):
    class Meta:
        model = Lecture
        fields = "__all__"