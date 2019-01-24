from django.shortcuts import render
#from .models import PersonalDetails
from users.models import PersonalDetails
from django.contrib.auth.decorators import login_required
# Create your views here.


# Example of creating a view (in the future this should be a template)
@login_required()
def home(request):
    context = {
        'patients': PersonalDetails.objects.all(),
        'title': 'Home'
    }
    return render(request, 'mysite/home.html', context)

# # Patient details page
# @login_required()
# def patient(request):
#     context = {
#         'patients': PersonalDetails.objects.all(),
#         'title': 'Patient Details'
#     }
#     return render(request, 'mysite/patient.html', context)

