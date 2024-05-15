from django.db import models


class Student(models.Model):
    email = models.CharField(max_length=20)
    otp = models.CharField(max_length=20)
    
