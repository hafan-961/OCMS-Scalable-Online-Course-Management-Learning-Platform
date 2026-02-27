from django.urls import path
from . import views

urlpatterns = [
    path('api/courses/<int:course_id>/reviews/', views.course_reviews, name='course-reviews'),
    path('api/reviews/my/', views.my_reviews, name='my-reviews'),
]