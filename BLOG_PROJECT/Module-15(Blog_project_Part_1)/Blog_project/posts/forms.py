from django import forms
from .models import post


class Post(forms.ModelForm):
  class Meta:
    model = post
    fields = '__all__'
    # fields = ['name', 'email']
    # exclude = ['bio']