from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='application_homepage'),
    path('Data/', views.Data, name='application_Data'),
    path('airports_dep_data/', views.airports_dep_data, name='application_airports_dep'),
    path('airports_arr_data/', views.airports_arr_data, name='application_airports_arr'),
    path('Incidents/', views.incidents, name='application_incidents'),
    path('Incidents_desc/', views.incidents_desc, name='application_incidents_desc'),
    path('Explore/', views.Explore, name='application_explore'),
    path('explore_incidents/', views.explore_incidents, name='application_explore_incidents'),
    path('deces/', views.deces, name='application_explore_deces'),
    path('Pays/', views.Pays, name='application_explore_pays'),
    path('France/', views.France, name='application_france'),
    path('Chine/', views.Chine, name='application_chine'),
    path('Mexique/', views.Mexique, name='application_mexique'),
    path('Egypte/', views.Egypte, name='application_egypte'),
    path('Philippines/', views.Philippines, name='application_philippines'),
    path('compagnies/', views.compagnies, name='application_explore_compagnies'),
]