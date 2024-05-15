from django.db import models


class Otp(models.Model):
    email = models.CharField(max_length=50)
    otp = models.CharField(max_length=50)
