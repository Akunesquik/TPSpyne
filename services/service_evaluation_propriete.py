from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11

class ServiceEvaluationPropriete(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def analyse_des_donnees_du_marche_immobilier(ctx, donnees):
        #si la propriété est en ile-de-france on ajoute 10 000 au prix
        
        #on cree un tableau qui stock les departements d'ile-de-france
        departements = ["75", "77", "78", "91", "92", "93", "94", "95"]
        #on regarde dans adresse le moment ou il y a une suite de 5 chiffres et on compare les deux premiers avec departements  
        for i in range(len(donnees.adresse)-5):
            if donnees.adresse[i:i+5].isdigit():
                if donnees.adresse[i:i+2] in departements:
                    donnees.montant_pret += 10000
        
        return donnees

    @rpc(Unicode, _returns=Unicode)
    def inspection_virtuelle_ou_sur_place(ctx, propriete):
        # on met un bonus ou un malus aléatoire de 1 à 5000 euro en fonction de si la propriété est bien entretenue ou non
        import random
        bonus = random.randint(1, 5000)
        
        #si le texte contient bien entretenue 
        if "bien entretenue" in propriete.description_propriete:
            propriete.montant_pret += bonus
        else:
            propriete.montant_pret -= bonus
        
        return propriete

    @rpc(Unicode, _returns=Unicode)
    def conformite_legale_et_reglementaire(ctx, propriete):
        # Implémentez la conformité légale et réglementaire ici
        return propriete
