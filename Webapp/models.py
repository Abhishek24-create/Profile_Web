from django.contrib.auth.models import User
from django.db import models

class register(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=8)


class BuilD_Profile(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="img/%y", default="img")
    DOB = models.DateField(null=True,blank=True)

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption