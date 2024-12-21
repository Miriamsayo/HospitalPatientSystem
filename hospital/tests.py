
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Patient

# Create your tests here.
class PatientAPITestCase(APITestCase):
    def setUp(self):
        self.patient_data = {
            "first_name": "John",
            "last_name": "Doe",
            "contact_info": "123456789",
            "address": "123 Street Name",
            "email": "john@gmail.com"
        }
        self.patient = Patient.objects.create(**self.patient_data)
        
    def test_create_patient(self):
        response = self.client.post('/api/patients', self.patient_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'],self.patient_data['first_name'])
        self.assertEqual(response.data['last_name'],self.patient_data['last_name'])

    def test_get_patient(self):
        response = self.client.get(f'/api/patients/{self.patient.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.patient.first_name)
        self.assertEqual(response.data['last_name'], self.patient.last_name)
        
        
