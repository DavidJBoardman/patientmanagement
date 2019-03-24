from django import forms
#
from django.forms import fields, ModelForm

from users.models import PersonalDetails, NotesAndScans, GuardianDetails, SocialDetails, FamilyHistory, \
    DiagnosisHistory, AllergyDetails, Medication, Injection, Immunisation, NationalEarlyWarningScore


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%Y-%m-%d'], widget=DateInput(
        attrs={
            'class': 'form-control mb-2 mr-sm-2',
            'name': "patient_surname",
            'id': "search-dob",
            'placeholder': 'DOB'
        }
    ), required=False, )

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
                  'disability', 'sexuallyactive']


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
        'treatmentdatetime': DateTimeInput(),
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
        fields = ['medicationname',
                  'medstartdatetime',
                  'medenddatetime',
                  'usage',
                  'quantity',
                  'schedule']

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
        fields = ['date', 'respirationrate', 'oxygensaturation', 'bloodpressure', 'heartrate', 'temperature']

        widgets = {
            'date': DateTimeInput(),
        }
