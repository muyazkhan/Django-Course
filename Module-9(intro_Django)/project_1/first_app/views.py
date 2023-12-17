from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
  return HttpResponse("This is course page")
def home(request):
  return HttpResponse("This is first app home page")
