from spyne import Application, rpc, ServiceBase, Unicode, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from suds.client import Client

class ServiceSWC(ServiceBase):
    @rpc(String,String,String, _returns=String)
    def execution_des_services(ctx, contenu_fichier1,contenu_fichier2, info_bdd):
        print("\nEntré dans le SWC")
        C2 = Client('http://localhost:8000/EvalPropr?wsdl')
        
        valueC2_1=C2.service.conformite_legale_et_reglementaire(contenu_fichier1)
        print("Service : conformite_legale_et_reglementaire\nEntré : "+ contenu_fichier1 + "\nSortie : "+ valueC2_1+" \nProgression  10% |#         |\n")
        valueC2_2=C2.service.analyse_des_donnees_du_marche_immobilier(valueC2_1)
        print("Service : analyse_des_donnees_du_marche_immobilier\nEntré : "+ valueC2_1 + "\nSortie : "+ valueC2_2+"\nProgression  20% |##        |\n")
        valueC2_3=C2.service.inspection_virtuelle_ou_sur_place(valueC2_2)
        print("Service : inspection_virtuelle_ou_sur_place\nEntré : "+ valueC2_2 + "\nSortie : "+ valueC2_3+"\nProgression  30% |###       |\n")

        C3 = Client('http://localhost:8000/VeriSolv?wsdl')
        #valueC3_1=C3.service.integration_des_bureaux_de_credit(contenu_fichier[0])
        valueC3_2=C3.service.analyse_des_revenus_et_depenses(info_bdd)
        print("Service : analyse_des_revenus_et_depenses\nEntré : "+ info_bdd + "\nSortie : "+ valueC3_2+ "\nProgression  40% |####      |\n")
        valueC3_3=C3.service.scoring_de_credit(valueC3_2)
        print("Service : scoring_de_credit\nEntré : "+ valueC3_2 + "\nSortie : "+ valueC3_3+ "\nProgression  50% |#####     |\n")

        C4 = Client('http://localhost:8000/DeciAppro?wsdl')
        C4_1=C4.service.analyses_des_risques((contenu_fichier2+"*"+valueC2_1+"*"+valueC3_3))
        print("Service : analyses_des_risques\nEntré : "+ contenu_fichier2+"*"+valueC2_1+"*"+valueC3_3 + "\nSortie : "+ C4_1+ "\nProgression  60% |######    |\n")
        C4_2=C4.service.modele_de_prediction(C4_1)
        print("Service : modele_de_prediction\nEntré : "+ C4_1 + "\nSortie : "+ C4_2+ "\nProgression  70% |#######   |\n")
        C4_3=C4.service.politiques_de_linstitu_financiere(C4_2)
        print("Service : politiques_de_linstitu_financiere\nEntré : "+ C4_2 + "\nSortie : "+ C4_3+ "\nProgression  80% |########  |\n")
        C4_4=C4.service.prise_de_decision(C4_3)
        print("Service : prise_de_decision\nEntré : "+ C4_3 + "\nSortie : "+ C4_4+ "\nProgression  90% |######### |\n")
        reponse_content = C4.service.communication_de_la_decision(C4_4)
        print("Service : communication_de_la_decision\nEntré : "+ C4_4 + "\nSortie : "+ reponse_content+ "\nProgression 100% |##########|\n")
        print("\nSorti du SWC")
        return reponse_content
    

#Création de l'application à lancer sur le serveur
applicationSWC = Application([ServiceSWC],
    tns='SWC',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appSWC = WsgiApplication(applicationSWC)