from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import doctor, Nurse
from django.contrib.auth.models import User
from django import forms


class doctorForm(ModelForm):
    class Meta:
        ModelForm = doctor
        fields = ['name', 'gender', 'department']


class NurseForm(ModelForm):
    class Meta:
        ModelForm = Nurse
        fields = ['name', 'gender', 'department']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name', 'class': "input100"}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name', 'class': "input100"}))
    email = forms.EmailField(max_length=254,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter email address', 'class': "input100"}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password ', 'class': "input100"}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'confirm Password ', 'class': "input100"}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
