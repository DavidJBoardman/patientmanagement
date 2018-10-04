from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='mysite-home'),
    path('patient/', views.patient, name ='mysite-patient'),
]
