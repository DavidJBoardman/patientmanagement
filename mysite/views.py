from django.shortcuts import render
from .models import PersonalDetails

# Create your views here.


# Example of creating a view (in the future this should be a template)
def home(request):
    return render(request, 'mysite/home.html', {'title': 'Home'})

# Patient details page
def patient(request):
    context = {
        'patients': PersonalDetails.objects.all()
    }
    return render(request, 'mysite/patient.html', context)

