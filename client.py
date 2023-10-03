from suds.client import Client
import sys
import json

filename = sys.argv[1]

# Lire le contenu du fichier
with open(filename, 'r', encoding='utf-8') as file:
    contenu_fichier = file.read()


#Client permet d'acceder a l'URL afin d'appeler les fonctions des services
#On les appelle de la forme suivante :
# Client.service.nomDeLaFonction(args...)
C1 = Client('http://localhost:8000/InfoMetier?wsdl')
tab= C1.service.Extraction_information(contenu_fichier)
print(tab)
