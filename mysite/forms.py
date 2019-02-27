from django import forms
#
from django.forms import fields, ModelForm

from users.models import PersonalDetails, NotesAndScans, GuardianDetails, SocialDetails, FamilyHistory, \
    DiagnosisHistory, AllergyDetails, Medication, Injection, Immunisation, NationalEarlyWarningScore


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


# class AddPatientForm(forms.ModelForm):
#     patienttitle = forms.CharField(required=True, max_length=256)
#     patientfirstname = forms.CharField(required=True, max_length=256)
#     patientlastname = forms.CharField(required=True, max_length=256)
#     patientpreferredname = forms.CharField(required=True, max_length=256)
#     dateofbirth = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     gender = forms.CharField(required=True, max_length=256)
#     occupation = forms.CharField(required=False, max_length=256)
#     weight = forms.CharField(required=False, max_length=256)
#     height = forms.CharField(required=False, max_length=256)
#     address = forms.CharField(required=True, max_length=256)
#     bmi = forms.CharField(required=False, max_length=256)
#     phonenumber = forms.CharField(required=False, max_length=256)
#     email = forms.CharField(required=False, max_length=256)
#     dnr = forms.CharField(required=False)
#     wardlocation = forms.CharField(required=False, max_length=256)
#     photo = forms.ImageField(required=False)
#
#     class Meta:
#         model = PersonalDetails
#         widgets = {
#             'dateofbirth': DateInput(),
#         }


class AddPatientForm(ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['patienttitle', 'patientfirstname', 'patientlastname', 'patientpreferredname', 'dateofbirth',
                      'gender', 'weight', 'height', 'address', 'bmi', 'phonenumber', 'email', 'dnr', 'wardlocation',
                      'photo']
        widgets = {
                     'dateofbirth': DateInput(),
                 }


class AddNotesForm(ModelForm):
    class Meta:
        model = NotesAndScans
        fields = ['note_name', 'notes']


class AddGuardianForm(ModelForm):
    class Meta:
        model = GuardianDetails
        fields = ['guardiantitle', 'guardianfirstname', 'guardianlastname', 'patientrelation', 'address',
                  'contactnumber', 'email']


class AddSocialDetailsForm(ModelForm):
    class Meta:
        model = SocialDetails
        fields = ['occupation', 'smoking', 'drink', 'sexualorientation', 'socialdruguse',
                  'handicaps', 'sexuallyactive']


class AddFamilyHistoryForm(ModelForm):
    class Meta:
        model = FamilyHistory
        fields = ['allgergies', 'asthma', 'arthritis', 'glaucoma', 'cancer', 'tuberculosis',
                  'diabetes', 'hearttrouble', 'highbloodpressure', 'stroke', 'epilepsy', 'substanceabuse',
                  'depression', 'emotionalproblems', 'suicide', 'kidneytrouble', 'thyroiddisease']


class AddDiagnosisHistoryForm(ModelForm):
    class Meta:
        model = DiagnosisHistory
        fields = ['previousdiagnosis', 'diagnoseddatetime', 'treatment', 'treatmentdatetime', 'result']

        widgets = {
        'diagnoseddatetime': DateTimeInput(),
        }



class AddAllergyDetailsForm(ModelForm):
    class Meta:
        model = AllergyDetails
        fields = ['allergytype', 'allergyagent', 'allergyreaction', 'reactionseverity', 'allergyinfosource', 'allergystatus', 'allergyrecorddatetime']

        widgets = {
            'allergyrecorddatetime': DateTimeInput(),
        }


class AddMedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['medicationname', 'medstartdatetime', 'medenddatetime', 'medicationduration', 'medicationquantity', 'medicationschedule']

        widgets = {
            'medstartdatetime': DateTimeInput(),
            'medenddatetime': DateTimeInput(),
        }


class AddInjectionForm(ModelForm):
    class Meta:
        model = Injection
        fields = ['injectionname', 'injectiondatetime', 'injectionreason', 'injectiondose', 'injectionpriority']

        widgets = {
            'injectiondatetime': DateTimeInput(),
        }


class AddImmunisationForm(ModelForm):
    class Meta:
        model = Immunisation
        fields = ['vaccinename', 'vaccinedatetime', 'vaccinedose', 'vaccinereason', 'immunisationpriority']

        widgets = {
            'vaccinedatetime': DateTimeInput(),
        }


class AddNewsForm(ModelForm):
    class Meta:
        model = NationalEarlyWarningScore
        fields = ['date', 'respirationrate', 'oxygensaturation', 'systolicbloodpressure', 'levelofconsciousnessnewconfusion', 'temperature']

        widgets = {
            'date': DateTimeInput(),
        }
