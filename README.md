# Description 

Voici le dépôt git de notre projet semestriel en base de données relationnelles. Le but de ce projet est de réaliser une application web permettant à tout internaute de naviguer dans les données pertinentes par rapport au sujet d’étude choisi,
de les exploiter : les interroger, les croiser, les trier, les filtrer, les visualiser, etc.
Les données mises à disposition sont disponibles aux URL suivantes :

https://www.data.gouv.fr/en/datasets/donnees-despace-aerien-de-la-base-aeronautique-du-sia/

https://openflights.org/data.html

https://aviation-safety.net/database/

https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx

https://www.transtats.bts.gov/databases.asp?Mode_ID=1&Mode_Desc=Aviation&Subject_ID2=0


Le travail à réaliser consiste en : 

1) concevoir une base de données multi-tables sous formes normales

2) peupler la base de données avec au moins (sans être restrictif) les données pertinentes par rapport au sujet d’étude retenu, définir les relations entres les tables

3) concevoir l’application web


Les contraintes imposées sont les suivantes:

1) utiliser le SGBD postgreSQL

2) utiliser le framework Django

3) consigner en temps réel le travail réalisé sous github

# Contributors
Main project contributors : RENAUDIN Philippine, DADI Asmae, BENNETEAU Pierre

# Subject

Nous allons essayer de réaliser une application permettant aux internautes de naviguer parmis des informations statistiques sur l'aviation (accidents, fréquentation des aéropoprts, etc..) mais aussi tout simplement des informations relatives aux aéroports, gares ferroviares ou gares maritimes.
Nous aimerions aussi si possible afficher des graphiques statistiques ou des cartes de transport (chemin le plus court, etc...)

# Etat de réalisation du projet:

Récupération des données pertinentes achevée
Création du répertoire de projet avec Django
Remplissage de la base de données effectué
Application web réalisée

# Description des fichiers du dépôt:

	script_get_data.py : fichier python permettant de récupérer les données utiles et de les mettre sous forme de dataframe pour une manipulation simplifiée.

	script_cleaning_data.py : fichier python permettant de nettoyer les données récupérées (suppression ou remplissage des valeurs manquantes)

	data_scrapping_script.py, data_srapping_script_complemental.py : fichiers python permettant de récupérer des données par web scrapping.

	global_html_to_csv.py : fichier python permmetant de générer un fichier csv de toutes les données récupérées avec les 2 scripts précédents.

	script_remplissage_'name' : script python (django) de remplissage des tables ('name') de la base de données
	
	Django_project : répertoire du projet Django complet

# Etat de la récupération des données, du nettoyage et de leur mise en forme:

Toutes les données récupérables (soucis matériel et de temps) récupérées, nettoyées

# Etat de la base de données réalisée:

Créée, tables créées, migrées, base remplie

# Programmes réalisés et les fonctionnalités opérationnelles:
	scripts de récupération des données
	scripts de nettoyage des données
	scripts de remplissage de la base de données
