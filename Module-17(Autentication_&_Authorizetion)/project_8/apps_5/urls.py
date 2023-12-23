from django.urls import path
from .import views
urlpatterns = [
    path('', views.singup, name="singup_page"), 
    path('home/', views.home, name="homepage"), 
    path('profile/', views.profile, name="profilepage"), 
    path('login/', views.user_login, name="loginpage"), 
    path('logout/', views.user_logout, name="logoutpage"), 
    path('pass_change/', views.pass_change, name="passchange"), 
    path('pass_change2/', views.pass_change2, name="passchange2"), 
    # path('change_user_data/', views.change_user_data, name="change_user_data"), 
]
