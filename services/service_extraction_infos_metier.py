from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11

class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # Implémentez le prétraitement du texte ici
        return texte


application_service_extraction_infos_metier = Application([ServiceExtractionInfosMetier], 'http://localhost:8000/service_extraction_infos_metier/?wsdl',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())