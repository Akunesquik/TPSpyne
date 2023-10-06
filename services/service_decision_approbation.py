from spyne import Application, rpc, ServiceBase, Unicode, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json

class ServiceDecisionApprobation(ServiceBase):
    @rpc(String, _returns=String)
    def analyses_des_risques(ctx, demande_credit):
        tableau_entrees=demande_credit.split('*')
        
        JSON_Information=tableau_entrees[0]
        JSON_Valeur_Propriete=tableau_entrees[1]
        JSON_Solvabilite=tableau_entrees[2]
        
        tableau_information,tableau_solvabilite,tableau_valeur_propriete=[],[],[]
        
        lignes = JSON_Information.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_information+=[elements]
        
        lignes = JSON_Valeur_Propriete.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_valeur_propriete+=[elements]
        
        lignes = JSON_Solvabilite.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_solvabilite+=[elements]
        
        
        
        
        Duree_emprunt=int(tableau_information[0][1])
        Age=int(tableau_information[1][1])
        Valeur_pret=float(tableau_information[2][1])
        respecte_loi=tableau_information[3][1]
        
        Depenses=float(tableau_solvabilite[0][1])
        Revenus=float(tableau_solvabilite[1][1])
        STR_pret=tableau_solvabilite[2][1]
        Score_Credit=float(tableau_solvabilite[3][1])
        
        Valeur_propriete=float(tableau_valeur_propriete[0][1])
        
        
        Autres_prets=[]
        prets_temp=STR_pret.split('%')
        for j in range(len(prets_temp)-1):
            Autres_prets+=[int(prets_temp[j])]
        
        print("\n\n tableau prets: ",Autres_prets,"\n\n")
        PolitiqueA=1#refus de clients sans benefice net
        PolitiqueB=50000#refus de dettes superieures à #valeur#
        PolitiqueC=3.0#taux de risque maximum envisagé par la banque
        PolitiqueD=0.05#taux d'interets de la banque
        
        Taux_de_risque=0.0
        
        Somme_dettes=0
        for k in Autres_prets:
            Somme_dettes+=k
        
        Taux_de_risque=Taux_de_risque+(Somme_dettes/10000)
        
        print("taux de risque lie aux dettes: ",Taux_de_risque)
        
        
        Taux_de_risque=Taux_de_risque-Score_Credit/2
        
        print("taux de risque lie au score de credit: ",Taux_de_risque)
        
        
        
        JSON_Decision=""
        JSON_Decision+="Duree_emprunt: "+str(Duree_emprunt)+";"
        JSON_Decision+="Age: "+str(Age)+";"
        JSON_Decision+="Valeur_propriete: "+str(Valeur_propriete)+";"
        JSON_Decision+="respecte_loi: "+ respecte_loi+";"
        JSON_Decision+="Valeur_pret: "+str(Valeur_pret)+";"
        JSON_Decision+="Depenses: "+str(Depenses)+";"
        JSON_Decision+="Revenus: "+str(Revenus)+";"
        JSON_Decision+="Prets_en_cours: "+str(STR_pret)+";"
        JSON_Decision+="Taux_de_risques: "+str(Taux_de_risque)+";"
        
        
        return JSON_Decision

    @rpc(String, _returns=String)
    def politiques_de_linstitu_financiere(ctx, demande_credit):
        lignes=demande_credit.split(';')
        
        tableau_entrees=[]
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_entrees+=[elements]
        
        Duree_emprunt=int(tableau_entrees[0][1])#necessaire
        respecte_loi=tableau_entrees[1][1]#necessaire
        Valeur_pret=float(tableau_entrees[2][1])#necessaire
        Depenses=float(tableau_entrees[3][1])#necessaire
        Revenus=float(tableau_entrees[4][1])#necessaire
        STR_pret=tableau_entrees[5][1]#necessaire
        Taux_de_risque=float(tableau_entrees[6][1])#necessaire
        
        
        
        PolitiqueA=1#refus de clients sans benefice net
        PolitiqueB=50000#refus de dettes superieures à #valeur#
        PolitiqueC=3.0#taux de risque maximum envisagé par la banque
        PolitiqueD=0.05#taux d'interets de la banque
        
        Autres_prets=[]
        prets_temp=STR_pret.split('%')
        for j in range(len(prets_temp)-1):
            Autres_prets+=[int(prets_temp[j])]
        
        
        Refuse="NON"
        Motif=""
        
        Somme_dettes=0
        for k in Autres_prets:
            Somme_dettes+=k
        
        Taux_de_risque=Taux_de_risque*(PolitiqueD+1)
        
        print("taux de risque lie au taux d'interet: ",Taux_de_risque)
        
        if Revenus<Depenses and PolitiqueA==1:
            Refuse="OUI"
            Motif="Entree d'argent inferieures aux sorties d'argent, impossible de preter dans ces conditions \n"
        
        if Somme_dettes>PolitiqueB:
            Refuse="OUI"
            Motif="Désolé, notre banque n'autorise pas les emprunts pour les personnes ayant contracté plus de ",PolitiqueB," euros d'emprunts \n"
        
        
        if respecte_loi!="OUI":
            Refuse="OUI"
            Motif+="propriete illegale, on appelle la maréchaussée tout de suite \n"
        
        JSON_Decision=""
        JSON_Decision+="Duree_emprunt: "+str(Duree_emprunt)+";"
        JSON_Decision+="Valeur_pret: "+str(Valeur_pret)+";"
        JSON_Decision+="Refuse: "+Refuse+";"
        JSON_Decision+="Motif: "+Motif+";"
        JSON_Decision+="Taux_de_risques: "+str(Taux_de_risque)+";"
        
        return JSON_Decision

    @rpc(String, _returns=String)
    def modele_de_prediction(ctx, String_entree):
        lignes=String_entree.split(';')
        
        tableau_entrees=[]
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_entrees+=[elements]
            
        Duree_emprunt=int(tableau_entrees[0][1])#necessaire
        Age=int(tableau_entrees[1][1])#necessaire
        Valeur_propriete=float(tableau_entrees[2][1])
        respecte_loi=tableau_entrees[3][1]#necessaire
        Valeur_pret=float(tableau_entrees[4][1])#necessaire
        Depenses=float(tableau_entrees[5][1])#necessaire
        Revenus=float(tableau_entrees[6][1])#necessaire
        STR_pret=tableau_entrees[7][1]#necessaire
        Taux_de_risque=float(tableau_entrees[8][1])#necessaire
        
        
        
        PolitiqueA=1#refus de clients sans benefice net
        PolitiqueB=50000#refus de dettes superieures à #valeur#
        PolitiqueC=3.0#taux de risque maximum envisagé par la banque
        PolitiqueD=0.05#taux d'interets de la banque
        
        if Age+Duree_emprunt>100:
            Taux_de_risque=Taux_de_risque-(100-(Age+Duree_emprunt))*2
        
        print("taux de risque lie à l'age: ",Taux_de_risque)
        
        if Valeur_propriete>Valeur_pret:
            Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/10000)
        
        print("taux de risque lie à la valuation de la propriete: ",Taux_de_risque)
        
        if Valeur_propriete<Valeur_pret:
            Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/5000)
        
        print("taux de risque lie à la dévaluation de la propriete: ",Taux_de_risque)
        
        if Revenus>Depenses:
            if ((Revenus-Depenses)*Duree_emprunt)<Valeur_pret:
                Taux_de_risque+=(Valeur_pret-((Revenus-Depenses)*Duree_emprunt*12))/1000
        
        print("taux de risque lie au ratio emprunt/capacite à rembourser: ",Taux_de_risque)
        
        
        JSON_Decision=""
        JSON_Decision+="Duree_emprunt: "+str(Duree_emprunt)+";"
        JSON_Decision+="respecte_loi: "+ respecte_loi+";"
        JSON_Decision+="Valeur_pret: "+str(Valeur_pret)+";"
        JSON_Decision+="Depenses: "+str(Depenses)+";"
        JSON_Decision+="Revenus: "+str(Revenus)+";"
        JSON_Decision+="Prets_en_cours: "+STR_pret+";"
        JSON_Decision+="Taux_de_risques: "+str(Taux_de_risque)+";"
        
        
        return JSON_Decision

    @rpc(String, _returns=String)
    def prise_de_decision(ctx, decision):
        lignes=decision.split(';')
        
        tableau_entrees=[]
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_entrees+=[elements]
        
        Duree_emprunt=int(tableau_entrees[0][1])
        Valeur_pret=float(tableau_entrees[1][1])
        Refuse=tableau_entrees[2][1]
        Motif=tableau_entrees[3][1]
        Taux_de_risque=float(tableau_entrees[4][1])
        
        
        PolitiqueA=1#refus de clients sans benefice net
        PolitiqueB=50000#refus de dettes superieures à #valeur#
        PolitiqueC=3.0#taux de risque maximum envisagé par la banque
        PolitiqueD=0.05#taux d'interets de la banque
        
        if Refuse == "OUI":
            return Motif
        
        if PolitiqueC<Taux_de_risque:
            return "Nous nous voyons dans l'incapacité d'accepter votre demande de pret, vous nous en voyez désolés"
        
        Somme_mensuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt*12)
        Somme_annuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt)
        if PolitiqueC>Taux_de_risque:
            return str("Nous sommes ravis de pouvoir vous dire que votre prêt a été validé par notre système. AVec le taux d'interet de "+str(PolitiqueD)+" % vous serez soumis à un paiment de "+str(Somme_mensuelle)+" euros par mois( ou "+str(Somme_annuelle)+" euros par an) pendant "+str(Duree_emprunt)+" ans")
        
        
        return "erreur dans le calculs, veuillez patienter..."

    @rpc(String, _returns=String)
    def communication_de_la_decision(ctx, decision):
        if decision=="erreur":
            return "issue with computing"
        return decision

    @rpc(String, _returns=String)
    def suivi_de_performances(ctx, performances):
        # Implémentez le suivi de performances ici
        return performances
    
    @rpc(String, _returns=String)
    def Prise_Decision(ctx,String_entree):
        
        tableau_entrees=String_entree.split('*')
        
        JSON_Information=tableau_entrees[0]
        JSON_Valeur_Propriete=tableau_entrees[1]
        JSON_Solvabilite=tableau_entrees[2]
        
        tableau_information,tableau_solvabilite,tableau_valeur_propriete=[],[],[]
        
        lignes = JSON_Information.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_information+=[elements]
        
        lignes = JSON_Valeur_Propriete.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_valeur_propriete+=[elements]
        
        lignes = JSON_Solvabilite.split(';')
        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_solvabilite+=[elements]
        
        
        print("\n\n tableau_information: ",tableau_information,"\n\n")
        print("\n\n tableau_valeur_propriete: ",tableau_valeur_propriete,"\n\n")
        print("\n\n tableau_solvabilite: ",tableau_solvabilite,"\n\n")
        
        
        Duree_emprunt=int(tableau_information[0][1])
        Age=int(tableau_information[1][1])
        Valeur_pret=float(tableau_information[2][1])
        respecte_loi=tableau_information[3][1]
        
        Sorties=float(tableau_solvabilite[0][1])
        Entree=float(tableau_solvabilite[1][1])
        STR_pret=tableau_solvabilite[2][1]
        Score_Credit=float(tableau_solvabilite[3][1])
        
        Valeur_propriete=float(tableau_valeur_propriete[0][1])
        
        
        Autres_prets=[]
        prets_temp=STR_pret.split('%')
        for j in range(len(prets_temp)-1):
            Autres_prets+=[int(prets_temp[j])]
        
        print("\n\n tableau prets: ",Autres_prets,"\n\n")
        PolitiqueA=1#refus de clients sans benefice net
        PolitiqueB=50000#refus de dettes superieures à #valeur#
        PolitiqueC=3.0#taux de risque maximum envisagé par la banque
        PolitiqueD=0.05#taux d'interets de la banque
        
        Taux_de_risque=0.0
        if Age+Duree_emprunt>100:
            Taux_de_risque=Taux_de_risque-(100-(Age+Duree_emprunt))*2
        
        print("taux de risque lie à l'age: ",Taux_de_risque)
        
        Somme_dettes=0
        for k in Autres_prets:
            Somme_dettes+=k
        
        Taux_de_risque=Taux_de_risque+(Somme_dettes/10000)
        
        print("taux de risque lie aux dettes: ",Taux_de_risque)
        
        if Valeur_propriete>Valeur_pret:
            Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/10000)
        
        print("taux de risque lie à la valuation de la propriete: ",Taux_de_risque)
        
        if Valeur_propriete<Valeur_pret:
            Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/5000)
        
        print("taux de risque lie à la dévaluation de la propriete: ",Taux_de_risque)
        
        if Entree>Sorties:
            if ((Entree-Sorties)*Duree_emprunt)<Valeur_pret:
                Taux_de_risque+=(Valeur_pret-((Entree-Sorties)*Duree_emprunt*12))/1000
        
        print("taux de risque lie au ratio emprunt/capacite à rembourser: ",Taux_de_risque)
        
        Taux_de_risque=Taux_de_risque*(PolitiqueD+1)
        
        print("taux de risque lie au taux d'interet: ",Taux_de_risque)
        
        Taux_de_risque=Taux_de_risque-Score_Credit/2
        
        print("taux de risque lie au score de credit: ",Taux_de_risque)
        
        if Entree<Sorties and PolitiqueA==1:
            return "Entree d'argent inferieures aux sorties d'argent, impossible de preter dans ces conditions"
        
        if Somme_dettes>PolitiqueB:
            return "Désolé, notre banque n'autorise pas les emprunts pour les personnes ayant contracté plus de ",PolitiqueB," euros d'emprunts"
        
        
        if respecte_loi!="OUI":
            return "propriete illegale, on appelle la maréchaussée tout de suite"
        
        if PolitiqueC<Taux_de_risque:
            return "Nous nous voyons dans l'incapacité d'accepter votre demande de pret, vous nous en voyez désolés"
        
        Somme_mensuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt*12)
        Somme_annuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt)
        if PolitiqueC>Taux_de_risque:
            Accord= str("Nous sommes ravis de pouvoir vous dire que votre prêt a été validé par notre système. AVec le taux d'interet de "+str(PolitiqueD)+" % vous serez soumis à un paiment de "+str(Somme_mensuelle)+" euros par mois( ou "+str(Somme_annuelle)+" euros par an) pendant "+str(Duree_emprunt)+" ans")
            return Accord
        return 'erreur'


#Création de l'application à lancer sur le serveur
applicationDeciAppro = Application([ServiceDecisionApprobation],
    tns='DecisionApprobation',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appDeciAppro = WsgiApplication(applicationDeciAppro)


