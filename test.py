from suds.client import Client


# Créez un client SOAP pour le service
client = Client('http://localhost:8000/?wsdl')

# Appelez la méthode `pretraitement_de_texte()`
result = client.service.pretraitement_de_texte("Texte à traiter")

# Affichez le résultat
print(result)