from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=150, null=True)
    is_tem = models.BooleanField('is tem', default=False)
    is_tro = models.BooleanField('is tro', default=False)
    institute_name = models.CharField(max_length=150, null=True)

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_date = models.DateField(null=True)
    task = models.CharField(max_length=150)
    machine = models.CharField(max_length=150)
    location = models.CharField(max_length=150)