from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class personalInfo(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=25)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    phonenumber = models.IntegerField(default=0)
    Chronic_disease = models.CharField(max_length=10)
    chief_complaint = models.CharField(max_length=100)
    other_complaint = models.CharField(max_length=100)


class Intial_assessment(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    apperance = models.CharField(max_length=25)
    Working_of_breathing = models.CharField(max_length=25)
    Skin_Circulation = models.CharField(max_length=25)
    Select_Pyschological_state = models.CharField(max_length=25)
    select_Unstatble_status = models.CharField(max_length=25)


class Primary_Assessment(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Airway_Status = models.CharField(max_length=25)


class Final_Physchological_Assessment(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Status = models.CharField(max_length=25)
