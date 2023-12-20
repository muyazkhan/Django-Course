from django import forms
from .models import author


class Author(forms.ModelForm):
  class Meta:
    model = author
    fields = '__all__'
    # fields = ['name', 'email']
    # exclude = ['bio']