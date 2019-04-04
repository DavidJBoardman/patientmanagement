import uuid

from django.core.validators import RegexValidator
from django.db.models.signals import pre_save

from mysite.utils import unique_patient_id_generator
from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Prefer not to say', 'Prefer not to say'),
)

SEXUAL_ORIENTATION_CHOICES = (
    ('Hetrosexual', 'Hetrosexual'),
    ('Homosexual', 'Homosexual'),
    ('Bisexual', 'Bisexual'),
    ('Prefer not to say', 'Prefer not to say'),
)

ALLERGY_TYPE_CHOICES = (
    ('Drug', 'Drug'),
    ('Food', 'Food'),
    ('Environmental', 'Environmental'),
    ('Inhalant', 'Inhalant'),
    ('Insect', 'Insect'),
    ('Plant', 'Plant'),
    ('Other', 'Other (Specify)')
)

ALLERGY_AGENT_CHOICES = (
    ('Propensity to adverse reaction (disorder)', 'Propensity to adverse reaction (disorder)'),
    ('Propensity to adverse reaction to drug (disorder)', 'Propensity to adverse reaction to drug (disorder)'),
    ('Propensity to adverse reaction to food (disorder)', 'Propensity to adverse reaction to food (disorder)'),
    ('Allergy to substance (disorder)', 'Allergy to substance (disorder)'),
    ('Drug allergy (disorder)', 'Drug allergy (disorder)'),
    ('Food allergy (disorder)', 'Food allergy (disorder)'),
    ('Drug intolerance (disorder)', 'Drug intolerance (disorder)'),
    ('Food intolerance (disorder)', 'Food intolerance (disorder)')

)

ALLERGY_REACTION_SEVERITY_CHOICES = (
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe')
)

ALLERGY_SOURCE_CHOICES = (
    ('Practice Reported', 'Practice Reported'),
    ('Patient Reported', 'Patient Reported'),
    ('Allergy history', 'Allergy history'),
    ('Transition of care/referral', 'Transition of care/referral')
)

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Resolved', 'Resolved')
)

INJECTION_PRIORITY_CHOICES = (
    ('Routine', 'Routine'),
    ('Urgent', 'Urgent'),
    ('Requested', 'Requested')
)

# TODO: How to store in database correctly without the -'s
VACCINE_DISTRIBUTION_CHOICES = (
    ('Birth', 'Birth'),
    ('1 Months', '1 Months',),
    ('4 Months', '4 Months'),
    ('6 Months', '6 Months'),
    ('12 Months', '12 Months'),
    ('15 Months', '15 Months'),
    ('18 Months', '18 Months'),
    ('19-23 Months', '19-23 Months'),
    ('2-3 Years', '2-3 Years'),
    ('4-6 Years', '4-6 Years'),
    ('7-10 Years', '7-10 Years')
)

# TODO: Ability to add other vaccines.
VACCINE_LIST_CHOICES = (
    ('BCG', 'BCG'),
    ('Hepatitis A', 'Hepatitis A'),
    ('Hepatitis B', 'Hepatitis B'),
    ('Rotavirus', 'Rotavirus'),
    ('Diphtheria-Tetanus-Pertussis', 'Diphtheria-Tetanus-Pertussis'),
    ('Pneumococcal', 'Pneumococcal'),
    ('Poliovirus', 'Poliovirus'),
    ('Influenza', 'Influenza'),
    ('Measles-Mumps-Rubella', 'Measles-Mumps-Rubella'),
    ('Other', 'Other')
)


MED_USES_CHOICES = (
    ('With Food', 'With Food'),
    ('Without Food', 'Without Food'),
    ('NA', 'NA')
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
    patientuniqueid = models.CharField(unique=True, max_length=10, verbose_name='Patient ID')
    patientfirstname = models.CharField(max_length=256, verbose_name='First Name')
    patientlastname = models.CharField(max_length=256, verbose_name='Last Name')
    patientpreferredname = models.CharField(max_length=256, blank=True, verbose_name='Preferred name')
    dateofbirth = models.DateTimeField(verbose_name='DOB')
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES, verbose_name='Gender')
    weight = models.CharField(max_length=256, blank=True, verbose_name='Weight (kg)')
    height = models.CharField(max_length=256, blank=True, verbose_name='Height (cm)')
    address = models.CharField(max_length=256, verbose_name='Address')
    bmi = models.CharField(max_length=256, blank=True, verbose_name='BMI')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. 9 to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.CharField(max_length=256, blank=True, verbose_name='Email')
    dnr = models.NullBooleanField(null=True, blank=True, verbose_name='DNR')
    wardlocation = models.CharField(max_length=256, blank=True, verbose_name='Ward Location')
    photo = models.ImageField(default='default.png', upload_to='profile_pics', blank=True, verbose_name='Photo')
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.patientfirstname


class AssignedPatient(models.Model):
    users = models.ManyToManyField(PersonalDetails)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_patient(cls, current_user, new_patient):
        patient, created = cls.objects.get_or_create(
            current_user=current_user
        )
        patient.users.add(new_patient)

    @classmethod
    def lose_patient(cls, current_user, new_patient):
        patient, created = cls.objects.get_or_create(
            current_user=current_user
        )
        patient.users.remove(new_patient)

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.patientuniqueid:
        instance.patientuniqueid= unique_patient_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=PersonalDetails)


