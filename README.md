## TPSpyne

# Creer un nouvel environnement python
pip install virtualenv
virtualenv TPSpyne 
TPSpyne\Scripts\activate

deactivate

# installer les packages necessaires au bon fonctionnement du programme
pip install spyne
pip install suds
pip install soap

python serveur.py
python client.py
