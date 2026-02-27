from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from django.views.decorators.cache import cache_page
#importing models from others app
from accounts.models import accounts
from courses.models import Course
from enrollments.models import Enrollment

#admin analytics
#redis TTL 5-15 minutes 
@cache_page(900)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_analytics(request):
    #check if the user is an ADMIN
    if request.user.role != 'ADMIN':
        return Response({"error": "Admin access required"}, status=403)

    data = {
        "total_users": accounts.objects.count(),
        "total_courses": Course.objects.count(),
        "total_enrollments": Enrollment.objects.count(),
    }
    return Response(data)

#enrolled courses
@cache_page(900)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def top_courses(request):
    if request.user.role != 'ADMIN':
        return Response({"error": "Admin access required"}, status=403)

    #aggregates enrollments per course and orders by highest count
    top_list = Enrollment.objects.values('course_id__title').annotate(
        enrollment_count=Count('id')
    ).order_by('-enrollment_count')[:5] #top 5 courses
    return Response(top_list)