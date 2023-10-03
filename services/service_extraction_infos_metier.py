from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode
from spyne.model import Array

class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # Implémentez le prétraitement du texte ici
        return texte
    
    @rpc(Unicode, _returns=Array(Unicode))
    def Extraction_information(ctx,fichierOuvert):
        tableau_resultat=[]

        lignes = fichierOuvert.split('\n')

        for ligne in lignes:
            elements = ligne.split(': ')
            tableau_resultat+=[elements]

        return tableau_resultat[1]
    
    
#Création de l'application à lancer sur le serveur
applicationInfoMetier = Application([ServiceExtractionInfosMetier],
    tns='ExtractionInfosMetier',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appInfoMetier = WsgiApplication(applicationInfoMetier)