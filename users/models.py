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
    patienttitle = models.CharField(max_length=4, choices=TITLE_CHOICES, verbose_name='Title')
    patientfirstname = models.CharField(max_length=256, verbose_name='First Name')
    patientlastname = models.CharField(max_length=256, verbose_name='Last Name')
    patientpreferredname = models.CharField(max_length=256, blank=True, verbose_name='Preferred name')
    dateofbirth = models.DateTimeField(verbose_name='DOB')
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES, verbose_name='Gender')
    weight = models.CharField(max_length=256, blank=True, verbose_name='Weight')
    height = models.CharField(max_length=256, blank=True, verbose_name='Height')
    address = models.CharField(max_length=256, verbose_name='Address')
    bmi = models.CharField(max_length=256, blank=True, verbose_name='BMI')
    phonenumber = models.CharField(max_length=256, blank=True, verbose_name='Phone Number')
    email = models.CharField(max_length=256, blank=True, verbose_name='Email')
    dnr = models.NullBooleanField(null=True, blank=True, verbose_name='DNR')
    wardlocation = models.CharField(max_length=256, blank=True, verbose_name='Ward Location')
    photo = models.ImageField(default='default.png', upload_to='profile_pics', blank=True, verbose_name='Photo')

    def __str__(self):
        return self.patientfirstname


class NotesAndScans(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=85, verbose_name='Note Description')
    notes = models.ImageField(upload_to='note_pics', verbose_name='Upload Note')


class GuardianDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    guardiantitle = models.CharField(max_length=256, blank=True, verbose_name='Title', choices=TITLE_CHOICES)
    guardianfirstname = models.CharField(max_length=256, verbose_name='First Name')
    guardianlastname = models.CharField(max_length=256, verbose_name='Last Name')
    patientrelation = models.CharField(max_length=256, blank=True, verbose_name='Patient Relation')
    address = models.CharField(max_length=256, blank=True, verbose_name='Address')
    contactnumber = models.CharField(max_length=256, blank=True, verbose_name='Contact Number')
    email = models.CharField(max_length=256, blank=True, verbose_name='Email')

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
    occupation = models.CharField(max_length=256, blank=True, verbose_name='Occupation')
    smoking = models.CharField(max_length=10, blank=True, verbose_name='Smoker', choices=YES_NO_CHOICES)
    drink = models.CharField(max_length=10, blank=True, verbose_name='Drinker', choices=YES_NO_CHOICES)
    sexualorientation = models.CharField(max_length=10, blank=True, verbose_name='Sexual Orientation', choices=SEXUAL_ORIENTATION_CHOICES)
    socialdruguse = models.CharField(max_length=10, blank=True, verbose_name='Social Drug Use', choices=YES_NO_CHOICES)
    handicaps = models.CharField(max_length=256, blank=True, verbose_name='Handicaps')
    sexuallyactive = models.CharField(max_length=10, blank=True, verbose_name='Sexually Active', choices=YES_NO_CHOICES)

    def __str__(self):
        return self.patientid


