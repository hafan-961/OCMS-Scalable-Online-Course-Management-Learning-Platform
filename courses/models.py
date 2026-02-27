from django.db import models
from accounts.models import accounts  

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced")
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    instructor_id = models.ForeignKey(
        accounts, 
        on_delete=models.CASCADE, 
        related_name="instructed_courses"
    )
    category_id = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="courses"
    )
    
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_id', 'order'], name='unique_course_module_order')
        ]

class Lecture(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=255)
    video_url = models.TextField()
    notes = models.TextField()
    order = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['module_id', 'order'], name='unique_module_lecture_order')
        ]