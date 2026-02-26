from django.db import models
from accounts.models import accounts
from courses.models import Course
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Reviews(models.Model):
    student_id = models.ForeignKey(accounts , on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course , on_delete = models.CASCADE)
    rating  = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ["student_id" , "course_id"],
            name = "unique_accounts_reviews_course_id"
        )]




