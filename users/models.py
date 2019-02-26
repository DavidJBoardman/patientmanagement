from django.db import models
from django.contrib.auth.models import User

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    ('DR', 'Dr.'),
    ('SIR', 'Sir.'),
)

GENDER_CHOICES = (
    ('M', 'M'),
    ('F', 'F'),
    ('O', 'Other'),
)

YES_NO_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

SEXUAL_ORIENTATION_CHOICES = (
    ('S', 'Straight'),
    ('G', 'Gay'),
    ('B', 'Bisexual'),
)

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


# Personal Details-------------------------


class PersonalDetails(models.Model):
    patienttitle = models.CharField(max_length=4, choices=TITLE_CHOICES)
    patientfirstname = models.CharField(max_length=256)
    patientlastname = models.CharField(max_length=256)
    patientpreferredname = models.CharField(max_length=256, blank=True)
    dateofbirth = models.DateTimeField()
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES)
    weight = models.CharField(max_length=256, blank=True)
    height = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256)
    bmi = models.CharField(max_length=256, blank=True)
    phonenumber = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)
    dnr = models.NullBooleanField(null=True, blank=True)
    wardlocation = models.CharField(max_length=256, blank=True)
    photo = models.ImageField(default='default.png', upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.patientfirstname


class NotesAndScans(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=85)
    notes = models.ImageField(upload_to='note_pics')


class GuardianDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    guardiantitle = models.CharField(max_length=256, blank=True, choices=TITLE_CHOICES)
    guardianfirstname = models.CharField(max_length=256)
    guardianlastname = models.CharField(max_length=256)
    patientrelation = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    contactnumber = models.CharField(max_length=256, blank=True)
    email = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.patientid

# Currently unsued
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


class SocialDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=256, blank=True)
    smoking = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    drink = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    sexualorientation = models.CharField(max_length=10, blank=True, choices=SEXUAL_ORIENTATION_CHOICES)
    socialdruguse = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    handicaps = models.CharField(max_length=256, blank=True)
    sexuallyactive = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)

    def __str__(self):
        return self.patientid


class FamilyHistory(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allgergies = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    asthma = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    arthritis = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    glaucoma = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    cancer = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    tuberculosis = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    diabetes = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    hearttrouble = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    highbloodpressure = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    stroke = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    epilepsy = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    substanceabuse = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    depression = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    emotionalproblems = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    suicide = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    kidneytrouble = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)
    thyroiddisease = models.CharField(max_length=10, blank=True, choices=YES_NO_CHOICES)

    def __str__(self):
        return self.patientid


class DiagnosisHistory(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    previousdiagnosis = models.CharField(max_length=256)
    diagnoseddatetime = models.DateTimeField()
    treatment = models.CharField(max_length=256)
    treatmentdatetime = models.DateTimeField()
    result = models.CharField(max_length=256)

    def __str__(self):
        return self.patientid


# Medication Information Allergies -------------------------
class AllergyDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allergytype = models.CharField(max_length=256, blank=True)
    allergyagent = models.CharField(max_length=256, blank=True)
    allergyreaction = models.CharField(max_length=256, blank=True)
    reactionseverity = models.CharField(max_length=256, blank=True)
    allergyinfosource = models.CharField(max_length=256, blank=True)
    allergystatus = models.CharField(max_length=256, blank=True)
    allergyrecorddatetime = models.DateTimeField()

    def __str__(self):
        return self.allergytype


# Medication Information Medications -------------------------
class Medication(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    medicationname = models.CharField(max_length=256)
    medstartdatetime = models.DateTimeField(blank=True)
    medenddatetime = models.DateTimeField(blank=True)
    medicationduration = models.IntegerField(blank=True)
    medicationquantity = models.CharField(max_length=256, blank=True)
    medicationschedule = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.medicationname


class Injection(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    injectionname = models.CharField(max_length=256)
    injectiondatetime = models.DateTimeField()
    injectionreason = models.CharField(max_length=256, blank=True)
    injectiondose = models.CharField(max_length=256, blank=True)
    injectionpriority = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.injectionname


class Immunisation(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    vaccinename = models.CharField(max_length=256)
    vaccinedatetime = models.DateTimeField()
    vaccinedose = models.CharField(max_length=256)
    vaccinereason = models.CharField(max_length=256, blank=True)
    immunisationpriority = models.IntegerField()

    def __str__(self):
        return self.vaccinename


class NationalEarlyWarningScore(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    date = models.DateTimeField()
    respirationrate = models.CharField(max_length=256, blank=True)
    oxygensaturation = models.CharField(max_length=256, blank=True)
    systolicbloodpressure = models.CharField(max_length=256, blank=True)
    levelofconsciousnessnewconfusion = models.CharField(max_length=256, blank=True)
    temperature = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.patientid


