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
# Meta ----------------------------------------------------
class TableData(models.Model):
    TableName = models.AutoField(primary_key=True)
    TableDescription = models.CharField(max_length=256)
    RowCount = models.IntegerField()
    ImportDataDatetime = models.DateTimeField()

    def __str__(self):
        return self.tablename


class TableError(models.Model):
    TableName = models.AutoField(primary_key=True)
    TableDescription = models.CharField(max_length=256)
    Error = models.CharField(max_length=256)
    ErrorDescription = models.CharField(max_length=256)
    ErrorDataDatetime = models.DateTimeField()

    def __str__(self):
        return self.tablename


# Personal Details -------------------------
class PersonalDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PatientTitle = models.CharField(max_length=256)
    PatientFirstName = models.CharField(max_length=256)
    PatientLastName = models.CharField(max_length=256)
    DateOfBirth = models.DateTimeField()
    Gender = models.CharField(max_length=256)
    Weight = models.CharField(max_length=256)
    Height = models.CharField(max_length=256)
    Address = models.CharField(max_length=256)
    BMI = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)
    DNR = models.NullBooleanField
    WardLocation = models.CharField(max_length=256)
    Photo = models.ImageField(default='default.png', upload_to='profile_pics')
    Notes = models.ImageField(default='default.png', upload_to='note_pics')

    def __str__(self):
        return self.patientfirstname

class GuardianDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    GuardianTitle = models.CharField(max_length=256)
    GuardianFirstName = models.CharField(max_length=256)
    GuardianLastName = models.CharField(max_length=256)
    PatientRelations = models.DateTimeField()
    Address = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)

    def __str__(self):
        return self.id

class DoctorDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    DoctorID = models.AutoField(primary_key=True)
    DoctorTitle = models.CharField(max_length=256)
    DoctorFirstName = models.CharField(max_length=256)
    DoctorLastName = models.CharField(max_length=256)
    Specialty = models.CharField(max_length=256)
    WardLocation = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)

    def __str__(self):
        return self.doctorid

class SocialDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    CurrentOccupation = models.CharField(max_length=256)
    Smoking = models.CharField(max_length=256)
    Drinking = models.CharField(max_length=256)
    SexualOrientation = models.CharField(max_length=256)
    SocialDrugUse = models.CharField(max_length=256)
    Handicaps = models.CharField(max_length=256)
    CurrentlySexuallyActive = models.CharField(max_length=256)

    def __str__(self):
        return self.doctorid

class FamilyHistory(models.Model):
    PatientID = models.AutoField(primary_key=True)
    HeartDisease = models.CharField(max_length=256)
    Diabetes = models.CharField(max_length=256)
    CoroneyArteryDisease = models.CharField(max_length=256)
    HighBloodPressure = models.CharField(max_length=256)
    Eczma = models.CharField(max_length=256)
    Asthma = models.CharField(max_length=256)

    def __str__(self):
        return self.doctorid

class DiagnosisHistory(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PreviousDiagnosis = models.CharField(max_length=256)
    DiagnosedDateTime = models.DateTimeField()
    Treatment= models.CharField(max_length=256)
    TreatmentDateTime = models.DateTimeField()
    Result = models.CharField(max_length=256)

    def __str__(self):
        return self.doctorid


# Medication Information Allergies -------------------------
class AllergyDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    AllergyType = models.CharField(max_length=256)
    AllergyAgent = models.CharField(max_length=256)
    AllergyReaction = models.CharField(max_length=256)
    ReactionSeverity = models.CharField(max_length=256)
    AllergyInfoSource = models.CharField(max_length=256)
    AllergyStatus = models.CharField(max_length=256)
    AllergyRecordDatetime = models.DateTimeField()

    def __str__(self):
        return self.allergytype


# Medication Information Medications -------------------------
class MedicationTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    MedicationName = models.CharField(max_length=256)
    MedStartDatetime = models.DateTimeField()
    MedEndDatetime = models.DateTimeField()
    MedicationDuration = models.IntegerField()
    MedicationQuantity = models.CharField(max_length=256)
    MedicationSchedule = models.CharField(max_length=256)

    def __str__(self):
        return self.medicationname

class InjectionTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    InjectionName = models.CharField(max_length=256)
    InjectionDatetime = models.DateTimeField()
    InjectionReason = models.CharField(max_length=256)
    InjectionDose = models.CharField(max_length=256)
    InjectionPriority = models.CharField(max_length=256)

    def __str__(self):
        return self.injectionname

class ImmunisationTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    VaccineName = models.CharField(max_length=256)
    VaccineDatetime = models.DateTimeField()
    VaccineDose = models.CharField(max_length=256)
    VaccineReason = models.CharField(max_length=256)
    ImmunisationPriority = models.IntegerField()

    def __str__(self):
        return self.vaccinename

class NationalEarlyWarningScore(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PersonalDetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    RespirationRate = models.CharField(max_length=256)
    OxygenSaturation = models.CharField(max_length=256)
    SystolicBloodPressure = models.CharField(max_length=256)
    LevelOfConsciousnessNewConfusion = models.CharField(max_length=256)
    Temperature = models.CharField(max_length=256)

    def __str__(self):
        return self.vaccinename