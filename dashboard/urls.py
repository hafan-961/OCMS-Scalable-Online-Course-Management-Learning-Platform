from django.urls import path
from . import views

urlpatterns = [
    path('api/admin/analytics/', views.admin_analytics, name='admin-analytics'),
    path('api/admin/top-courses/', views.top_courses, name='top-courses'),
]