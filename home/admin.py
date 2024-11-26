from django.contrib import admin
from .models import Department,PatientDetails,Appointments,Doctors

# Register your models here.

admin.site.register(Doctors)
admin.site.register(PatientDetails)
admin.site.register(Appointments)
admin.site.register(Department)