from django.db import models
from accounts.models import accounts

class Category(models.Model):
    category_name = models.CharField(max_length =100)
    slug = models.CharField(max_length = 100 , unique = True)
    created_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    #ENUM
    levels = [("BEGINNER" , "Beginner") , ("INTERMEDIATE" , "Intermediate") , ("ADVANCED" , "Advanced")]


    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    price = models.FloatField()
    level = models.CharField(max_length = 100 , choices = levels , default = "BEGINNER")
    instructor_id = models.ForeignKey(accounts, on_delete =models.CASCADE, related_name = "instructed_courses" ,limit_choices_to = {'role' : "INSTRUCTOR"})
    category_id = models.ForeignKey(Category , on_delete = models.CASCADE, related_name = "course_category")
    is_published = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Module(models.Model):
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    order = models.IntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ["course_id" , "order"],
            name = "unique_course_module_order")]

class Lecture(models.Model):
    module_id = models.ForeignKey(Module , on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    video_url  = models.TextField()
    notes = models.TextField()
    order = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ["module_id" , "order"],
            name = "unique_module_lecure_order"
        )]











