from django.urls import path
from . import views
urlpatterns = [ 
    # path('', views.home),
    # path('get/',views.get_cookie),
    # path('del/',views.del_cookie),
     path('',views.set_session),
    path('get/',views.get_session),
    path('del/',views.del_session),
]