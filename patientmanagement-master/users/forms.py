from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign up forms go here
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']