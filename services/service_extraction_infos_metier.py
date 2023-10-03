from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # Implémentez le prétraitement du texte ici
        return texte

#Création de l'application à lancer sur le serveur
applicationInfoMetier = Application([ServiceExtractionInfosMetier],
    tns='ExtractionInfosMetier',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_appInfoMetier = WsgiApplication(applicationInfoMetier)