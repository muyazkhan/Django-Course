from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.add_authors, name="add_author"),
]
