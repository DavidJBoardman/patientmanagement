from django.db import models
# from django.utils import timezone


# Create your models here.
# A model is a object model of a database table. You create a class which will then be used with the ORM in order to
# handle database requests

# Meta----------------------------------------------------

class TableData(models.Model):
    TableName = models.AutoField(primary_key=True)
    TableDescription = models.CharField(max_length=256)
    RowCount = models.IntegerField()
    ImportDataDateTime = models.DateTimeField()


class TableError(models.Model):
    TableName = models.AutoField(primary_key=True)
    TableDescription = models.CharField(max_length=256)
    Error = models.CharField(max_length=256)
    ErrorDescription = models.CharField(max_length=256)
    ImportDataDateTime = models.DateTimeField()


# MedicationInformationMedications-------------------------
class MedicationTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    MedicationName = models.CharField(max_length=256)
    MedStartDateTime = models.DateTimeField()
    MedEndDateTime = models.DateTimeField()
    MedicationDuration = models.IntegerField()
    MedicationQuantity = models.CharField(max_length=256)
    MedicationSchedule = models.CharField(max_length=256)


class InjectionTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    InjectionName = models.CharField(max_length=256)
    InjectionDateTime = models.DateTimeField()
    InjectionReason = models.CharField(max_length=256)
    InjectionDose = models.CharField(max_length=256)
    InjectionPriority = models.CharField(max_length=256)


class ImmunisationTable(models.Model):
    PatientID = models.AutoField(primary_key=True)
    VaccineName = models.CharField(max_length=256)
    VaccineDateTime = models.DateTimeField()
    VaccineDose = models.CharField(max_length=256)
    VaccineReason = models.CharField(max_length=256)
    ImmunisationPriority = models.IntegerField()


# MedicationInformationAllergies-------------------------
class AllergyDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    AllergyType = models.CharField(max_length=256)
    AllergyAgent = models.CharField(max_length=256)
    AllergyReaction = models.CharField(max_length=256)
    ReactionSeverity = models.CharField(max_length=256)
    AllergyInfoSource = models.CharField(max_length=256)
    AllergyStatus = models.CharField(max_length=256)
    AllergyRecordDateTime = models.DateTimeField()


# PersonalDetails----------------------------------------
class PersonalDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    PatientTitle = models.CharField(max_length=256)
    PatientFirstName = models.CharField(max_length=256)
    PatientLastName = models.CharField(max_length=256)
    PatientPreferredName = models.CharField(max_length=256)
    DateOfBirth = models.DateTimeField()
    Gender = models.CharField(max_length=256)
    Occupation = models.CharField(max_length=256)
    Weight = models.CharField(max_length=256)
    Height = models.CharField(max_length=256)
    Address = models.CharField(max_length=256)
    BMI = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)
    DNR = models.NullBooleanField
    WardLocation = models.CharField(max_length=256)
    Photo = models.CharField(max_length=256)


class GuardianDetails(models.Model):
    PatientID = models.AutoField(primary_key=True)
    GuardianTitle = models.CharField(max_length=256)
    GuardianFirstName = models.CharField(max_length=256)
    GuardianLastName = models.CharField(max_length=256)
    PatientRelation = models.DateTimeField()
    Address = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)


class DoctorDetails(models.Model):
    DoctorID = models.AutoField(primary_key=True)
    DoctorTitle = models.CharField(max_length=256)
    DoctorFirstName = models.CharField(max_length=256)
    DoctorLastName = models.CharField(max_length=256)
    Specialty = models.CharField(max_length=256)
    WardLocation = models.CharField(max_length=256)
    PhoneNumber = models.CharField(max_length=256)
    Email = models.CharField(max_length=256)


def __str__(self):
    return self.patientname
