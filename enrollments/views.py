from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment, LectureProgress
from .serializers import EnrollmentSerializer, LectureProgressSerializer
from courses.models import Course

# 1. Enroll in a Course
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_course(request):
    course_id = request.data.get("course_id")
    data = {"student_id": request.user.id, "course_id": course_id}
    
    serializer = EnrollmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#views enrolled courses for student dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_courses(request):
    enrollments = Enrollment.objects.filter(student_id=request.user.id)
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)

#get progress for a specific course
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_progress(request, course_id):
    enrollment = Enrollment.objects.filter(student_id=request.user.id, course_id=course_id).first()
    if not enrollment:
        return Response({"error": "Not enrolled in this course"}, status=404)
    
    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.data)