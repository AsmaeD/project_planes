# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:55:55 2020

@author: Philippine
"""

import pandas as pd

"""
Récupération des données utiles
"""

airport_col=["Airport_ID","Name","City","Country","IATA","ICAO","Lat","Lon","Altitude","Timezone","DST","Tz","Type","Source"]
airport_data=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat",names=airport_col)



#airlines_col=["Airline_ID","Name","Alias","IATA","ICAO","Callsign","Country","Active"]
#airlines_data=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat",names=airlines_col)

##L'alias de beaucoup de compagnies aériennes se retrouvent dans le colonne "Country". Il faudra changer ça.
##Beaucoup de données manquantes et mal rensiegnées également


routes_col=["Airline_IATA_ICAO","Airline_ID","Source_airport_IATA_ICAO","Source_airport_ID","Destination_airport_IATA_ICAO",
            "Destination_airport_ID","Codeshare","Stops","Equipment"]
routes_data=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat",names=routes_col)


#planes_col=['Name','IATA','ICAO']
#planes_data=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat", names=planes_col)
##print(planes_data)
##Certains noms d'avions me semblent bizzare...
##Voir si les codes IATA et ICAO sont différents de ceux déjà présents dans les autres dataframes (un code IATA_avion, IATA_aeroport, IATA_compagnie ?)
#
#
#countries_col=["Name","iso_code","dafif_code"]
#countries_data=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/countries.dat",names=countries_col)
##print(countries_data)
##Le code dafif est apparement obsolète. On pourra s'en passer dans la suite. Pas beaucoup d'information sur les pays,
##à part leur code iso qui pourra servir de clé étrangère par la suite
#
#
#air_train_boat=pd.read_csv("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports-extended.dat", names=airport_col)
##print(air_train_boat)
##Seuls les types airports et station sont rensignés. Il faudra remplir le type gare_maritime/port.
##Beaucoup de noms de villes manquants. A compléter.