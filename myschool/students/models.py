from django.db import models

# Create your models here.


class Student(models.Model):
  rollnumber = models.IntegerField()
  name = models.CharField(max_length=255)
  BloodGroup=models.CharField(max_length=255)
  Class=models.IntegerField()