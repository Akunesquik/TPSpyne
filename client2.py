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
print("\nProgression  0% |               |", end='\r')
valueC1 = C1.service.Extraction_information(contenu_fichier)
print("Progression  6% |#              |", end='\r')
C2 = Client('http://localhost:8000/EvalPropr?wsdl')
print("Progression 12% |##             |", end='\r')
valueC2_1=C2.service.conformite_legale_et_reglementaire(valueC1[1])
print("Progression 18% |###            |", end='\r')
valueC2_2=C2.service.analyse_des_donnees_du_marche_immobilier(valueC2_1)
print("Progression 24% |####           |", end='\r')
valueC2_3=C2.service.inspection_virtuelle_ou_sur_place(valueC2_2)
print("Progression 30% |#####          |", end='\r')

C3 = Client('http://localhost:8000/VeriSolv?wsdl')
print("Progression 36% |######         |", end='\r')
valueC3_1=C3.service.integration_des_bureaux_de_credit(valueC1[0])
print("Progression 42% |#######        |", end='\r')
valueC3_2=C3.service.analyse_des_revenus_et_depenses(valueC3_1)
print("Progression 48% |########       |", end='\r')
valueC3_3=C3.service.scoring_de_credit(valueC3_2)
print("Progression 54% |#########      |", end='\r')
C4 = Client('http://localhost:8000/DeciAppro?wsdl')
print("Progression 60% |##########     |", end='\r')
C4_1=C4.service.analyses_des_risques((valueC1[2]+"*"+valueC2_1+"*"+valueC3_3))
print("Progression 67% |###########    |", end='\r')
C4_2=C4.service.modele_de_prediction(C4_1)
print("Progression 74% |############   |", end='\r')
C4_3=C4.service.politiques_de_linstitu_financiere(C4_2)
print("Progression 82% |#############  |", end='\r')
C4_4=C4.service.prise_de_decision(C4_3)
print("Progression 90% |############## |", end='\r')
reponse_content = C4.service.communication_de_la_decision(C4_4)
print("Progression 100% |################|\n")

Nom_Prenom = valueC1[3]
Path_Fichier = "reponse_credit/"
# Résultat de votre fonction
nom_fichier = Nom_Prenom + "_reponse.txt"
# Écriture du résultat dans le fichier
with open(Path_Fichier+Nom_Prenom+ "_reponse.txt", 'w', encoding='utf-8') as fichier:
    fichier.write(reponse_content)

print("Votre réponse de crédit se trouve dans : " + Path_Fichier + nom_fichier)