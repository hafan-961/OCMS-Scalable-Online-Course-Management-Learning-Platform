from django.db import models

class accounts(models.Model):

    roles = [("STUDENT" , "Student"),
             ("INSTRUCTOR" , "Instructor"),
             ("ADMIN" , "Admin"),]     #the first is name is used in database and the secodn name is fro frontend

    email = models.CharField(max_length = 1000, unique = True)
    password = models.CharField(max_length = 10000)
    full_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100 , choices = roles , default = "STUDENT")
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    


   

