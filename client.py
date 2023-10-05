from suds.client import Client

# Créez un client pour chaque service que vous souhaitez utiliser
client_extraction_infos_metier = Client('http://localhost:8000/?wsdl')
client_verif_solvabilite = Client('http://localhost:8000/?wsdl')
client_evaluation_propriete = Client('http://localhost:8000/?wsdl')
client_decision_approbation = Client('http://localhost:8000/?wsdl')

# Utilisez les fonctions des clients pour appeler les services
result_extraction = client_extraction_infos_metier.service.pretraitement_de_texte("Nom du Client : bobby bob \n Adresse : 13 rue des lilas \n Email : bob@gmail.com \n Numéro de Téléphone : 06 43 38 11 44 \n Montant du prêt demandé : 211 111 eur \n Durée du pret : 12 ans \n Description de la Propriété  : bien entretenue \n Revenu Mensuel : 5111 EUR \n Depenses mensuelles  : 3111 EUR")
result_verif = client_extraction_infos_metier.service.integration_des_bureaux_de_credit(result_extraction)
#result_evaluation = client_extraction_infos_metier.service.analyse_des_donnees_du_marche_immobilier("Données du marché")
#result_decision = client_extraction_infos_metier.service.analyses_des_risques("Analyse des risques")

# Affichez les résultats
print("Résultat de l'extraction d'infos métier:", result_extraction)
print("test")
print("Résultat de la vérification de solvabilité:", result_verif)
#print("Résultat de l'évaluation de la propriété:", result_evaluation)
#print("Résultat de la décision d'approbation:", result_decision)
