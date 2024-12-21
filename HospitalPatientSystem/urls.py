"""
URL configuration for HospitalPatientSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hospital import views

def home(request):
    return HttpResponse("Welcome to the HospitalPatientSystem")

router = DefaultRouter()
router. register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'departments', views. DepartmentViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'medical-records', views.MedicalRecordViewSet)
router.register(r'medication', views.MedicationViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/', include(router.urls)),
]
