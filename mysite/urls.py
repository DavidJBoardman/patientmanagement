from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url
from django.views.generic import DetailView
from mysite.views import Patient, AddPatientView
from . import views
from users.models import PersonalDetails

urlpatterns = [
    path('', views.home, name ='mysite-home'),
    path('add_patient', AddPatientView.as_view(), name ='add-patient'),
    path('patient/<int:id>', Patient.as_view(), name="patient_list"),
    path('patient/<int:id>/add_note', views.addnoteview, name='add-note'),
    path('patient/<int:id>/add_guardian', views.addguardianview, name='add-guardian'),
    path('patient/<int:id>/add_social', views.addsocialview, name='add-social'),
    path('patient/<int:id>/add_family_hist', views.addfamilyhistview, name='add-family-hist'),
    path('patient/<int:id>/add_diagnosis_hist', views.adddiagnosishistview, name='add-diag-hist'),
    path('patient/<int:id>/add_allergy', views.addallgergyview, name='add-allergy'),
    path('patient/<int:id>/add_medication', views.addmedicationview, name='add-medication'),
    path('patient/<int:id>/add_injection', views.addInjectionView, name='add-injection'),
    path('patient/<int:id>/add_immunisation', views.addImmunisationView, name='add-immunisation'),
    path('patient/<int:id>/add_news', views.addNewsView, name='add-news'),
    path('patient/<int:id>/edit/', views.edit_profile, name='edit_profile'),
    #path('patient/', views.patient, name ='mysite-patient'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
