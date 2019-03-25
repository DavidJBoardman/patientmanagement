from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url
from django.views.generic import DetailView
from mysite.views import Patient, AddPatientView
from . import views
from users.models import PersonalDetails

urlpatterns = [
    path('', views.home, name='mysite-home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_assigned, name='change_assigned'),
    path('add_patient', AddPatientView.as_view(), name='add-patient'),
    path('search', views.search_view, name='search'),
    path('patient/<int:id>', Patient.as_view(), name="patient-list"),
    path('patient/<int:id>/add_note', views.edit_notes_view, name='add-note'),
    path('patient/<int:id>/add_guardian', views.edit_guardian_details_view, name='add-guardian'),
    path('patient/<int:id>/add_social', views.edit_social_view, name='add-social'),
    path('patient/<int:id>/add_family_hist', views.edit_family_history_view, name='add-family-hist'),
    path('patient/<int:id>/add_diagnosis_hist', views.edit_diagnosis_view, name='add-diag-hist'),
    path('patient/<int:id>/add_allergy', views.edit_allergy_view, name='add-allergy'),
    path('patient/<int:id>/add_medication', views.edit_medication, name='add-medication'),
    path('patient/<int:id>/add_injection', views.edit_injection, name='add-injection'),
    path('patient/<int:id>/add_immunisation', views.edit_immunisation_view, name='add-immunisation'),
    path('patient/<int:id>/add_news', views.edit_news_view, name='add-news'),
    path('patient/<int:id>/edit/', views.edit_profile, name='edit-profile'),
    path('patient/<int:id>/edit_medication/<int:medication>', views.edit_medication, name='edit-medication'),
    path('patient/<int:id>/edit_injection/<int:injection>', views.edit_injection, name='edit-injection'),
    path('patient/<int:id>/edit_note/<int:note>', views.edit_notes_view, name='add-note'),
    path('patient/<int:id>/edit_guardian/<int:guardian>', views.edit_guardian_details_view, name='add-guardian'),
    path('patient/<int:id>/edit_social/<int:social>', views.edit_social_view, name='add-social'),
    path('patient/<int:id>/edit_family_history/<int:family_history>', views.edit_family_history_view, name='add-family-hist'),
    path('patient/<int:id>/edit_diagnosis_history/<int:diagnosis>', views.edit_diagnosis_view, name='add-diag-hist'),
    path('patient/<int:id>/edit_allergy/<int:allergy>', views.edit_allergy_view, name='add-allergy'),
    path('patient/<int:id>/edit_immunisation/<int:immunisation>', views.edit_immunisation_view, name='add-immunisation'),
    path('patient/<int:id>/edit_news/<int:news>', views.edit_news_view, name='add-news'),
    #path('patient/', views.patient, name ='mysite-patient'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
