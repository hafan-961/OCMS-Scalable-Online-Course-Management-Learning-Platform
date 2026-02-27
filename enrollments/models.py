from django.db import models
from accounts.models import accounts
from courses.models import Course, Lecture

class Enrollment(models.Model):
    STATUS_CHOICES = [("ACTIVE", "Active"), ("COMPLETED", "Completed")]

    student_id = models.ForeignKey(
        accounts, 
        on_delete=models.CASCADE,
        limit_choices_to={"role": "STUDENT"}) # Matches your 'accounts' model choices
    
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student_id", "course_id"],
                name="unique_student_enrollment")]
    
    def __str__(self):
        return f"{self.student_id.email} enrolled in {self.course_id.title}"

class LectureProgress(models.Model):
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="progress")
    lecture_id = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False) 
    completed_at = models.DateTimeField(null=True, blank=True) 
