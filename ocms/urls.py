from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),


    path('',TemplateView.as_view(template_name='index.html'),name='home'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('dashboard/',TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
    path('course-detail/',TemplateView.as_view(template_name='course-detail.html'),name='course_detail'),
    path('instructor/',TemplateView.as_view(template_name='instructor-dashboard.html'),name='instructor_dashboard'),
    path('admin-dashboard/',TemplateView.as_view(template_name='admin-dashboard.html'),name='admin_dashboard'),
    
    
    path('api/auth/',include('accounts.urls')),
    path('api/',include('courses.urls')),
    path('api/',include('enrollments.urls')),
    path('api/',include('reviews.urls')),
    path('api/',include('dashboard.urls')),
]