from django.db import models
from django.contrib.auth.models import AbstractUser
class school_user(models.Model):
    a1 = models.CharField(max_length=30)
    a2 = models.CharField(max_length=30)
    a3 = models.CharField(max_length=30)
    a4 = models.CharField(max_length=30)
    a5 = models.CharField(max_length=30)
    a6 = models.CharField(max_length=30)
    a7 = models.CharField(max_length=30)
    a8 = models.CharField(max_length=30)
    a9 = models.CharField(max_length=30)
    a10 = models.CharField(max_length=30)
    a11 = models.CharField(max_length=30)
    a12 = models.CharField(max_length=30)

class school_basic(models.Model):
    a1 = models.CharField(max_length=30)
    a2 = models.CharField(max_length=30)
    a3 = models.CharField(max_length=30)
    a4 = models.CharField(max_length=30)
    a5 = models.CharField(max_length=30)
    a6 = models.CharField(max_length=30)
    a7 = models.CharField(max_length=30)
    a8 = models.CharField(max_length=30)
    a9 = models.CharField(max_length=30)
    a10 = models.CharField(max_length=30)
    a11 = models.CharField(max_length=30)
    a12 = models.CharField(max_length=30)

class student_funding(models.Model):
    a1 = models.CharField(max_length=30)
    a2 = models.CharField(max_length=30)
    a3 = models.CharField(max_length=30)
    a4 = models.CharField(max_length=30)
    a5 = models.CharField(max_length=30)
    a6 = models.CharField(max_length=30)
    a7 = models.CharField(max_length=30)
    a8 = models.CharField(max_length=30)
    a9 = models.CharField(max_length=30)
    a10 = models.CharField(max_length=30)
    a11 = models.CharField(max_length=30)
    a12 = models.CharField(max_length=30)

class webs(models.Model):
    id=models.AutoField(primary_key = True)
    category= models.CharField(max_length=30)
    sitename= models.CharField(max_length=30)
    urls= models.CharField(max_length=30)
 
class teacher_examinstion(models.Model):
    a1 = models.CharField(max_length=30)
    a2 = models.CharField(max_length=30)
    a3 = models.CharField(max_length=30)
    a4 = models.CharField(max_length=30)
    a5 = models.CharField(max_length=30)
    a6 = models.CharField(max_length=30)
    a7 = models.CharField(max_length=30)
    a8 = models.CharField(max_length=30)
    a9 = models.CharField(max_length=30)
    a10 = models.CharField(max_length=30)
    a11 = models.CharField(max_length=30)
    a12 = models.CharField(max_length=30)