from django.forms import ModelForm
from .models import personalInfo, Intial_assessment, Breath, Exposure, Circulation, Disability, \
    Final_Physchological_Assessment, Triange_Classification


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


class BreathForm(ModelForm):
    class Meta:
        ModelForm = Breath
        fields = ['Airway_Status', 'Enter_RR', 'Breathing_effort', 'Air_Entry', 'Ausciltation', 'Enter_Spo2_Room']


class ExposureForm(ModelForm):
    class Meta:
        ModelForm = Exposure
        fields = ['auxilary_temp', 'select_color', 'surface_finding']


class CirculationForm(ModelForm):
    class Meta:
        ModelForm = Circulation
        fields = ['Heart_Rate', 'Peripheral_Pulse', 'Central_Pulse', 'Enter_CFT_value', 'Skin_Temperature',
                  'BP_systolic', 'BP_diastolic', 'BP_pulse']


class DisabilityForm(ModelForm):
    class Meta:
        ModelForm = Disability
        fields = ['Select_AVPU_Response', 'Left_Pupil', 'Right_Pupil', 'Left_Pupil_Reaction', 'Right_Pupil_Reaction',
                  'Left_Pupil_Symmetry', 'Right_Pupil_Symmetry', 'Blood_sugar']


class Final_Physchological_AssessmentForm(ModelForm):
    class Meta:
        ModelForm = Final_Physchological_Assessment
        fields = ['Stable', 'Respiratory_Distress', 'Respiratory_Final', 'Hypotensive_Shock', 'Compensated_Shock',
                  'Primary_Brain', 'Cardiorespitary_Failure', 'Cardiorespitary_Arrest']


class TriangeForm(ModelForm):
    class Meta:
        ModelForm = Triange_Classification
        fields = ['select_classification_level']
