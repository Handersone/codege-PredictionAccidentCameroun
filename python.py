# capteur de vitesse 
import random
import time

class CapteurVitesse:
    def __init__(self, emplacement):
        self.emplacement = emplacement

    def lire_vitesse(self):
        # Simuler la lecture de la vitesse en km/h
        return random.randint(20, 120)

# Utilisation du capteur
capteur = CapteurVitesse("Route A")
vitesse_actuelle = capteur.lire_vitesse()
print(f"Vitesse actuelle sur {capteur.emplacement}: {vitesse_actuelle} km/h")

# transmission des données vers le centre de traitement 
import requests

class TransmetteurDonnees:
    def __init__(self, url_centre_traitement):
        self.url_centre_traitement = url_centre_traitement

    def transmettre_donnees(self, donnees):
        # Envoyer les données au centre de traitement
        response = requests.post(self.url_centre_traitement, json=donnees)
        return response.status_code

# Utilisation du transmetteur
transmetteur = TransmetteurDonnees("http://centre-traitement/api/reception-donnees")
donnees = {"emplacement": "Route A", "vitesse": vitesse_actuelle}
statut_transmission = transmetteur.transmettre_donnees(donnees)
print(f"Statut de la transmission : {statut_transmission}")

#  stockage des données dans une base MongoDB 
from pymongo import MongoClient

class StockageDonnees:
    def __init__(self, url_base_mongodb):
        self.client = MongoClient(url_base_mongodb)
        self.db = self.client["trafic_db"]
        self.collection = self.db["donnees_trafic"]

    def stocker_donnees(self, donnees):
        # Stocker les données dans la base MongoDB
        self.collection.insert_one(donnees)

# Utilisation du stockage
stockage = StockageDonnees("mongodb://localhost:27017/")
stockage.stocker_donnees(donnees)

#  modèle de prédiction de trafic 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Chargement des données (
donnees_historiques = ...

# Préparation des données
X_train, X_test, y_train, y_test = train_test_split(donnees_historiques.drop("trafic", axis=1), donnees_historiques["trafic"], test_size=0.2)

# Entraînement du modèle
modele = RandomForestRegressor()
modele.fit(X_train, y_train)

# Prédiction du trafic
trafic_predit = modele.predict(X_test)
erreur_moyenne = mean_squared_error(y_test, trafic_predit)
print(f"Erreur moyenne de prédiction : {erreur_moyenne}")

# Ajustement des feux de signalisation 
class GestionFeuxSignalisation:
    def ajuster_feux_signalisation(self, intensite_trafic):
        # Ajuster la durée des feux en fonction de l'intensité du trafic
        nouvelle_duree_vert = min(intensite_trafic // 10, 60)
        return nouvelle_duree_vert

# Utilisation de l'ajustement des feux
gestion_feux = GestionFeuxSignalisation()
duree_vert_ajustee = gestion_feux.ajuster_feux_signalisation(intensite_trafic_actuelle)
print(f"Nouvelle durée de feu vert : {duree_vert_ajustee} secondes")


