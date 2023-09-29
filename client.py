from suds.client import Client

# Créez un client pour chaque service que vous souhaitez utiliser
client_extraction_infos_metier = Client('http://localhost:8000/?wsdl')
client_verif_solvabilite = Client('http://localhost:8000/?wsdl')
client_evaluation_propriete = Client('http://localhost:8000/?wsdl')
client_decision_approbation = Client('http://localhost:8000/?wsdl')

# Utilisez les fonctions des clients pour appeler les services
result_extraction = client_extraction_infos_metier.service.pretraitement_de_texte("Texte à traiter")
result_verif = client_extraction_infos_metier.service.integration_des_bureaux_de_credit("Demande de crédit")
result_evaluation = client_extraction_infos_metier.service.analyse_des_donnees_du_marche_immobilier("Données du marché")
result_decision = client_extraction_infos_metier.service.analyses_des_risques("Analyse des risques")

# Affichez les résultats
print("Résultat de l'extraction d'infos métier:", result_extraction)
print("Résultat de la vérification de solvabilité:", result_verif)
print("Résultat de l'évaluation de la propriété:", result_evaluation)
print("Résultat de la décision d'approbation:", result_decision)
