from django.shortcuts import render
from .models import Doctorrequest, doctor


# Create your views here.
def acceptrequest(request, pk):
    doc = doctor.objects.get(username=request.user)
    d = Doctorrequest.objects.get(pk=pk)
    d.accepted = True
    d.doctor = doc
    d.save()
