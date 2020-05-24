from django.contrib import admin
from .models import Airports_dep, Airports_arr, Incidents, Incidents_description

admin.site.register(Airports_dep)
admin.site.register(Airports_arr)
admin.site.register(Incidents)
admin.site.register(Incidents_description)