class FamilyHistory(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allgergies = models.CharField(max_length=10, blank=True, verbose_name='Allergies', choices=YES_NO_CHOICES)
    asthma = models.CharField(max_length=10, blank=True, verbose_name='Asthma', choices=YES_NO_CHOICES)
    arthritis = models.CharField(max_length=10, blank=True, verbose_name='Arthritis', choices=YES_NO_CHOICES)
    glaucoma = models.CharField(max_length=10, blank=True, verbose_name='Glaucoma', choices=YES_NO_CHOICES)
    cancer = models.CharField(max_length=10, blank=True, verbose_name='Cancer', choices=YES_NO_CHOICES)
    tuberculosis = models.CharField(max_length=10, blank=True, verbose_name='Tuberculosis', choices=YES_NO_CHOICES)
    diabetes = models.CharField(max_length=10, blank=True, verbose_name='Diabetes', choices=YES_NO_CHOICES)
    hearttrouble = models.CharField(max_length=10, blank=True, verbose_name='Heart Trouble', choices=YES_NO_CHOICES)
    highbloodpressure = models.CharField(max_length=10, blank=True, verbose_name='High Blood Pressure', choices=YES_NO_CHOICES)
    stroke = models.CharField(max_length=10, blank=True, verbose_name='Stroke', choices=YES_NO_CHOICES)
    epilepsy = models.CharField(max_length=10, blank=True, verbose_name='Epilepsy', choices=YES_NO_CHOICES)
    substanceabuse = models.CharField(max_length=10, blank=True, verbose_name='Substance Abuse', choices=YES_NO_CHOICES)
    depression = models.CharField(max_length=10, blank=True, verbose_name='Depression', choices=YES_NO_CHOICES)
    emotionalproblems = models.CharField(max_length=10, blank=True, verbose_name='Emotional Problems', choices=YES_NO_CHOICES)
    suicide = models.CharField(max_length=10, blank=True, verbose_name='Suicide', choices=YES_NO_CHOICES)
    kidneytrouble = models.CharField(max_length=10, blank=True, verbose_name='Kidney Trouble', choices=YES_NO_CHOICES)
    thyroiddisease = models.CharField(max_length=10, blank=True, verbose_name='Thyroid Disease', choices=YES_NO_CHOICES)

    def __str__(self):
        return self.patientid


class DiagnosisHistory(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    previousdiagnosis = models.CharField(max_length=256, verbose_name='Previous Diagnosis')
    diagnoseddatetime = models.DateTimeField(verbose_name='Diagnosis Date')
    treatment = models.CharField(max_length=256, verbose_name='Treatment administered')
    treatmentdatetime = models.DateTimeField(verbose_name='Treatment Date')
    result = models.CharField(max_length=256)

    def __str__(self):
        return self.patientid


# Medication Information Allergies -------------------------
class AllergyDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allergytype = models.CharField(max_length=256, blank=True, verbose_name='Allergy type')
    allergyagent = models.CharField(max_length=256, blank=True, verbose_name='Allergy Agent')
    allergyreaction = models.CharField(max_length=256, blank=True, verbose_name='Allergy reaction')
    reactionseverity = models.CharField(max_length=256, blank=True, verbose_name='Reaction severity')
    allergyinfosource = models.CharField(max_length=256, blank=True, verbose_name='Allergy Info Source')
    allergystatus = models.CharField(max_length=256, blank=True, verbose_name='Status')
    allergyrecorddatetime = models.DateTimeField()

    def __str__(self):
        return self.allergytype


# Medication Information Medications -------------------------
class Medication(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    medicationname = models.CharField(max_length=256, verbose_name='Medication Name')
    medstartdatetime = models.DateTimeField(blank=True, verbose_name='Medication Start Date')
    medenddatetime = models.DateTimeField(blank=True, verbose_name='Medication End Date')
    medicationduration = models.IntegerField(blank=True, verbose_name='Medication Duration')
    medicationquantity = models.CharField(max_length=256, blank=True, verbose_name='Medication Quantity')
    medicationschedule = models.CharField(max_length=256, blank=True, verbose_name='Medication Schedule')

    def __str__(self):
        return self.medicationname


class Injection(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    injectionname = models.CharField(max_length=256, verbose_name='Injection Name')
    injectiondatetime = models.DateTimeField(verbose_name='Injection Date Administered')
    injectionreason = models.CharField(max_length=256, blank=True, verbose_name='Injection Reason')
    injectiondose = models.CharField(max_length=256, blank=True, verbose_name='Injection Dose')
    injectionpriority = models.CharField(max_length=256, blank=True, verbose_name='Injection Priority')

    def __str__(self):
        return self.injectionname


class Immunisation(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    vaccinename = models.CharField(max_length=256, verbose_name='Vaccine Name')
    vaccinedatetime = models.DateTimeField(verbose_name='Vaccine date administered')
    vaccinedose = models.CharField(max_length=256, verbose_name='Vaccine dose')
    vaccinereason = models.CharField(max_length=256, blank=True, verbose_name='Vaccine Reason')
    immunisationpriority = models.IntegerField(verbose_name='Immunisation priority')

    def __str__(self):
        return self.vaccinename


class NationalEarlyWarningScore(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    date = models.DateTimeField()
    respirationrate = models.CharField(max_length=256, blank=True, verbose_name='Respiration Rate')
    oxygensaturation = models.CharField(max_length=256, blank=True, verbose_name='Oxygen Saturation')
    systolicbloodpressure = models.CharField(max_length=256, blank=True, verbose_name='Systolic Blood Pressure')
    levelofconsciousnessnewconfusion = models.CharField(max_length=256, blank=True, verbose_name='Level of Consciousness')
    temperature = models.CharField(max_length=256, blank=True, verbose_name='Temperature')

    def __str__(self):
        return self.patientid


