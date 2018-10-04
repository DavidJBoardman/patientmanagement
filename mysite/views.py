from django.shortcuts import render

# Create your views here.

patients = [
    {
        'name': 'Bob',
        'dob': 'September 30, 1994',
        'prescriptions': 'painkillers'
    },
    {
        'name': 'Ted',
        'dob': 'January 25, 1988',
        'prescriptions': 'None'
    }
]

# Example of creating a view (in the future this should be a template)
def home(request):
    return render(request, 'mysite/home.html', {'title': 'Home'})

# Patient details page
def patient(request):
    context = {
        'title': 'Patient Details',
        'patients': patients
    }
    return render(request, 'mysite/patient.html', context)

