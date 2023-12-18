from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidationProject
# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST.get('exampleInputname')
        email = request.POST.get('exampleInputEmail1')
        return render(request, 'home.html', {'name': name, 'email': email})
    else:
        return render(request, 'home.html')


def form(request):
    if request.method == 'POST':
        name = request.POST.get('exampleInputname')
        email = request.POST.get('exampleInputEmail1')
        select = request.POST.get('select')
        return render(request, 'form.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'form.html')


def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./apps_3/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form': form})


def studentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, 'django_form.html', {'form': form})
    else:
        form = StudentData()
    return render(request, 'django_form.html', {'form': form})


def PasswordValidation(request):
    if request.method == 'POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, 'django_form.html', {'form': form})
