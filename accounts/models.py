from django.db import models

class accounts(models.Model):

    roles = [("STUDENT" , "Student"),
             ("INSTRUCTOR" , "Instructor"),
             ("ADMIN" , "Admin"),]     #the first is name is used in database and the secodn name is fro frontend

    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 128)
    full_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 20 , choices = roles , default = "STUDENT")
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email

   

