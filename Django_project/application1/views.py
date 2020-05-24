from django.shortcuts import render
from django.http import HttpResponse
from application1.models import Airports_dep, Airports_arr, Incidents, Incidents_description
from django.db.models import Count, Sum

# Create your views here.

#Pour la page Home
def home(request):
    return render(request, 'application1/home.html')

#Pour la page Data
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

#Pour la page Explore

def Explore(request):
    return render(request, 'application1/explore.html')

def explore_incidents(request):
    return render(request, 'application1/explore_incidents.html',
        {
            'nb_in_tot': Incidents.objects.count(),
            'nb_in_ann': Incidents.objects.values('date').annotate(Count('date')).order_by('date'),
            'nb_in_lethal': Incidents_description.objects.filter(fatalities__gt=0).count(),
            'nb_in_type': Incidents_description.objects.values('inc_type').annotate(Count('inc_type')).order_by('inc_type')
        } )

def deces(request):
    return render(request, 'application1/explore_deces.html',
       {
           'nb_death_y': Incidents.objects.filter(incidents_description__fatalities__gt=0).values('date').annotate(fat=Sum('incidents_description__fatalities')).order_by('date'),
           'coun_m_d': Incidents.objects.filter(incidents_description__fatalities__gt=0).values('incident_country').annotate(sum_death=Sum('incidents_description__fatalities')).order_by('-sum_death')[0:10],
           'comp_m_d': Incidents_description.objects.filter(fatalities__gt=0).values('airline').annotate(sum_death=Sum('fatalities')).order_by('-sum_death')[0:10] 
       } )

def Pays(request):
    return render(request, 'application1/explore_pays.html',
       {
           'nb_airp_pays_1': Airports_dep.objects.values('country').annotate(nb_airp=Count('country')).order_by('-nb_airp')[0:79],
           'nb_airp_pays_2': Airports_dep.objects.values('country').annotate(nb_airp=Count('country')).order_by('-nb_airp')[80:159],
           'nb_airp_pays_3': Airports_dep.objects.values('country').annotate(nb_airp=Count('country')).order_by('-nb_airp')[160:238],
           'nb_pays': Airports_dep.objects.distinct('country').count() 
       } )

def France(request):
    return render(request, 'application1/france.html',
       {
           'nb_airp': Airports_dep.objects.filter(country='France').count(),
           'nb_inc': Incidents.objects.filter(incident_country='  France').count(),
           'nb_inc_mortel': Incidents.objects.filter(incident_country='  France', incidents_description__fatalities__gt=0).count(),
           'nb_death': Incidents.objects.filter(incident_country='  France', incidents_description__fatalities__gt=0).aggregate(nb=Sum('incidents_description__fatalities')),
           'nb_inc_y': Incidents.objects.filter(incident_country='  France').values('date').annotate(Count('date')).order_by('date'),
           'nb_inc_airp': Airports_dep.objects.filter(country='France').values('airport_name').annotate(nb_inc=Count('incidents__airport_dep')).filter(nb_inc__gt=0).order_by('-nb_inc')
       } )

def Chine(request):
    return render(request, 'application1/chine.html',
       {
           'nb_airp': Airports_dep.objects.filter(country='China').count(),
           'nb_inc': Incidents.objects.filter(incident_country='  China').count(),
           'nb_inc_mortel': Incidents.objects.filter(incident_country='  China', incidents_description__fatalities__gt=0).count(),
           'nb_death': Incidents.objects.filter(incident_country='  China', incidents_description__fatalities__gt=0).aggregate(nb=Sum('incidents_description__fatalities')),
           'nb_inc_y': Incidents.objects.filter(incident_country='  China').values('date').annotate(Count('date')).order_by('date'),
           'nb_inc_airp': Airports_dep.objects.filter(country='China').values('airport_name').annotate(nb_inc=Count('incidents__airport_dep')).filter(nb_inc__gt=0).order_by('-nb_inc')

       } )

def Mexique(request):
    return render(request, 'application1/mexique.html',
       {
           'nb_airp': Airports_dep.objects.filter(country='Mexico').count(),
           'nb_inc': Incidents.objects.filter(incident_country='  Mexico').count(),
           'nb_inc_mortel': Incidents.objects.filter(incident_country='  Mexico', incidents_description__fatalities__gt=0).count(),
           'nb_death': Incidents.objects.filter(incident_country='  Mexico', incidents_description__fatalities__gt=0).aggregate(nb=Sum('incidents_description__fatalities')),
           'nb_inc_y': Incidents.objects.filter(incident_country='  Mexico').values('date').annotate(Count('date')).order_by('date'),
           'nb_inc_airp': Airports_dep.objects.filter(country='Mexico').values('airport_name').annotate(nb_inc=Count('incidents__airport_dep')).filter(nb_inc__gt=0).order_by('-nb_inc')

       } )

def Egypte(request):
    return render(request, 'application1/egypte.html',
       {
           'nb_airp': Airports_dep.objects.filter(country='Egypt').count(),
           'nb_inc': Incidents.objects.filter(incident_country='  Egypt').count(),
           'nb_inc_mortel': Incidents.objects.filter(incident_country='  Egypt', incidents_description__fatalities__gt=0).count(),
           'nb_death': Incidents.objects.filter(incident_country='  Egypt', incidents_description__fatalities__gt=0).aggregate(nb=Sum('incidents_description__fatalities')),
           'nb_inc_y': Incidents.objects.filter(incident_country='  Egypt').values('date').annotate(Count('date')).order_by('date'),
           'nb_inc_airp': Airports_dep.objects.filter(country='Egypt').values('airport_name').annotate(nb_inc=Count('incidents__airport_dep')).filter(nb_inc__gt=0).order_by('-nb_inc')

       } )

def Philippines(request):
    return render(request, 'application1/philippines.html',
       {
           'nb_airp': Airports_dep.objects.filter(country='Philippines').count(),
           'nb_inc': Incidents.objects.filter(incident_country='  Philippines').count(),
           'nb_inc_mortel': Incidents.objects.filter(incident_country='  Philippines', incidents_description__fatalities__gt=0).count(),
           'nb_death': Incidents.objects.filter(incident_country='  Philippines', incidents_description__fatalities__gt=0).aggregate(nb=Sum('incidents_description__fatalities')),
           'nb_inc_y': Incidents.objects.filter(incident_country='  Philippines').values('date').annotate(Count('date')).order_by('date'),
           'nb_inc_airp': Airports_dep.objects.filter(country='Philippines').values('airport_name').annotate(nb_inc=Count('incidents__airport_dep')).filter(nb_inc__gt=0).order_by('-nb_inc')

       } )

def compagnies(request):
    return render(request, 'application1/explore_compagnies.html',
       {
           'nb_comp': Incidents_description.objects.order_by('airline').distinct('airline').count(),
           'comp_most_inc': Incidents_description.objects.values('airline').annotate(nb_inc=Count('airline')).order_by('-nb_inc')[0:20],
           'comp_least_inc': Incidents_description.objects.values('airline').annotate(nb_inc=Count('airline')).filter(nb_inc__gt=9).order_by('nb_inc')[0:20] 
        } )


