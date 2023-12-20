from django.shortcuts import render
from .import forms
# Create your views here.
def add_profile(request):
  if request.method == "POST":
        Profile_form = forms.Profile(request.POST)
        if Profile_form.is_valid():
            Profile_form.save()
            
  else:
        Profile_form = forms.Profile()
  return render(request, 'profile.html',{'profile': Profile_form})