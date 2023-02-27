from django.shortcuts import render
from doctor.models import doctor, Doctorrequest, Nurse
from .models import personalInfo
from .forms import personalInfoForm


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def PatientForm(request):
    form = personalInfoForm()
    if request.method == 'POST':
        form = personalInfoForm(request.POST)
    return render(request, 'PatientForm.html', {'form': form})


def PatientList(request):
    per = personalInfoForm.objects.all()
    return render(request, 'AllPatient.html', {'per': per})

def PatientHome(request,pk):
    pInfo = personalInfo.objects.get(pk=pk)
    return render(request, 'PatientHome.html', {'per': pInfo})
def sendRequest(request, pk):
    if request.method == "POST":
        department = request.method.get('department')
        pInfo = personalInfo.objects.get(pk=pk)

        r = Doctorrequest(Nurse=request.user, patient=pInfo, department=department)
        r.save()
