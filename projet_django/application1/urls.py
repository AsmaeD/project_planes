from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='application_homepage'),
    path('Data/', views.Data, name='application_Data'),
    path('airports_dep_data/', views.airports_dep_data, name='application_airports_dep'),
    path('airports_arr_data/', views.airports_arr_data, name='application_airports_arr'),
    path('Incidents/', views.incidents, name='application_incidents'),
    path('Incidents_desc/', views.incidents_desc, name='application_incidents_desc')
]