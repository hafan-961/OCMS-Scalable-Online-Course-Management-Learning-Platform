from django.db import models
from accounts.models import accounts
from courses.models import Course

class Review(models.Model):
    student_id = models.ForeignKey(accounts, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField() 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student_id', 'course_id'], 
                name='unique_student_course_review')]

    def __str__(self):
        return f"{self.rating} stars for {self.course_id.title}"

