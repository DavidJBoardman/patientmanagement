from django.urls import path
from django.conf.urls import url
from django.views.generic import DetailView
from . import views
from users.models import PersonalDetails

urlpatterns = [
    path('', views.home, name ='mysite-home'),
    #path('patient/', views.patient, name ='mysite-patient'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=PersonalDetails,
                                             template_name='mysite/patient.html'))
]
