from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def home(request):
  response = render(request,'home.html')
  response.set_cookie('name','kahim' ,expires=datetime.utcnow()+timedelta(days=2))
  return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})


def del_cookie(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response


def set_session(request):
      data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'Bangla'
     }
      print(request.session.get_session_cookie_age())
      print(request.session.get_expiry_date())
      request.session.update(data)
      return render(request, 'home.html')
      
# def get_session(request):
#     name = request.session.get('name')
#     return render(request,'get_session.html' ,{'name' : name})


def del_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del_session.html')

# set_session ফাংশনে 'name' নামে একটি সেশন সেট করা হয়েছে যার ভ্যালু রাখা হয়েছে 'karim' 


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified = True
        return render(request,'get_session.html' ,{'name' : name})
    else:
        return HttpResponse("Your session has been expired.Login again")