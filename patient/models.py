from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)
y_n = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

no_ab = (
    ('Normal', 'Normal'),
    ('Abnormal', 'Abnormal')
)
breathing = (
    ('Normal', 'Noraml'),
    ('Increased', 'Increased'),
    ('Decreased', 'Decreased'),
    ('Gasping', 'Gasping'),
    ('Apnea', 'Apnea')
)
st_un = (
    ('Stable', 'Statble'),
    ('Unstable', 'Unstable')
)
threat = (
    ('Life Threatening', 'Life Threatening'),
    ('Not Life Threatening', 'Not Life Threatening')
)
skin = (
    ('Normal', 'Normal'),
    ('Abnormal', 'Abnormal'),
    ('Bleeding', 'Bleeding')
)
Breathing = (
    ('Normal', 'Normal'),
    ('Poor', 'Poor'),
    ('Increased', 'Increased'),
    ('Acidiotic', 'Acidiotic')
)
N_P = (
    ('Normal', 'Normal'),
    ('Poor', 'Poor'),

)
entry = (
    ('Normal', 'Normal'),
    ('Poor', 'Poor'),
    ('Differentiated', 'Differentiated'),

)
ausc = (
    ('None', 'None'),
    ('Stridor', 'Stridor'),
    ('Wheeze', 'Wheeze'),
    ('Crackels', 'Crackels')
)

color = (
    ('Normal', 'Normal'),
    ('Pallor', 'Pallor'),
    ('Cyanosis', 'Cyanosis'),
    ('Ashen Grey Skin', 'Ashen Grey Skin')

)
finding =(
    ('Rash', 'Rash'),
    ('Abscess','Abscess'),
    ('Pustules','Pustules'),
    ('Celluitis','Celluitis'),
    ('Purpura', 'Purpura'),
    ('Pstechie','Pstechie'),
    ('Eochymosis','Eochymosis')
)
skin_temp = (

    ('Normal', 'Normal'),
    ('Warm', 'Warm'),
    ('Cool', 'Cool'),
)
RSVP = (
    ('Alert','Alert'),
    ('Verbal Stimuli','Verbal Stimuli'),
    ('Paitful Stimuli','Paitful Stimuli'),
    ('Unresponsive',' Unresponsive')
)
pupil_reaction = (
    ('Normal Reactive','Normal Reactive'),
    ('Slow','Slow'),
    ('Brisk Reaction','Brisk Reaction'),
    ('Non Reactive(fix)','Non Reactive (fix)')
)
pupil_symmetry=(
    ('Symmetric','Symmetric'),
    ('Asymmetric', 'Asymmetric'),
    ('Fix and distaled', 'Fix and distaled')
)
lvl = (
    ('level 1 (Resiution)','level 1 (Resiution)'),
    ('level 2 (Emergent)','level 2 (Emergent)'),
    ('level 3 (Urgent)','level 3 (urgent)'),
    ('level 4 (Less Urgent)','level 4 (Less Urgent)'),
    ('level 5 (Non-Urgent)','level 5(Non-Urgent)')
)
# Create your models here.
class personalInfo(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    phonenumber = models.IntegerField(default=0)
    Chronic_disease = models.CharField(max_length=10, choices=y_n)
    chief_complaint = models.CharField(max_length=100)
    other_complaint = models.CharField(max_length=100)


class Intial_assessment(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    apperance = models.CharField(max_length=25, choices=no_ab)
    Working_of_breathing = models.CharField(max_length=25, choices=breathing)
    Skin_Circulation = models.CharField(max_length=25, choices=skin)
    Select_Pyschological_state = models.CharField(max_length=25, choices=st_un)
    select_Unstatble_status = models.CharField(max_length=25, choices=threat)


class Breath(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Airway_Status = models.CharField(max_length=25)
    Enter_RR = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    Breathing_effort = models.CharField(max_length=25, choices=Breathing)
    Air_Entry = models.CharField(max_length=25, choices=entry)
    Ausciltation = models.CharField(max_length=25, choices=ausc)
    Enter_Spo2_Room = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

class Exposure(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    auxilary_temp = models.DecimalField(max_digits=5,decimal_places=2,default=0.0)
    select_color = models.CharField(max_length=25,choices=color)
    surface_finding = models.CharField(max_length=25, choices=finding)

class Circulation(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Heart_Rate = models.IntegerField(default=0)
    Peripheral_Pulse = models.CharField(max_length=25, choices=N_P)
    Central_Pulse = models.CharField(max_length=25,choices=N_P)
    Enter_CFT_value = models.IntegerField(default=0)
    Skin_Temperature = models.CharField(max_length=25, choices=skin_temp)
    BP_systolic = models.IntegerField(default=0)
    BP_diastolic = models.IntegerField(default=0)
    BP_pulse = models.IntegerField(default=0)

class Disability(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Select_AVPU_Response = models.CharField(max_length=25,choices=RSVP)
    Left_Pupil = models.IntegerField(default=0)
    Right_Pupil = models.IntegerField(default=0)
    Left_Pupil_Reaction = models.CharField(max_length=25, choices=pupil_reaction)
    Right_Pupil_Reaction = models.CharField(max_length=25, choices=pupil_reaction)
    Left_Pupil_Symmetry = models.CharField(max_length=25, choices=pupil_symmetry)
    Right_Pupil_Symmetry = models.CharField(max_length=25, choices=pupil_symmetry)
    Blood_sugar = models.IntegerField(default=0)


class Final_Physchological_Assessment(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    Stable = models.CharField(max_length=25,choices=y_n,blank=True)
    Respiratory_Distress = models.CharField(max_length=25, choices=y_n, blank=True)
    Respiratory_Final = models.CharField(max_length=25, choices=y_n, blank=True)
    Hypotensive_Shock = models.CharField(max_length=25, choices=y_n, blank=True)
    Compensated_Shock = models.CharField(max_length=25, choices=y_n, blank=True)
    Primary_Brain= models.CharField(max_length=25, choices=y_n,blank=True)
    Cardiorespitary_Failure= models.CharField(max_length=25,choices=y_n,blank=True)
    Cardiorespitary_Arrest = models.CharField(max_length=25, choices=y_n,blank=True)

class Triange_Classification(models.Model):
    user = models.ForeignKey(personalInfo, on_delete=models.CASCADE, default="")
    select_classification_level = models.CharField(max_length=100,choices=lvl)


