from django.db import models
from django.contrib.auth.models import User
from patient.models import personalInfo


# Create your models here.
class doctor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    department = models.CharField(max_length=250)


class Nurse(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    department = models.CharField(max_length=250)


class Doctorrequest(models.Model):
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE,null=True,blank=True)
    Nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(personalInfo, on_delete=models.CASCADE)
    department = models.CharField(max_length=250,default='general')
    accepted = models.BooleanField(default=False)
