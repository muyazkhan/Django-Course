from django import forms
from .models import profile


class Profile(forms.ModelForm):
  class Meta:
    model = profile
    fields = '__all__'
    # fields = ['name', 'email']
    # exclude = ['bio']