from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .models import Doctorrequest, doctor,Nurse
from patient.models import personalInfo
from .forms import SignUpForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

class SignUpViewDoctor(View):
    form_class = SignUpForm

    template_name = 'partner_company/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(User.objects.all())
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            emaill = form.cleaned_data['email']
            if User.objects.filter(email=emaill).exists():

                return HttpResponse('User with same email already exists, Please try again with different Username!!')
            else:
                user = form.save(commit=False)
                user.username = user.email
                user.user_name = user.email
                user.is_active = False  # change this to False after testing
                user.save()
                new_candidate = doctor(user=user)  # change is email to False after testing
                new_candidate.save()

                return redirect('user:Login')
                # return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


def index(request):
    return render(request, 'index.html')


def login_Doctor(request):
    if request.user.is_authenticated and request.user.is_company:
        print(request.user)
        return redirect('partner_company:partner_company_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            # print(username)
            # print(password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('partner_company:partner_company_home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'partner_company/login.html', context)
class SignUpViewNurse(View):
    form_class = SignUpForm

    template_name = 'partner_company/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(User.objects.all())
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            emaill = form.cleaned_data['email']
            if User.objects.filter(email=emaill).exists():

                return HttpResponse('User with same email already exists, Please try again with different Username!!')
            else:
                user = form.save(commit=False)
                user.username = user.email
                user.user_name = user.email
                user.is_active = False  # change this to False after testing
                user.is_company = True
                user.save()
                new_candidate = Nurse(user=user)  # change is email to False after testing
                new_candidate.save()

                return redirect('user:Login')
                # return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})




def login_Nurse(request):
    if request.user.is_authenticated and request.user.is_company:
        print(request.user)
        return redirect('partner_company:partner_company_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('pass')
            # print(username)
            # print(password)
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_company:
                login(request, user)
                return redirect('partner_company:partner_company_home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'partner_company/login.html', context)

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

