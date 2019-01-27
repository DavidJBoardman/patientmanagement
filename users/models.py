from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone

# Create your models here.
# A model is a object model of a database table. You create a class which will then be used with the ORM in order to


class Profile(models.Model):
    # if the user is deleted then delete the profile too but not the other way around
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


# handle database requests
# Meta----------------------------------------------------


class TableData(models.Model):
    tablename = models.AutoField(primary_key=True)
    tabledescription = models.CharField(max_length=256)
    rowcount = models.IntegerField()
    importdatadatetime = models.DateTimeField()

    def __str__(self):
        return self.tablename


class TableError(models.Model):
    tablename = models.AutoField(primary_key=True)
    tabledescription = models.CharField(max_length=256)
    error = models.CharField(max_length=256)
    errordescription = models.CharField(max_length=256)
    importdatadatetime = models.DateTimeField()

    def __str__(self):
        return self.tablename


# MedicationInformationMedications-------------------------


class PersonalDetails(models.Model):
    patienttitle = models.CharField(max_length=256)
    patientfirstname = models.CharField(max_length=256)
    patientlastname = models.CharField(max_length=256)
    patientpreferredname = models.CharField(max_length=256)
    dateofbirth = models.DateTimeField()
    gender = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    weight = models.CharField(max_length=256)
    height = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    bmi = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    dnr = models.NullBooleanField
    wardlocation = models.CharField(max_length=256)
    photo = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.patientfirstname


class InjectionTable(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    injectionname = models.CharField(max_length=256)
    injectiondatetime = models.DateTimeField()
    injectionreason = models.CharField(max_length=256)
    injectiondose = models.CharField(max_length=256)
    injectionpriority = models.CharField(max_length=256)

    def __str__(self):
        return self.injectionname


class ImmunisationTable(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    vaccinename = models.CharField(max_length=256)
    vaccinedatetime = models.DateTimeField()
    vaccinedose = models.CharField(max_length=256)
    vaccinereason = models.CharField(max_length=256)
    immunisationpriority = models.IntegerField()

    def __str__(self):
        return self.vaccinename


# MedicationInformationAllergies-------------------------
class AllergyDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allergytype = models.CharField(max_length=256)
    allergyagent = models.CharField(max_length=256)
    allergyreaction = models.CharField(max_length=256)
    reactionseverity = models.CharField(max_length=256)
    allergyinfosource = models.CharField(max_length=256)
    allergystatus = models.CharField(max_length=256)
    allergyrecorddatetime = models.DateTimeField()

    def __str__(self):
        return self.allergytype


class MedicationTable(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    medicationname = models.CharField(max_length=256)
    medstartdatetime = models.DateTimeField()
    medenddatetime = models.DateTimeField()
    medicationduration = models.IntegerField()
    medicationquantity = models.CharField(max_length=256)
    medicationschedule = models.CharField(max_length=256)

    def __str__(self):
        return self.medicationname


class GuardianDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    guardiantitle = models.CharField(max_length=256)
    guardianfirstname = models.CharField(max_length=256)
    guardianlastname = models.CharField(max_length=256)
    patientrelation = models.DateTimeField()
    address = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.id


class DoctorDetails(models.Model):
    doctorid = models.AutoField(primary_key=True)
    doctortitle = models.CharField(max_length=256)
    doctorfirstname = models.CharField(max_length=256)
    doctorlastname = models.CharField(max_length=256)
    specialty = models.CharField(max_length=256)
    wardlocation = models.CharField(max_length=256)
    phonenumber = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.doctorid

