from django.shortcuts import render
from django.http import HttpResponse
from application1.models import Airports_dep, Airports_arr, Incidents, Incidents_description

# Create your views here.

def home(request):
    return render(request, 'application1/home.html',
        {
            'Aéroport_dep': Airports_dep.objects.all()
        } )


def test(request):
    return render(request, 'application1/test.html')

def airports_dep_data(request):
    return render(request, 'application1/airp_dep.html',
        {
            'Aéroport_dep': Airports_dep.objects.all(),
        } )