from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("kire ki obostha")
  return render(request,'apps_2/index.html')
