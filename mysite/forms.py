import requests
from django import forms
#
from django.forms import fields, ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, FileInput

from mysite.widgets import ListTextWidget
from users.models import PersonalDetails, NotesAndScans, GuardianDetails, SocialDetails, FamilyHistory, \
    Diagnosis, AllergyDetails, Medication, Injection, Immunisation, NationalEarlyWarningScore


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
                      'gender', 'weight', 'height', 'address', 'postcode', 'city', 'county', 'country', 'bmi', 'phonenumber', 'email', 'dnr', 'wardlocation',
                      'photo']
        widgets = {
                     'dateofbirth': DateInput(),
                     'photo': FileInput(),
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
        fields = ['eczma', 'asthma', 'cancer', 'diabetes', 'heartdisease', 'highbloodpressure']


class AddDiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['diagnosis', 'symptoms', 'diagnoseddatetime', 'treatment', 'treatmentdatetime', 'result']

        widgets = {
        'diagnoseddatetime': DateInput(),
        'treatmentdatetime': DateInput()
        }

    def __init__(self, *args, **kwargs):
        _diagnosis_list = kwargs.pop('diagnosis_list', None)
        super(AddDiagnosisForm, self).__init__(*args, **kwargs)

        self.fields['symptoms'].widget = ListTextWidget(data_list=_diagnosis_list, name='diagnosis-list')


class AddAllergyDetailsForm(ModelForm):
    class Meta:
        model = AllergyDetails
        fields = ['allergytype', 'allergyagent', 'allergyreaction', 'reactionseverity', 'allergyinfosource', 'allergystatus', 'allergyrecorddatetime']

        widgets = {
            'allergyrecorddatetime': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        _allergy_list = kwargs.pop('allergy_list', None)
        super(AddAllergyDetailsForm, self).__init__(*args, **kwargs)

        self.fields['allergyreaction'].widget = ListTextWidget(data_list=_allergy_list, name='allergy-list')


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
            'medstartdatetime': DateInput(),
            'medenddatetime': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        _medication_list = kwargs.pop('data_list', None)
        _frequency_list = kwargs.pop('freq_list', None)
        super(AddMedicationForm, self).__init__(*args, **kwargs)

        self.fields['medicationname'].widget = ListTextWidget(data_list=_medication_list, name='medication-list')
        self.fields['schedule'].widget = ListTextWidget(data_list=_frequency_list, name='frequency-list')


class AddInjectionForm(ModelForm):
    class Meta:
        model = Injection
        fields = ['injectionname', 'injectiondatetime', 'injectionreason', 'injectiondose', 'injectionpriority']

        widgets = {
            'injectiondatetime': DateInput(),
        }


class AddImmunisationForm(ModelForm):
    class Meta:
        model = Immunisation
        fields = ['vaccinename', 'vaccinedatetime', 'vaccinedose', 'vaccinereason', 'immunisationpriority']

        widgets = {
            'vaccinedatetime': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        _medication_list = kwargs.pop('data_list', None)
        super(AddImmunisationForm, self).__init__(*args, **kwargs)

        self.fields['vaccinename'].widget = ListTextWidget(data_list=_medication_list, name='vaccine-list')


class AddNewsForm(ModelForm):
    class Meta:
        model = NationalEarlyWarningScore
        fields = ['date', 'respirationrate', 'oxygensaturation', 'bloodpressure', 'heartrate', 'temperature']

        widgets = {
            'date': DateInput(),
        }
