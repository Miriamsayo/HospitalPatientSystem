from rest_framework import serializers
from .models import Patient, Doctor, Appointment, Medication, Department, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
        def validate(self, data):
            if data['date'] < date.today():
                raise serializers.ValidationError("Appointment date cannot be in the past.")
            return data

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        
class MedicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medication
        fields = '__all__'
    