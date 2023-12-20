from django.shortcuts import render, redirect
from .import forms

# Create your views here.


def add_authors(request):
    if request.method == "POST":
        author_form = forms.Author(request.POST)
        if author_form.is_valid():
            author_form.save()
            
    else:
        author_form = forms.Author()
    return render(request, 'author.html', {'author': author_form})



      
    
