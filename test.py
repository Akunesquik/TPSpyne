from suds.client import Client


# Créez un client pour l'application
client_extraction_infos_metier = Client('http://localhost:8000/service_extraction_infos_metier/?wsdl')


# Utilisez les fonctions du client pour appeler les méthodes du service
result_extraction = client_extraction_infos_metier.service.pretraitement_de_texte("Texte à traiter")




# Affichez le résultat
print("Résultat de l'extraction d'infos métier:", result_extraction)