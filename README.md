# HospitalPatientSystem
PROJECT OVERVIEW
The hospitalPatientSystem is a web-based application designed to manage hospital operations, including the management of patients, doctors,appointments, medicalrecords and departments. The system utilizes Django and Django REST framework to provide a RESTful API for seamless interaction with hospital data.

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




