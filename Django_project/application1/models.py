from django.db import models

class Airports_dep(models.Model):
    IACO = models.CharField(primary_key=True, max_length=4,unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.CharField(max_length = 30)
    lon = models.CharField(max_length = 30)

class Airports_arr(models.Model):
    IACO = models.CharField(primary_key=True, max_length=4,unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.CharField(max_length = 30)
    lon = models.CharField(max_length = 30)

class Incidents(models.Model):
    date = models.CharField(max_length = 4)
    location = models.CharField(max_length = 100)
    incident_country = models.CharField(max_length = 100)
    plane_type = models.CharField(max_length = 100)
    airport_dep = models.ForeignKey(Airports_dep, on_delete=models.CASCADE)#revoir si cascade justifiée
    airport_arr = models.ForeignKey(Airports_arr, on_delete=models.CASCADE)#idem 


class Incidents_description(models.Model):
    id_incidents = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    #description = models.CharField(max_length=1000)
    inc_type = models.CharField(max_length = 5)
    fatalities = models.IntegerField()
    airline = models.CharField(max_length = 100)