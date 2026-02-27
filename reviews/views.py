from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

#can view all review or post also  
@api_view(['GET', 'POST'])
def course_reviews(request, course_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(course_id=course_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"detail": "Login required to review"}, status=401)
            
        data = request.data.copy()
        data['student_id'] = request.user.id
        data['course_id'] = course_id
        
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#view the user review 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_reviews(request):
    reviews = Review.objects.filter(student_id=request.user.id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)