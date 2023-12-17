from django.http import HttpResponse

def home(request):
  return HttpResponse("Ho vai home page")
def Contact(request):
  return HttpResponse("Ho vai eida contact page")