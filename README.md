## TPSpyne

# Creer un nouvel environnement python et l'activer

pip install virtualenv

python -m virtualenv TPSpyne

TPSpyne\Scripts\activate

#desactiver le virtualenv creer plus tot : 
deactivate

# installer les packages necessaires au bon fonctionnement du programme

pip install spyne

pip install suds

pip install soap

python serveur.py
python client.py
