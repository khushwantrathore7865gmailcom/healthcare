"""healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from doctor.views import SignUpViewDoctor, SignUpViewNurse, login_Doctor, login_Nurse, dashboard, acceptrequest, \
    patientInfo
from patient.views import Home, PatientList, sendRequest,PatientForm,PatientHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/signin',SignUpViewNurse.as_view),
    path('/login',login_Nurse),
    path('/',Home),
    path('/NewPatient',PatientForm),
    path('PatientList',PatientList),
    path('/sendRequest/<int:pk>',sendRequest),
    path('/PatientHome/<int:pk>',PatientHome),
    path('/doctor/signin',SignUpViewDoctor.as_view),
    path('/doctor/login',login_Doctor),
    path('/doctor',dashboard),
    path('/doctor/accept/<int:pk>',acceptrequest),
    path('/doctor/Patientinfo/<int:pk>',patientInfo),


]
