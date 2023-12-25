from django import forms
from .models import post,Comment


class Post(forms.ModelForm):
  class Meta:
    model = post
    # fields = '__all__'
    # fields = ['name', 'email']
    exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        