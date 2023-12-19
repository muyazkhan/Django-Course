from django.urls import path
# from . import views
from apps_5.views import home
urlpatterns = [
    path('', home, name='homepage'),
    # path('show/', showData, name='showData'),
]