class NotesAndScans(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    note_name = models.CharField(max_length=85, verbose_name='Note Description')
    notes = models.ImageField(upload_to='note_pics', verbose_name='Upload Note')
    date = models.DateField(default=date.today)
    lastmodified = models.DateField(auto_now=True)


class GuardianDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    guardiantitle = models.CharField(max_length=256, blank=True, verbose_name='Title', choices=TITLE_CHOICES)
    guardianfirstname = models.CharField(max_length=256, verbose_name='First Name')
    guardianlastname = models.CharField(max_length=256, verbose_name='Last Name')
    patientrelation = models.CharField(max_length=256, blank=True, verbose_name='Patient Relation')
    address = models.CharField(max_length=256, blank=True, verbose_name='Address')
    contactnumber = models.CharField(max_length=256, blank=True, verbose_name='Contact Number')
    email = models.CharField(max_length=256, blank=True, verbose_name='Email')
    lastmodified = models.DateField(auto_now=True)

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
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.doctorid


class SocialDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=256, blank=True, verbose_name='Occupation')
    smoking = models.CharField(max_length=10, blank=True, verbose_name='Smoker', choices=YES_NO_CHOICES)
    drink = models.CharField(max_length=10, blank=True, verbose_name='Drinker', choices=YES_NO_CHOICES)
    sexualorientation = models.CharField(max_length=17, blank=True, verbose_name='Sexual Orientation', choices=SEXUAL_ORIENTATION_CHOICES)
    socialdruguse = models.CharField(max_length=10, blank=True, verbose_name='Social Drug Use', choices=YES_NO_CHOICES)
    disability = models.CharField(max_length=256, blank=True, verbose_name='disabilities')
    sexuallyactive = models.CharField(max_length=10, blank=True, verbose_name='Sexually Active', choices=YES_NO_CHOICES)
    lastmodified = models.DateField(auto_now=True)

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
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.patientid


class DiagnosisHistory(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    previousdiagnosis = models.CharField(max_length=256, verbose_name='Diagnosis')
    diagnoseddatetime = models.DateTimeField(verbose_name='Diagnosis Date')
    treatment = models.CharField(max_length=256, verbose_name='Treatment administered')
    treatmentdatetime = models.DateTimeField(verbose_name='Treatment Date')
    result = models.CharField(max_length=256)
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.patientid


# TODO: Add other please specifcy feild to allergy_type_choices form
# Medication Information Allergies -------------------------
class AllergyDetails(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    allergytype = models.CharField(max_length=256, blank=True, verbose_name='Allergy type', choices=ALLERGY_TYPE_CHOICES)
    allergyagent = models.CharField(max_length=256, blank=True, verbose_name='Allergy Agent', choices=ALLERGY_AGENT_CHOICES)
    allergyreaction = models.CharField(max_length=256, blank=True, verbose_name='Allergy reaction')
    reactionseverity = models.CharField(max_length=256, blank=True, verbose_name='Reaction severity', choices=ALLERGY_REACTION_SEVERITY_CHOICES)
    allergyinfosource = models.CharField(max_length=256, blank=True, verbose_name='Allergy Info Source', choices=ALLERGY_SOURCE_CHOICES)
    allergystatus = models.CharField(max_length=256, blank=True, verbose_name='Status', choices=STATUS_CHOICES)
    allergyrecorddatetime = models.DateTimeField(default=date.today, verbose_name="Allergy Date Recorded")
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.allergytype


# Medication Information Medications -------------------------
class Medication(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    medicationname = models.CharField(max_length=256, verbose_name='Medication Name')
    medstartdatetime = models.DateTimeField(default=date.today, verbose_name='Medication Start Date')
    medenddatetime = models.DateTimeField(verbose_name='Medication End Date')
    usage = models.CharField(max_length=12, blank=True, verbose_name='Medication Usage', choices=MED_USES_CHOICES)
    quantity = models.CharField(max_length=256, blank=True, verbose_name='Medication dose (mg)')
    schedule = models.CharField(max_length=256, blank=True, verbose_name='Medication Schedule Frequency')
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.medicationname


class Injection(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    injectionname = models.CharField(max_length=256, verbose_name='Injection Name')
    injectiondatetime = models.DateTimeField(default=date.today, verbose_name='Injection Date Administered')
    injectionreason = models.CharField(max_length=256, blank=True, verbose_name='Injection Reason')
    injectiondose = models.CharField(max_length=256, blank=True, verbose_name='Injection Dose (mg)')
    injectionpriority = models.CharField(max_length=256, blank=True, verbose_name='Injection Priority', choices=INJECTION_PRIORITY_CHOICES)
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.injectionname


class Immunisation(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    vaccinename = models.CharField(max_length=256, verbose_name='Vaccine Name', choices=VACCINE_LIST_CHOICES)
    vaccinedatetime = models.DateTimeField(default=date.today, verbose_name='Vaccine date administered')
    vaccinedose = models.CharField(max_length=256, verbose_name='Vaccine dose (mg)')
    vaccinereason = models.CharField(max_length=256, blank=True, verbose_name='Vaccine Reason')
    immunisationpriority = models.CharField(max_length=9, verbose_name='Immunisation priority', choices=INJECTION_PRIORITY_CHOICES)
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.vaccinename


class NationalEarlyWarningScore(models.Model):
    personaldetails = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    date = models.DateTimeField()
    respirationrate = models.CharField(max_length=256, blank=True, verbose_name='Respiration Rate (Breaths per minute)')
    oxygensaturation = models.CharField(max_length=256, blank=True, verbose_name='Oxygen Saturation Levels (%)')
    bloodpressure = models.CharField(max_length=256, blank=True, verbose_name='Blood Pressure')
    heartrate = models.CharField(max_length=256, blank=True, verbose_name='Heart rate')
    temperature = models.CharField(max_length=256, blank=True, verbose_name='Temperature')
    bm = models.CharField(max_length=256, blank=True, verbose_name='Blood Monitoring Glucose (Diabetic)')
    lastmodified = models.DateField(auto_now=True)

    def __str__(self):
        return self.patientid


