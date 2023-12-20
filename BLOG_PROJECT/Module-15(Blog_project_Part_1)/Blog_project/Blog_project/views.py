from django.shortcuts import render
from posts.models import post

def home(request):
  data = post.objects.all()
  print (data)
  return render(request,'home.html',{'data':data})