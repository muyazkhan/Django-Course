from django.shortcuts import render,redirect
from .import forms
from . import models
# Create your views here.


def add_post(request):
  if request.method == "POST":
        post_form = forms.Post(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
            
  else:
        post_form = forms.Post()
  return render(request, 'post.html',{'poost': post_form})


def edit_post(request,id):
    post = models.post.objects.get(pk=id) 
    post_form = forms.Post(instance=post)
    # print(post.title)
    if request.method == 'POST': # user post request koreche
        post_form = forms.Post(request.POST, instance=post) # user er post request data ekhane capture korlam
        if post_form.is_valid():
            post_form.instance.author = request.user # post kora data gula amra valid kina check kortechi
            post_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('home') # sob thik thakle take add author ei url e pathiye dibo
    return render(request, 'post.html', {'poost' : post_form})

def delete_post(request, id):
    post = models.post.objects.get(pk=id)
    post.delete()
    return redirect('home')