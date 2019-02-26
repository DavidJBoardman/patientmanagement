from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(TableData)
admin.site.register(TableError)
admin.site.register(PersonalDetails)
admin.site.register(NotesAndScans)
admin.site.register(GuardianDetails)
admin.site.register(DoctorDetails)
admin.site.register(SocialDetails)
admin.site.register(FamilyHistory)
admin.site.register(DiagnosisHistory)
admin.site.register(AllergyDetails)
admin.site.register(Medication)
admin.site.register(Injection)
admin.site.register(Immunisation)