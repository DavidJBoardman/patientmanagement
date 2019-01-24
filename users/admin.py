from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(PersonalDetails)
admin.site.register(TableData)
admin.site.register(TableError)
admin.site.register(MedicationTable)
admin.site.register(InjectionTable)
admin.site.register(ImmunisationTable)
admin.site.register(AllergyDetails)
admin.site.register(GuardianDetails)
admin.site.register(DoctorDetails)
