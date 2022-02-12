from django.urls import path
from django.shortcuts import HttpResponse, render
from . import views


urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('add/', views.add, name='add'),
    path('check_data/', views.check_data, name='check_data'),
    path('first_experiment/', views.first_experiment, name='first_experiment'),
    path('second_experiment/', views.second_experiment, name='second_experiment'),
    path('third_experiment/', views.third_experiment, name='third_experiment'),
    path('fourth_experiment/', views.fourth_experiment, name='fourth_experiment'),
    path('fifth_experiment/', views.fifth_experiment, name='fifth_experiment'),
    path('sixth_experiment/', views.sixth_experiment, name='sixth_experiment'),
]