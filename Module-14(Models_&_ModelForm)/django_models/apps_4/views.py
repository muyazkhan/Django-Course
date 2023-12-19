from django.shortcuts import render,redirect
from . import models

# Create your views here.


def home(request):
    student = models.students.objects.all
    return render(request, "home.html", {"student":student})

def delete_student(request, roll):
    std = models.students.objects.get(pk = roll).delete()
    return redirect("homepage")