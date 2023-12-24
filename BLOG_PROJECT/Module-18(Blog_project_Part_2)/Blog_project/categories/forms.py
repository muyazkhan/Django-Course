from django import forms
from .models import category


class add_category(forms.ModelForm):
  class Meta:
    model = category
    fields = '__all__'
    # fields = ['name', 'email']
    # exclude = ['bio']