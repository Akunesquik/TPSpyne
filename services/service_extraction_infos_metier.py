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
    
    @rpc(Unicode, _returns=[String,String,String])
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
        
        
        return JSON_Verif_Solv,JSON_Eval_Prop,JSON_Decision
    
    
#Création de l'application à lancer sur le serveur
applicationInfoMetier = Application([ServiceExtractionInfosMetier],
    tns='ExtractionInfosMetier',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appInfoMetier = WsgiApplication(applicationInfoMetier)