from django.urls import path
from . import views

urlpatterns = [
    path('api/enroll/', views.enroll_course, name='enroll-course'),
    path('api/my-courses/', views.my_courses, name='my-courses'),
    path('api/course/<int:course_id>/progress/', views.course_progress, name='course-progress'),
]