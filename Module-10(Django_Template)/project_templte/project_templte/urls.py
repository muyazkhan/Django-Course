
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('apps_2/', include('apps_2.urls')),
    path('', views.index),
]
