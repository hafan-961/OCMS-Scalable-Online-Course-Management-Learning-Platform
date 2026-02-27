# from django.urls import path
# from . import views
# from rest_framework_simplejwt.views import TokenRefreshView

# urlpatterns = [
#     path('api/auth/register/', views.register, name='register'),
#     path('api/auth/login/', views.login, name='login'),
#     path('api/auth/profile/', views.profile, name='profile'),
#     path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/auth/logout/', views.logout, name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # We removed 'api/auth/' from here because it's already in the main urls.py
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]