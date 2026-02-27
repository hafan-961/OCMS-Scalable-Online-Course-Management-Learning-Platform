from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('courses/', views.course_list_public, name='course-list'),
    path('courses/create/', views.course_create, name='course-create'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),
    path('instructor/courses/', views.instructor_courses, name='instructor-courses'),

    path('api/courses/<int:course_id>/modules/', views.module_list_create),
    
    path('api/modules/<int:module_id>/lectures/', views.lecture_list_create),
    
    path('api/lectures/<int:pk>/', views.lecture_detail),
]