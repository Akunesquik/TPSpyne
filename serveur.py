import sys
from spyne.util.wsgi_wrapper import run_twisted


from services.service_decision_approbation import wsgi_appDeciAppro
from services.service_evaluation_propriete import wsgi_appEvalPropr
from services.service_extraction_infos_metier import wsgi_appInfoMetier
from services.service_verif_solvabilite import wsgi_appVeriSolv

if __name__ == '__main__':

    twisted_apps = [
        (wsgi_appDeciAppro, b'DeciAppro'),
        (wsgi_appEvalPropr, b'EvalPropr'),
        (wsgi_appInfoMetier, b'InfoMetier'),
        (wsgi_appVeriSolv, b'VeriSolv'),
    ]

    sys.exit(run_twisted(twisted_apps, 8000))
    
    