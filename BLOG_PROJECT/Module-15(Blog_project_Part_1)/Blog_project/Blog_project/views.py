from django.shortcuts import render
from posts.models import post

def home(request):
  data = post.objects.all()
  print (data)
  for i in data :
        print(i.title)
        for j in  i.category.all():
            print(j)
        print()
  return render(request,'home.html',{'data':data})