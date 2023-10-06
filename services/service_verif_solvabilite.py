from spyne import Application, rpc, ServiceBase, Unicode, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json

class ServiceVerifSolvabilite(ServiceBase):
    
    @rpc(String, _returns=String)
    def Verif_Solvabilite(ctx,JSON_entr): 
        JSON_Decision=""
        tableau_rentree=[]
        lignes = JSON_entr.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_rentree+=[elements]
        
        Taux_risque=1
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
            if i>4 and i<len(lignes)-1:
                Prets_en_cours+=[int(elements[0])]
            tableau_resultat+=[elements]
            i+=1
        
        Depenses=float(tableau_resultat[3][1])
        Revenus=float(tableau_resultat[2][1])
        
        if Taux_risque <= 0:
            Taux_risque=1
        Score_Credit=100.00
        Score_Credit=Score_Credit/(Duree_emprunt*Taux_risque+Age)
        
        Restant=Revenus-Depenses
        if Restant<0:
            Restant=float(-1/Restant)
        Score_Credit=Score_Credit*(Restant)
        
        for j in Prets_en_cours:
            Score_Credit=Score_Credit-(j/10)
        
        if Age<18 or Duree_emprunt>100:
            Score_Credit=10000
        
        Score_Credit=Score_Credit/100
        
        String_prets=""
        for pret_individuel in Prets_en_cours:
            String_prets+=str(pret_individuel)+"%"
        
        JSON_Decision+="Depenses: "+str(Depenses)+";"
        JSON_Decision+="Revenus: "+str(Revenus)+";"
        JSON_Decision+="Prets_en_cours: "+str(String_prets)+";"
        JSON_Decision+="Score_Credit: "+str(Score_Credit)+";"
        
        return JSON_Decision
    
    
    

    @rpc(String, _returns=String)
    def scoring_de_credit(ctx, demande_credit):
        JSON_retour=""
        tableau_rentree=[]
        lignes = demande_credit.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_rentree+=[elements]
        
        Duree_emprunt=int(tableau_rentree[0][1])
        Age=int(tableau_rentree[1][1])
        Depenses=float(tableau_rentree[2][1])
        Revenus=float(tableau_rentree[3][1])
        Taux_risque=int(tableau_rentree[4][1])
        str_emprunt=tableau_rentree[5][1]
        Score_Credit=float(tableau_rentree[6][1])
        
        Prets_en_cours=[]
        prets_temp=str_emprunt.split('%')
        for j in range(len(prets_temp)-1):
            Prets_en_cours+=[int(prets_temp[j])]
        
        
        Score_Credit=Score_Credit/(Duree_emprunt*Taux_risque+Age)
        
        Restant=Revenus-Depenses
        if Restant<0:
            Restant=float(-1/Restant)
        Score_Credit=Score_Credit*(Restant)
        
        for j in Prets_en_cours:
            Score_Credit=Score_Credit-(j/10)
        
        if Age<18 or Duree_emprunt>100:
            Score_Credit=10000
        
        Score_Credit=Score_Credit/100
        
        String_prets=""
        for pret_individuel in Prets_en_cours:
            String_prets+=str(pret_individuel)+"%"
        
        JSON_retour+="Depenses: "+str(Depenses)+";"
        JSON_retour+="Revenus: "+str(Revenus)+";"
        JSON_retour+="Prets_en_cours: "+str(String_prets)+";"
        JSON_retour+="Score_Credit: "+str(Score_Credit)+";"
        
        return JSON_retour

    @rpc(String, _returns=String)
    def analyse_des_revenus_et_depenses(ctx, demande_credit):
        JSON_retour=""
        tableau_rentree=[]
        lignes = demande_credit.split(';')
        
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_rentree+=[elements]
        
        Duree_emprunt=int(tableau_rentree[0][1])
        Age=int(tableau_rentree[1][1])
        Depenses=float(tableau_rentree[2][1])
        Revenus=float(tableau_rentree[3][1])
        Taux_risque=int(tableau_rentree[4][1])
        str_emprunt=tableau_rentree[5][1]
        
        
        Score_Credit=100.00
        
        Restant=Revenus-Depenses
        if Restant<0:
            Restant=float(-1/Restant)
        Score_Credit=Score_Credit*(Restant)
        
        
        JSON_retour+="Duree_emprunt: "+str(Duree_emprunt)+";"
        JSON_retour+="Age: "+str(Age)+";"
        JSON_retour+="Depenses: "+str(Depenses)+";"
        JSON_retour+="Revenus: "+str(Revenus)+";"
        JSON_retour+="Taux de risque: "+str(Taux_risque)+";"
        JSON_retour+="Prets_en_cours: "+str_emprunt+";"
        JSON_retour+="Score_Credit: "+str(Score_Credit)+";"
        
        return JSON_retour

#Création de l'application à lancer sur le serveur
applicationVeriSolv = Application([ServiceVerifSolvabilite],
    tns='VerifSolvabilite',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appVeriSolv = WsgiApplication(applicationVeriSolv)