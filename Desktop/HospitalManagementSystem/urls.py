"""
URL configuration for HospitalManagementSystem project.

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
from django .urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include('hospital.urls')),
    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctor/<int:pk>/', view.DoctorDetailView.as_view(), name='doctor-details'),
    path('patients/',views.PatientsListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailsView.as_view(), name='patient-detail'),
    path('departments/',views.DepartmentListCreateView.as_view(), name= 'department-list-create'),
    path('departments/<int:pk/', views.DepartmentDetailsView.as_view(), name='department-detail'),
    path('appointments/',views.AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/<int:pk>/cancel/',views.AppointmentCancelView.as_view(), name='appointment-cancel'),
    path('bills/', views.BillListCreateView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', views.BillDetailView.as_view(), name='bill-details'),
    path('bills/<int:pk>/pay/', views.BillPaymentView.as_view(), name='bill-payment'),
] 
