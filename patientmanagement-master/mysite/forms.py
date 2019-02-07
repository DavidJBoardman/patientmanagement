from django import forms

class AddPatient(forms.Form):
    patienttitle = forms.CharField(required=True, max_length=256)
    patientfirstname = forms.CharField(required=True, max_length=256)
    patientlastname = forms.CharField(required=True, max_length=256)
    patientpreferredname = forms.CharField(required=True, max_length=256)
    dateofbirth = forms.DateTimeField(required=True)
    gender = forms.CharField(required=True, max_length=256)
    occupation = forms.CharField(required=True, max_length=256)
    weight = forms.CharField(required=True, max_length=256)
    height = forms.CharField(required=True, max_length=256)
    address = forms.CharField(required=True, max_length=256)
    bmi = forms.CharField(required=True, max_length=256)
    phonenumber = forms.CharField(required=True, max_length=256)
    email = forms.CharField(required=True, max_length=256)
    dnr = forms.CharField(required=True)
    wardlocation = forms.CharField(required=True, max_length=256)
    #photo = forms.ImageField(default='default.png', upload_to='profile_pics')
