from suds.client import Client

C1 = Client('http://localhost:8000/DeciAppro?wsdl')
print(C1.service.analyses_des_risques('DeciAppro'))

C2 = Client('http://localhost:8000/EvalPropr?wsdl')
print(C2.service.analyse_des_donnees_du_marche_immobilier('EvalPropr'))

C3 = Client('http://localhost:8000/InfoMetier?wsdl')
print(C3.service.pretraitement_de_texte('InfoMetier'))

C4 = Client('http://localhost:8000/VeriSolv?wsdl')
print(C4.service.integration_des_bureaux_de_credit('VeriSolv'))
