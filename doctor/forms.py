from django.forms import ModelForm
from.models import doctor,Nurse

class  doctorForm(ModelForm):
    class Meta:
        ModelForm= doctor
        fields = ['name','gender','department']

class  NurseForm(ModelForm):
    class Meta:
        ModelForm= Nurse
        fields = ['name','gender','department']

