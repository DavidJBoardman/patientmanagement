from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from users.models import *
from django.contrib.auth.decorators import login_required
from mysite.forms import AddPatient
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
# #@login_required()
# class PatientView(ListView):
#     context_object_name = 'patient_list'
#     template_name = 'mysite/patient.html'
#     title = 'Patient Details'
#     queryset = PersonalDetails.objects.all()
#
#     def get_context_data(self, **kwargs):
#          context = super(PatientView, self).get_context_data(**kwargs)
#          context['patientdetails'] = self.queryset
#          context['medication'] = MedicationTable.objects.all()
#          context['injection'] = InjectionTable.objects.all()
#          context['immunisation'] = ImmunisationTable.objects.all()
#          context['allergies'] = AllergyDetails.objects.all()
#          context['guardian'] = GuardianDetails.objects.all()
#
#          return context

# # Patient details page


class Patient(LoginRequiredMixin, DetailView):
    template_name = 'mysite/patient.html'
    context_object_name = 'patient_list'
    #queryset = PersonalDetails.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PersonalDetails, id=id_)

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("id")

        context = super(Patient, self).get_context_data(**kwargs)
        context['medication'] = MedicationTable.objects.filter(personaldetails_id=id_)
        context['injection'] = InjectionTable.objects.filter(personaldetails_id=id_)
        context['immunisation'] = ImmunisationTable.objects.filter(personaldetails_id=id_)
        context['allergies'] = AllergyDetails.objects.filter(personaldetails_id=id_)
        context['guardian'] = GuardianDetails.objects.filter(personaldetails_id=id_)
        context['title'] = ('Patient %s' % id_)
        return context


class AddPatientView(TemplateView):
    template_name = 'mysite/add_patient.html'

    def get(self, request):
        form = AddPatient()
        return render(request, self.template_name, {'form': form})
