# TPSpyne

## Creer un nouvel environnement python et l'activer

pip install virtualenv

### Une des deux selon ce qui fonctionne
python -m virtualenv TPSpyne

virtualenv TPSpyne
###

TPSpyne\Scripts\activate

#desactiver le virtualenv creer plus tot : 
deactivate

## Installation des packages necessaires au programme

pip install watchdog twisted spyne suds soap

## A faire tourner en arrière-plan !
python serveur.py
python listener.py


## Ajouter un fichier .txt du bon format dans le dossier depot pour lancer le client
nous utilisons "client2.py" comme client