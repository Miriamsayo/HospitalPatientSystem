# HospitalPatientSystem
PROJECT OVERVIEW

The hospitalPatientSystem is a web-based application designed to manage hospital operations, including managing patients, doctors, appointments, medicalrecords, and departments. The system utilizes Django and Django REST framework to provide  RESTful API for seamless interaction with hospital data.

GROUP MEMBERS ID

97017
151892
107119
150349

PROJECT STRUCTUREHospitalPatientSystem/

├── HospitalPatientSystem/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── hospital/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
├── manage.py
└── db.sqlite3

MODELS AND THEIR RELATIONSHIP

 PATIENT
name(CharField)
age(IntegerField)
contact_info(CharField)
address(TextField)
email(EmailField)

DOCTOR
name(CharField)
Specialization(CharField)
contact_number(CharField)
email(EmailField)

DEPARTMENT
name(CharField)
location(CharField)
contact_info(CharField)

APPOINTMENT
STATUS_CHOICES(pending,completed,canceled)
date(DateField)
time(TimeField)
status(CharField)
patient(foreignKey)
doctor(foreignkey)

VIEWS/VIEWSet

PatientViewSet
Handles CRUD operations for patients
URL:/api/patients/

DoctorViewSet
Handles CRUD operations for doctors
URL:/api/doctors/

AppointmentViewSet
Handle CRUD operations for appointments
URL:/api/appointments/

MedicalRecordViewSet

Handle CRUD operations for medicalrecords
URL:/api/medicalrecords/

DepartmentViewSet

Handle CRUD operations for the Department
URL:/api/department/


Serializers and Validation Rules

PatientSerializer
Fields serialized: name, age, contact_number

Validation:
age must be a positive Integer
contact_number must follow a valid phone number format

DoctorSerializer
Fields Serialized: name, specialization, contact_number

Validation
specialization cannot be empty.

AppointmentSerializer
Fields Serialized: patient, doctor, appointment_date, status

Validation:
appointment_date must not be in the past

Testing
The model was tested and is able to create a new patient, doctors can retrieve records, appointments are scheduled and the status is either Pending, canceled, or completed, or departments can be added.






