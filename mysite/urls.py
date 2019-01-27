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
    #path('patient/', views.patient, name ='mysite-patient'),
    path('<int:id>', Patient.as_view(), name="patient_list"),
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=PersonalDetails,
    #                                         template_name='mysite/patient.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
