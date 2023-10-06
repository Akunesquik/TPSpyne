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
valueC1 = C1.service.Extraction_information(contenu_fichier)

C2 = Client('http://localhost:8000/EvalPropr?wsdl')
valueC2_1=C2.service.conformite_legale_et_reglementaire(valueC1[1])
valueC2_2=C2.service.analyse_des_donnees_du_marche_immobilier(valueC2_1)
valueC2_3=C2.service.inspection_virtuelle_ou_sur_place(valueC2_2)

C3 = Client('http://localhost:8000/VeriSolv?wsdl')
valueC3_1=C3.service.integration_des_bureaux_de_credit(valueC1[0])
valueC3_2=C3.service.analyse_des_revenus_et_depenses(valueC3_1)
valueC3_3=C3.service.scoring_de_credit(valueC3_2)

C4 = Client('http://localhost:8000/DeciAppro?wsdl')
C4_1=C4.service.analyses_des_risques((valueC1[2]+"*"+valueC2_1+"*"+valueC3_3))
C4_2=C4.service.modele_de_prediction(C4_1)
C4_3=C4.service.politiques_de_linstitu_financiere(C4_2)
C4_4=C4.service.prise_de_decision(C4_3)
print(C4.service.communication_de_la_decision(C4_4))