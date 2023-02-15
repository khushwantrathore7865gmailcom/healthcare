from django.shortcuts import render, redirect
from .models import Doctorrequest, doctor
from patient.models import personalInfo


# Create your views here.
def dashboard(request):
    user = request.user
    d = doctor.objects.get(username=user)
    doc = Doctorrequest.objects.filter(department=d.department, accepted=False)
    return render(request, 'doctor_Dashboard.html', {'req': doc})


def acceptrequest(request, pk):
    doc = doctor.objects.get(username=request.user)
    d = Doctorrequest.objects.get(pk=pk)
    d.accepted = True
    d.doctor = doc
    d.save()
    return redirect()


def patientInfo(request, pk):
    pers = personalInfo.objects.get(pk=pk)
    return render(request, 'patientInfo.html', {'per': pers})

