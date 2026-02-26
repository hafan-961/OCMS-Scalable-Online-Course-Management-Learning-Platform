from django.db import models
from accounts.models import accounts
from courses.models import Course , Lecture
class Enrollment(models.Model):
    status_bar = [("ACTIVE" , "active") , ("COMPLETED" , "completed")]

    student_id = models.ForeignKey(accounts , on_delete = models.CASCADE,
     limit_choices_to = {"role" : "STUDENTS"} )
    course_id = models.ForeignKey(Course , on_delete = models.CASCADE )
    status = models.CharField(max_length = 100 , choices = status_bar , default = "ACTIVE" )
    enrolled_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields = ["student_id" , "course_id"],
            name = "unique_accounts_enrollment_course_id"
        )]

class LectureProgress(models.Model):
    enrollment_id = models.ForeignKey(Enrollment , on_delete = models.CASCADE)
    lecture_id = models.ForeignKey(Lecture , on_delete = models.CASCADE)
    compeleted = models.BooleanField(default = False)
    completed_at = models.DateTimeField(auto_now_add = True)



