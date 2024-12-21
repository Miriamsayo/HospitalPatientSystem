from django.db import models
from datetime import date

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_info = models.CharField(max_length=100)
    address = models.TextField()
    doctor_assigned = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    def available_appointments(self):
        from datetime import date
        return Appointment.objects.filter(doctor=self, date__gte=date.today(), status='pending')
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor, related_name="departments")
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    class Meta:
        constraints =[
            models.UniqueConstraint(
                fields=['date', 'time', 'doctor'],
                name='unique_appointment'
            )
        ]
    
    def __str__(self):
        return f"{self.patient.first_name} -{self.patient.last_name} -{self.date}"
    
    def cancel(self):
        self.status = 'canceled'
        self.save()
    
class MedicalRecord(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Record for {self.patient.first_name}{self.patient.last_name} by{self.doctor.name}"
    
    

    
class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medications")
    prescription_date = models.DateField()
    prescribed_by = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="prescriptions")
    
    def __str__(self):
        return f"{self.name}prescribed to {self.patient.first_name} {self.patient.last_name}"
    
    