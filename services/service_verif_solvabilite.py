from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11

class ServiceVerifSolvabilite(ServiceBase):


    @rpc(Unicode, _returns=Unicode)
    def scoring_de_credit(ctx, demande_credit):
        # on recupere les données dans la string
        splittedText = demande_credit.split("\n")
        montant_pret = splittedText[4]
        duree_pret= splittedText[5]
        revenu_mensuel = splittedText[7]   
        depenses_mensuelles = splittedText[8]
                
        score = 0
        
        dureeEnMois = duree_pret * 12
        
        pret_mensuel = montant_pret / dureeEnMois
        revenuNet = revenu_mensuel - depenses_mensuelles
        
        #si on a plus de revenunet que de pret mensuel a rembourser on ajoute 5 au score
        if (revenuNet > pret_mensuel):
            score += 5
                    
        return score

    @rpc(Unicode, _returns=Unicode)
    def analyse_des_revenus_et_depenses(ctx, demande_credit):
        
        # on recupere les données dans la string
        splittedText = demande_credit.split("\n")
        revenu_mensuel = splittedText[7]   
        depenses_mensuelles = splittedText[8]
        
        # on calcule le taux d'endettement
        taux_endettement = (depenses_mensuelles / revenu_mensuel) * 100
  
        return taux_endettement
    
    @rpc(Unicode, _returns=Unicode)
    def integration_des_bureaux_de_credit(ctx, demande_credit):
        
        #on cree une variable taux endettement qu'on initialise au resultat retournee par la fonction analyse_des_revenus_et_depenses
        taux_endettement = ServiceVerifSolvabilite.analyse_des_revenus_et_depenses(demande_credit)
        
        score = ServiceVerifSolvabilite.scoring_de_credit(demande_credit) 
        
        if taux_endettement > 35 :
            score -= 5
        elif taux_endettement > 25 :
            score -= 3
        elif taux_endettement > 15 :
            score += 1
        elif taux_endettement > 10 :
            score += 3
        elif taux_endettement > 5 :
            score += 5
        
        
        return score

