from django.db import models
from django.utils import timezone
# Create your models here.
# A model is a object model of a database table. You create a class which will then be used with the ORM in order to handle database requests


class PersonalDetails(models.Model):
    patientid = models.AutoField(primary_key=True)
    patientname = models.CharField(max_length=256)
    dateofbirth = models.DateTimeField()
    gender = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    photo = models.CharField(max_length=256)

    def __str__(self):
        return self.patientname