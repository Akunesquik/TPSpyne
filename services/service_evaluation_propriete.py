from spyne import Application, rpc, ServiceBase, Unicode,String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json

class ServiceEvaluationPropriete(ServiceBase):
    
    
    @rpc(String, _returns=String)
    def analyse_valeur_propriete(ctx, donnees):
        tableau_resultat=[]
        
        
        lignes = donnees.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]
        
        JSON_Decision="Valeur_propriete: "
        Valeur_propriete=float(tableau_resultat[0][1])
        Duree_emprunt=int(tableau_resultat[1][1])
        Valeur_region=int(tableau_resultat[2][1])
        Note_professionnel=int(tableau_resultat[3][1])
        Objectif=tableau_resultat[4][1]
        
        if Valeur_region==0:#region a fort taux de vente
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*0.7
            else:
                Valeur_propriete=Valeur_propriete*0.08*Duree_emprunt
        elif Valeur_region==1:#region a faible taux de vente
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*2
            else:
                Valeur_propriete=Valeur_propriete*0.03*Duree_emprunt
        elif Valeur_region==2:#region très attractive en tous points
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*2.5
            else:
                Valeur_propriete=Valeur_propriete*0.09*Duree_emprunt
        else:#il ne s'y passe rien, c'est plus ou moins la creuze
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*0.5
            else:
                Valeur_propriete=Valeur_propriete*0.01*Duree_emprunt
        
        
        Valeur_propriete=Valeur_propriete*float((Note_professionnel+3)/10)
        JSON_Decision+=str(Valeur_propriete)
        
        return JSON_Decision
    
    @rpc(String, _returns=String)
    def analyse_des_donnees_du_marche_immobilier(ctx, donnees):
        tableau_resultat=[]
        
        lignes = donnees.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]
        
        
        Valeur_propriete=float(tableau_resultat[0][1])
        Duree_emprunt=int(tableau_resultat[1][1])
        Valeur_region=int(tableau_resultat[2][1])
        Note_professionnel=int(tableau_resultat[3][1])
        Objectif=tableau_resultat[4][1]
        
        if Valeur_region==0:#region a fort taux de vente
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*0.7
            else:
                Valeur_propriete=Valeur_propriete*0.08*Duree_emprunt
        elif Valeur_region==1:#region a faible taux de vente
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*2
            else:
                Valeur_propriete=Valeur_propriete*0.03*Duree_emprunt
        elif Valeur_region==2:#region très attractive en tous points
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*2.5
            else:
                Valeur_propriete=Valeur_propriete*0.09*Duree_emprunt
        else:#il ne s'y passe rien, c'est plus ou moins la creuze
            if Objectif=="PROPRIETE":
                Valeur_propriete=Valeur_propriete*0.5
            else:
                Valeur_propriete=Valeur_propriete*0.01*Duree_emprunt
        
        JSOn_retour=""
        JSOn_retour+="Valeur_propriete: "+str(Valeur_propriete)+";"
        JSOn_retour+="Note_professionnel: "+ str(Note_professionnel)+";"
        
        return JSOn_retour

    @rpc(String, _returns=String)
    def inspection_virtuelle_ou_sur_place(ctx, propriete):
        tableau_resultat=[]
        
        lignes = propriete.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]
        
        
        JSOn_retour="Valeur_propriete: "
        Valeur_propriete=float(tableau_resultat[0][1])
        Note_professionnel=int(tableau_resultat[1][1])
        
        Valeur_propriete=Valeur_propriete*float((Note_professionnel+3)/10)
        
        JSOn_retour=""
        JSOn_retour+="Valeur_propriete: "+str(Valeur_propriete)+";"
        
        return JSOn_retour

    @rpc(String, _returns=String)
    def conformite_legale_et_reglementaire(ctx, propriete):
        tableau_resultat=[]
        
        lignes = propriete.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]
        
        
        Valeur_propriete=float(tableau_resultat[0][1])
        Duree_emprunt=int(tableau_resultat[1][1])
        Valeur_region=int(tableau_resultat[2][1])
        Note_professionnel=int(tableau_resultat[3][1])
        Objectif=tableau_resultat[4][1]
        Respecte_loi=tableau_resultat[5][1]
        
        if Respecte_loi!="OUI":
            Valeur_propriete=0
        
        
        JSOn_retour=""
        JSOn_retour+="Valeur_propriete: "+str(Valeur_propriete)+";"
        JSOn_retour+="Duree_emprunt: "+ str(Duree_emprunt)+";"
        JSOn_retour+="Valeur_region: "+ str(Valeur_region)+";"
        JSOn_retour+="Note_professionnel: "+ str(Note_professionnel)+";"
        JSOn_retour+="Objectif: "+ Objectif+";"
        
        return JSOn_retour

#Création de l'application à lancer sur le serveur
applicationEvalPropr = Application([ServiceEvaluationPropriete],
    tns='EvaluationPropriete',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appEvalPropr = WsgiApplication(applicationEvalPropr)