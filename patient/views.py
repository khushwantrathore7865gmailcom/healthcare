from django.shortcuts import render
from doctor.models import doctor, Doctorrequest, Nurse
from .models import personalInfo


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def PatientForm(request):
    if request.method == 'POST':
        name = request.method.get('name')
    return render(request, 'PatientForm.html')


def sendRequest(request):
    if request.method == "POST":
        phn = request.method.get('phn')
        department = request.method.get('department')
        pInfo = personalInfo.objects.get(phonenumber=phn)

        r = Doctorrequest( Nurse=request.user, patient=pInfo,department=department)
        r.save()
