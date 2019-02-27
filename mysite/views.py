from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from mysite.forms import AddPatientForm, AddNotesForm, AddGuardianForm, AddSocialDetailsForm, AddFamilyHistoryForm, \
    AddDiagnosisHistoryForm, AddAllergyDetailsForm, AddMedicationForm, AddInjectionForm, AddImmunisationForm, \
    AddNewsForm
from users.models import *
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
        context['notesandscans'] = NotesAndScans.objects.filter(personaldetails_id=id_)
        context['guardian'] = GuardianDetails.objects.filter(personaldetails_id=id_)
        context['social'] = SocialDetails.objects.filter(personaldetails_id=id_)
        context['familyhistory'] = FamilyHistory.objects.filter(personaldetails_id=id_)
        context['diagnosis'] = DiagnosisHistory.objects.filter(personaldetails_id=id_)
        context['allergies'] = AllergyDetails.objects.filter(personaldetails_id=id_)
        context['medication'] = Medication.objects.filter(personaldetails_id=id_)
        context['injection'] = Injection.objects.filter(personaldetails_id=id_)
        context['immunisation'] = Immunisation.objects.filter(personaldetails_id=id_)
        context['news'] = NationalEarlyWarningScore.objects.filter(personaldetails_id=id_)
        context['title'] = ('Patient %s' % id_)
        return context


class AddPatientView(LoginRequiredMixin, TemplateView):
    template_name = 'mysite/add_patient.html'

    def get(self, request):
        form = AddPatientForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        return render(request, self.template_name, {'form': form})

@login_required()
def addnoteview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddNotesForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddNotesForm()
    return render(request, 'mysite/add_note.html', {'form': form})

@login_required()
def addguardianview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddGuardianForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddGuardianForm()
    return render(request, 'mysite/add_guardian.html', {'form': form})

@login_required()
def addsocialview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddSocialDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddSocialDetailsForm()
    return render(request, 'mysite/add_social.html', {'form': form})

@login_required()
def addfamilyhistview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddFamilyHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddFamilyHistoryForm()
    return render(request, 'mysite/add_family_hist.html', {'form': form})

@login_required()
def adddiagnosishistview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddDiagnosisHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddDiagnosisHistoryForm()
    return render(request, 'mysite/add_diagnosis_hist.html', {'form': form})

@login_required()
def addallgergyview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddAllergyDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddAllergyDetailsForm()
    return render(request, 'mysite/add_allergy.html', {'form': form})

@login_required()
def addmedicationview(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddMedicationForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddMedicationForm()
    return render(request, 'mysite/add_medication.html', {'form': form})

@login_required()
def addInjectionView(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddInjectionForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddInjectionForm()
    return render(request, 'mysite/add_injection.html', {'form': form})

@login_required()
def addImmunisationView(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddImmunisationForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddImmunisationForm()
    return render(request, 'mysite/add_immunisation.html', {'form': form})

@login_required()
def addNewsView(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == "POST":
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = patient
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient_list', id=id)
    else:
        form = AddNewsForm()
    return render(request, 'mysite/add_news.html', {'form': form})

