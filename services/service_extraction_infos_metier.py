from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
import re
class ServiceExtractionInfosMetier(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def pretraitement_de_texte(ctx, texte):
        # Split the text into a list of lines
        lines = texte.split("\n")

        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Iterate through each line and extract the text after ":"
        for line in lines:
            parts = line.split(":")
            if len(parts) == 2:
                extracted_text += parts[1].strip() + "\n"
        
        splittedText = extracted_text.split("\n")
        montantPret = splittedText[4]
        chiffres = re.sub(r"[^0-9]", "", montantPret)
        splittedText[4] = chiffres
        
        dureePret= splittedText[5]
        chiffres = re.sub(r"[^0-9]", "", dureePret)
        splittedText[5] = chiffres
        
        revenuMensuel = splittedText[7]
        chiffres = re.sub(r"[^0-9]", "", revenuMensuel)
        splittedText[7] = chiffres  
        
        depensesMensuelles = splittedText[8]
        chiffres = re.sub(r"[^0-9]", "", depensesMensuelles)
        splittedText[8] = chiffres
        print(splittedText )

        print(extracted_text + "yoooooooooooooooooooooow")
        #on remet tout dans un string
        extracted_text = ""
        for i in range(len(splittedText)):
            extracted_text += splittedText[i] + "\n"
            
        return extracted_text
