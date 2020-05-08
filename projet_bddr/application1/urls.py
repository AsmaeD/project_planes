from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='application_homepage'),
    path('test/', views.test, name='application_test'),
    path('airports_dep_data/', views.airports_dep_data, name='application_airports_dep')
]