from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.serializers import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView

from mysite.forms import AddPatientForm, AddNotesForm, AddGuardianForm, AddSocialDetailsForm, AddFamilyHistoryForm, \
    AddDiagnosisHistoryForm, AddAllergyDetailsForm, AddMedicationForm, AddInjectionForm, AddImmunisationForm, \
    AddNewsForm, DateForm
from users.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.


# Example of creating a view (in the future this should be a template)
@login_required()
def home(request):
    patient_list = PersonalDetails.objects.all()

    query_id = request.GET.get('patient_unique_id')
    query_firstname = request.GET.get('patient_firstname')
    query_surname = request.GET.get('patient_surname')
    form = DateForm(request.GET)

    try:
        users = User.objects.exclude(id=request.user.id)
        patient = AssignedPatient.objects.get(current_user=request.user)
        personal_patients = patient.users.all()
    except AssignedPatient.DoesNotExist:
        personal_patients = None

    if form.is_valid():
        date = form.cleaned_data['date']

        if query_id:
            patient_list = patient_list.filter(patientuniqueid__icontains=query_id)
        if query_firstname:
            patient_list = patient_list.filter(patientfirstname__icontains=query_firstname)
        if query_surname:
            patient_list = patient_list.filter(patientlastname__icontains=query_surname)
        if date:
            patient_list = patient_list.filter(dateofbirth__day=date.day)

    paginator = Paginator(patient_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    patients = paginator.get_page(page)
    context = {
        'patients': patients,
        'personal_list': personal_patients,
        'title': 'Home',
        'form': form
    }
    return render(request, 'mysite/home.html', context)


def change_assigned(request, operation, pk):
    friend = PersonalDetails.objects.get(pk=pk)
    if operation == 'add':
        AssignedPatient.make_patient(request.user, friend)
    elif operation == 'remove':
        AssignedPatient.lose_patient(request.user, friend)
    return redirect('/home')


@login_required()
def search_view(request):
    patient_list = PersonalDetails.objects.all()

    query_id = request.GET.get('patient_id')
    query_firstname = request.GET.get('patient_firstname')
    query_surname = request.GET.get('patient_surname')
    query_dob = request.GET.get('patient_dob')

    if query_id:
        patient_list = patient_list.filter(id=query_id)
    if query_firstname:
        patient_list = patient_list.filter(patientfirstname__icontains=query_firstname)
    if query_surname:
        patient_list = patient_list.filter(patientlastname__icontains=query_surname)
    if query_dob:
        patient_list = patient_list.filter(dateofbirth__in=query_dob)

    paginator = Paginator(patient_list, 2)  # Show 25 contacts per page
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    context = {
        'patients': patients,
        'title': 'Search'
    }

    return render(request, 'mysite/search.html', context)


class Patient(LoginRequiredMixin, DetailView):
    template_name = 'mysite/patient.html'
    context_object_name = 'patient_list'

    # queryset = PersonalDetails.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(PersonalDetails, id=id_)

    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("id")

        context = super(Patient, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        medication = Paginator(Medication.objects.filter(personaldetails_id=id_), 3)
        notesandscans = Paginator(NotesAndScans.objects.filter(personaldetails_id=id_), 3)
        guardian = Paginator(GuardianDetails.objects.filter(personaldetails_id=id_), 3)
        social = Paginator(SocialDetails.objects.filter(personaldetails_id=id_), 3)
        familyhistory = Paginator(FamilyHistory.objects.filter(personaldetails_id=id_), 3)
        diagnosis = Paginator(DiagnosisHistory.objects.filter(personaldetails_id=id_), 3)
        allergies = Paginator(AllergyDetails.objects.filter(personaldetails_id=id_), 3)
        injection = Paginator(Injection.objects.filter(personaldetails_id=id_), 3)
        immunisation = Paginator(Immunisation.objects.filter(personaldetails_id=id_), 3)
        news = Paginator(NationalEarlyWarningScore.objects.filter(personaldetails_id=id_), 3)
        context['notesandscans'] = notesandscans.get_page(page)
        context['guardian'] = guardian.get_page(page)
        context['social'] = social.get_page(page)
        context['familyhistory'] = familyhistory.get_page(page)
        context['diagnosis'] = diagnosis.get_page(page)
        context['allergies'] = allergies.get_page(page)
        context['medication'] = medication.get_page(page)
        context['injection'] = injection.get_page(page)
        context['immunisation'] = immunisation.get_page(page)
        context['news'] = news.get_page(page)
        context['title'] = ('Patient %s' % id_)
        return context


class AddPatientView(LoginRequiredMixin, TemplateView):
    template_name = 'mysite/add_patient.html'

    def get(self, request):
        form = AddPatientForm(request.POST)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddPatientForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        return render(request, self.template_name, {'form': form})


@login_required()
def edit_medication(request, id, medication=None):
    medication = get_object_or_404(Medication, id=medication) if medication else None
    type = 'Edit'
    if medication is None:
        type = 'Add'
    if request.method == 'POST':
        form = AddMedicationForm(request.POST, request.FILES, instance=medication)

        if form.is_valid():
            medications = form.save(commit=False)
            medications.patient = medication
            form.instance.personaldetails_id = id
            medications.save()
            return redirect('patient-list', id=id)
    else:
        form = AddMedicationForm(instance=medication)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Medication', 'type': type})

@login_required()
def edit_notes_view(request, id, note=None):
    note = get_object_or_404(NotesAndScans, id=note) if note else None
    type = 'Edit'
    if note is None:
        type = 'Add'
    if request.method == "POST":
        form = AddNotesForm(request.POST, request.FILES, instance=note)

        if form.is_valid():
            notes = form.save(commit=False)
            notes.patient = note
            form.instance.personaldetails_id = id
            notes.save()
            return redirect('patient-list', id=id)
    else:
        form = AddNotesForm(instance=note)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Note', 'type': type})


@login_required()
def edit_guardian_details_view(request, id, guardian=None):
    guardian = get_object_or_404(GuardianDetails, id=guardian) if guardian else None
    type = 'Edit'
    if guardian is None:
        type = 'Add'
    if request.method == "POST":
        form = AddGuardianForm(request.POST, request.FILES, instance=guardian)
        if form.is_valid():
            guardians = form.save(commit=False)
            guardians.patient = guardian
            form.instance.personaldetails_id = id
            guardians.save()
            return redirect('patient-list', id=id)
    else:
        form = AddGuardianForm(instance=guardian)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Guardian Details', 'type': type})


@login_required()
def edit_social_view(request, id, social=None):
    social = get_object_or_404(SocialDetails, id=social) if social else None
    type = 'Edit'
    if social is None:
        type = 'Add'
    if request.method == "POST":
        form = AddSocialDetailsForm(request.POST, request.FILES, instance=social)
        if form.is_valid():
            socials = form.save(commit=False)
            socials.patient = social
            form.instance.personaldetails_id = id
            socials.save()
            return redirect('patient-list', id=id)
    else:
        form = AddSocialDetailsForm(instance=social)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Social History', 'type': type})


@login_required()
def edit_family_history_view(request, id, family_history=None):
    family_history = get_object_or_404(FamilyHistory, id=family_history) if family_history else None
    type='Edit'
    if family_history is None:
        type = 'Add'
    if request.method == "POST":
        form = AddFamilyHistoryForm(request.POST, request.FILES, instance=family_history)
        if form.is_valid():
            family_historys = form.save(commit=False)
            family_historys.patient = family_history
            form.instance.personaldetails_id = id
            family_historys.save()
            return redirect('patient-list', id=id)
    else:
        form = AddFamilyHistoryForm(instance=family_history)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Allergy', 'type': type})


@login_required()
def edit_diagnosis_view(request, id, diagnosis=None):
    diagnosis = get_object_or_404(DiagnosisHistory, id=diagnosis) if diagnosis else None
    type = 'Edit'
    if diagnosis is None:
        type = 'Add'
    if request.method == "POST":
        form = AddDiagnosisHistoryForm(request.POST, request.FILES, instance=diagnosis)
        if form.is_valid():
            diagnosiss = form.save(commit=False)
            diagnosiss.patient = diagnosis
            form.instance.personaldetails_id = id
            diagnosiss.save()
            return redirect('patient-list', id=id)
    else:
        form = AddDiagnosisHistoryForm(instance=diagnosis)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Diagnosis', 'type': type})


@login_required()
def edit_allergy_view(request, id, allergy=None):
    allergy = get_object_or_404(AllergyDetails, id=allergy) if allergy else None
    type = 'Edit'
    if allergy is None:
        type = 'Add'
    if request.method == "POST":
        form = AddAllergyDetailsForm(request.POST, request.FILES, instance=allergy)
        if form.is_valid():
            allergys = form.save(commit=False)
            allergys.patient = allergy
            form.instance.personaldetails_id = id
            allergys.save()
            return redirect('patient-list', id=id)
    else:
        form = AddAllergyDetailsForm()
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Allergy', 'type': type})


@login_required()
def edit_immunisation_view(request, id, immunisation=None):
    immunisation = get_object_or_404(Immunisation, id=immunisation) if immunisation else None
    type = 'Edit'
    if immunisation is None:
        type = 'Add'
    if request.method == "POST":
        form = AddImmunisationForm(request.POST, request.FILES, instance=immunisation)
        if form.is_valid():
            immunisations = form.save(commit=False)
            immunisations.patient = immunisation
            form.instance.personaldetails_id = id
            immunisations.save()
            return redirect('patient-list', id=id)
    else:
        form = AddImmunisationForm(instance=immunisation)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Immunisation', 'type': type})


@login_required()
def edit_news_view(request, id, news=None):
    news = get_object_or_404(NationalEarlyWarningScore, id=news) if news else None
    type = 'Edit'
    if news is None:
        type = 'Add'
    if request.method == "POST":
        form = AddNewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            newss = form.save(commit=False)
            newss.patient = news
            form.instance.personaldetails_id = id
            newss.save()
            return redirect('patient-list', id=id)
    else:
        form = AddNewsForm(instance=news)
    return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'NEWS', 'type': type})


@login_required()
def edit_profile(request, id):
    patient = get_object_or_404(PersonalDetails, id=id)
    if request.method == 'POST':
        form = AddPatientForm(request.POST, request.FILES, instance=patient)

        if form.is_valid():
            personadetails = form.save(commit=False)
            personadetails.patient = patient
            form.instance.personaldetails_id = id
            personadetails.save()
            return redirect('patient-list', id=id)
    else:
        form = AddPatientForm(instance=patient)

        return render(request, 'mysite/add_patient.html', {'form': form})


@login_required()
def edit_injection(request, id, injection=None):
    injection = get_object_or_404(Injection, id=injection) if injection else None
    type = 'Edit'
    if injection is None:
        type = 'Add'
    if request.method == 'POST':
        form = AddInjectionForm(request.POST, instance=injection)

        if form.is_valid():
            injections = form.save(commit=False)
            injections.patient = injection
            form.instance.personaldetails_id = id
            injections.save()
            return redirect('patient-list', id=id)
    else:
        form = AddInjectionForm(instance=injection)

        return render(request, 'mysite/add_edit_details.html', {'form': form, 'tab': 'Injection', 'type': type})

