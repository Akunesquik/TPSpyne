import sys
from spyne.util.wsgi_wrapper import run_twisted
import logging
logging.basicConfig(level=logging.DEBUG)

from services.service_decision_approbation import wsgi_appDeciAppro
from services.service_evaluation_propriete import wsgi_appEvalPropr
from services.service_extraction_infos_metier import wsgi_appInfoMetier
from services.service_verif_solvabilite import wsgi_appVeriSolv

if __name__ == '__main__':

    #Adresse de Base : http://localhost:8000/
    twisted_apps = [
        #Ajout de l'url en fonction de la WSGI_app
        #ex : b'DeciAppro' --> URL : http://localhost:8000/DeciAppro?wsdl
        (wsgi_appDeciAppro, b'DeciAppro'),
        (wsgi_appEvalPropr, b'EvalPropr'),
        (wsgi_appInfoMetier, b'InfoMetier'),
        (wsgi_appVeriSolv, b'VeriSolv'),
    ]
    #run le serveur au port 8000
    sys.exit(run_twisted(twisted_apps, 8000))
    
    