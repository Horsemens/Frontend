from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('getdata/', views.getdata),
    path('getsensorstatus/', views.getsensorstatus),
]