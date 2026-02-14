from django.contrib import admin
from .models import StaffProfile, Patient, TriageRequest

admin.site.register(StaffProfile)
admin.site.register(Patient)
admin.site.register(TriageRequest)
