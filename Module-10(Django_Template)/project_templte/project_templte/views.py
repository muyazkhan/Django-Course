from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# D:\PHITRON COURSE\Software Development Project\BACK-END\Module-10(Django_Template)\project_templte\templates
def admin(request):
    return HttpResponse("kire ki")

def index(request):
    return render(request,'index.html')
