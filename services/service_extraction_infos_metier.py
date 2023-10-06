from spyne import Application, rpc, ServiceBase, Unicode,String,Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json
import os

class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # Implémentez le prétraitement du texte ici
        return texte
    
    @rpc(Unicode, _returns=[String,String,String,String])
    def Extraction_information(ctx,fichierOuvert):
        tableau_resultat=[]
        
        lignes = fichierOuvert.split('\n')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]
        
        JSON_Verif_Solv=""
        JSON_Eval_Prop=""
        JSON_Decision=""
        
        
        JSON_Verif_Solv+="Prenom: " +tableau_resultat[1][1]+";"
        JSON_Verif_Solv+="Nom: "+tableau_resultat[0][1]+";"
        JSON_Verif_Solv+="Duree_emprunt: "+tableau_resultat[6][1].split(' ')[0]+";"
        JSON_Verif_Solv+="Age: "+tableau_resultat[12][1]+";"
        
        JSON_Eval_Prop+="Valeur_propriete: "+tableau_resultat[5][1].split(' ')[0]+";"
        JSON_Eval_Prop+="Duree_emprunt: "+ tableau_resultat[6][1].split(' ')[0]+";"
        JSON_Eval_Prop+="Valeur_region: "+ tableau_resultat[8][1]+";"
        JSON_Eval_Prop+="Note_professionnel: "+ tableau_resultat[9][1]+";"
        JSON_Eval_Prop+="Objectif: "+ tableau_resultat[11][1]+";"
        JSON_Eval_Prop+="respecte_loi: "+ tableau_resultat[10][1]+";"
        
        JSON_Decision+="Duree_emprunt: "+tableau_resultat[6][1].split(' ')[0]+";"
        JSON_Decision+="Age: "+tableau_resultat[12][1]+";"
        JSON_Decision+="Valeur_pret: "+tableau_resultat[4][1].split(' ')[0]+";"
        JSON_Decision+="respecte_loi: "+ tableau_resultat[10][1]+";"
        JSON_Decision+="Valeur_emprunt: "+tableau_resultat[5][1].split(' ')[0]+";"
        
        JSON_NP=tableau_resultat[1][1]+"_"+tableau_resultat[0][1]
        return JSON_Verif_Solv,JSON_Eval_Prop,JSON_Decision,JSON_NP
    
    @rpc(String, _returns=String)
    def integration_des_bureaux_de_credit(ctx, demande_credit):
        JSON_retour=""
        tableau_rentree=[]
        lignes = demande_credit.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_rentree+=[elements]
        
        Age=int(tableau_rentree[3][1])
        Nom=tableau_rentree[1][1]
        Prenom=tableau_rentree[0][1]
        Duree_emprunt=int(tableau_rentree[2][1])
        
        nom_fichier="./DATABASE_CREDIT/"+Prenom+"_"+Nom+"_credit.txt"
        file = open(nom_fichier, 'r')
        file_str = file.read()
        tableau_resultat=[]
        Prets_en_cours=[]
        
        
        lignes = file_str.split('\n')
        i=0
        for ligne in lignes:
            elements = ligne.split(': ')
            if i>5 and i<len(lignes)-1:
                Prets_en_cours+=[int(elements[0])]
            tableau_resultat+=[elements]
            i+=1
        
        Depenses=float(tableau_resultat[3][1])
        Revenus=float(tableau_resultat[2][1])
        Taux_risque=int(tableau_resultat[4][1])
        
        String_prets=""
        for pret_individuel in Prets_en_cours:
            String_prets+=str(pret_individuel)+"%"
        
        JSON_retour+="Duree_emprunt: "+str(Duree_emprunt)+";"
        JSON_retour+="Age: "+str(Age)+";"
        JSON_retour+="Depenses: "+str(Depenses)+";"
        JSON_retour+="Revenus: "+str(Revenus)+";"
        JSON_retour+="Taux de risque: "+str(Taux_risque)+";"
        JSON_retour+="Prets_en_cours: "+str(String_prets)+";"
        
        return JSON_retour
    
    
#Création de l'application à lancer sur le serveur
applicationInfoMetier = Application([ServiceExtractionInfosMetier],
    tns='ExtractionInfosMetier',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appInfoMetier = WsgiApplication(applicationInfoMetier)