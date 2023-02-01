from django.forms import ModelForm
from .models import personalInfo, Intial_assessment, Primary_Assessment, Final_Physchological_Assessment


class personalInfoForm(ModelForm):
    class Meta:
        ModelForm = personalInfo
        fields = ['Name', 'Gender', 'weight', 'age', 'phonenumber', 'Chronic_disease', 'chief_complaint',
                  'other_complaint']


class Intial_assessmentForm(ModelForm):
    class Meta:
        ModelForm = Intial_assessment
        fields = ['apperance', 'Working_of_breathing', 'Skin_Circulation', 'Select_Pyschological_state',
                  'select_Unstatble_status']


class Primary_AssessmentForm(ModelForm):
    class Meta:
        ModelForm = Primary_Assessment
        fields = ['Airway_Status']


class Final_Physchological_AssessmentForm(ModelForm):
    class Meta:
        ModelForm = Final_Physchological_Assessment
        fields = ['Status']
