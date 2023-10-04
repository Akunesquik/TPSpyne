from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from demande import Demande
class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # on prend le texte et a chaque ligne on prend tous les elements a droite de : c'est à adire element:11 on prend 11 
        texte = texte.split("\n")
        for i in range(len(texte)):
            texte[i] = texte[i].split(":")[1]
        
        # on affiche le texte pour chaque ligne
        for i in range(len(texte)):
            print(texte[i]) 
        
        return texte
