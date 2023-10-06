from suds.client import Client
import sys 


filename = sys.argv[1]

# Lire le contenu du fichier
with open(filename, 'r') as file:
    contenu_fichier = file.read()

#Client permet d'acceder a l'URL afin d'appeler les fonctions des services
#On les appelle de la forme suivante :
# Client.service.nomDeLaFonction(args...)


C1 = Client('http://localhost:8000/InfoMetier?wsdl')
print("\nExtraction des informations en cours\nentrée : fichier : " + filename)
valueC1 = C1.service.Extraction_information(contenu_fichier)
print("sortie : tableau de 4 string comportant les infos necessaires pour l'evaluation du credit" )
print("\nIntegration_des_bureaux_de_credit en cours\nentrée : str : " + valueC1[0])
valueC3_1=C1.service.integration_des_bureaux_de_credit(valueC1[0])#nouveau déplacé
print("sortie : " + valueC3_1)

C2 = Client('http://localhost:8000/SWC?wsdl')
print("\nConnexion au Service Web Composite \nentrées : str : " + valueC1[1] + "&& str : " + valueC1[1])
reponse_content = C2.service.execution_des_services(valueC1[1],valueC1[2],valueC3_1)


Nom_Prenom = valueC1[3]
Path_Fichier = "reponse_credit/"
# Résultat de votre fonction
nom_fichier = Nom_Prenom + "_reponse.txt"
# Écriture du résultat dans le fichier
with open(Path_Fichier+Nom_Prenom+ "_reponse.txt", 'w', encoding='utf-8') as fichier:
    fichier.write(reponse_content)

print("\nVotre réponse de crédit se trouve dans : " + Path_Fichier + nom_fichier)

#def func(con1 con2)
