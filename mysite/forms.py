from django import forms
#
from django.forms import fields, ModelForm

from users.models import PersonalDetails


class DateInput(forms.DateInput):
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
                      'gender', 'occupation', 'weight', 'height', 'address', 'bmi', 'phonenumber', 'email', 'dnr', 'wardlocation',
                      'photo']
        widgets = {
                     'dateofbirth': DateInput(),
                 }
