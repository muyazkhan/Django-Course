from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# class Author(forms.ModelForm):
#   class Meta:
#     model = author
#     fields = '__all__'
    # fields = ['name', 'email']
    # exclude = ['bio']

class registation_forms(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'requierd'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'requierd'}))
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class change_forms(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']