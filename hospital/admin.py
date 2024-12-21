from django.contrib import admin
from .models import Patient, Doctor, Department, Appointment, MedicalRecord

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'doctor_assigned')
    search_fields = ('first_name', 'last_name', 'email')
    

# Registering models

admin.site.register(Patient, PatientAdmin)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization', 'email')
    search_fields = ('name', 'specialization', 'email')
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_info')
    search_fields = ('name', 'location')
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'status', 'patient', 'doctor')
    list_filter = ('status', 'date')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__name')
    
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at','patient', 'doctor')
    fields =('description','patient' ,'doctor')
    
    