from django.shortcuts import render
from django.http import HttpResponse
from application1.models import Airports_dep, Airports_arr, Incidents, Incidents_description

# Create your views here.

def home(request):
    return render(request, 'application1/home.html')

def Data(request):
    return render(request, 'application1/Data.html')

def airports_dep_data(request):
    return render(request, 'application1/airp_dep.html',
        {
            'Aéroport_dep': Airports_dep.objects.all()[0:50],
        } )

def airports_arr_data(request):
    return render(request, 'application1/airp_arr.html',
        {
            'Aéroport_arr': Airports_arr.objects.all()[0:50],
        } )

def incidents(request):
    return render(request, 'application1/incidents.html',
        {
            'Incidents': Incidents.objects.all()[0:50] 
        } )

def incidents_desc(request):
    return render(request, 'application1/incidents_desc.html',
        {
            'Incidents_desc': Incidents_description.objects.all()[0:50] 
        } )