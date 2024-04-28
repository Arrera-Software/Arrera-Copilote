import json

class jsonWork : 
    def __init__(self,file):
        self.fichier = file
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)
    
    def lectureJSONMultiFlag(self,flag1,flag2):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag1][flag2]
        return str(dict)
    
    def lectureJSONList(self,flag):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            liste = json.load(openfile)[flag]
        return list(liste)
    
    def lectureJSONDict(self,flag):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dictionnaire = json.load(openfile)[flag]
        return dict(dictionnaire)
     
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict,writeFile,indent=2)
        
    def EcritureJSONList(self, flag, valeur):
        # Chargez le fichier JSON
        with open(self.fichier, 'r', encoding='utf-8') as openfile:
            data = json.load(openfile)
        # Vérifiez si le champ (flag) existe et est une liste
        if flag in data and isinstance(data[flag], list):
            # Ajoutez la nouvelle valeur à la liste
            data[flag].append(valeur)
            # Écrivez le fichier JSON mis à jour
            with open(self.fichier, 'w', encoding='utf-8') as writeFile:
                json.dump(data, writeFile, indent=2)
    
    def EcritureJSONDictionnaire(self, flag, cle, valeur):
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        if flag in data and isinstance(data[flag], dict):
            data[flag][cle] = valeur  # Met à jour le dictionnaire
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)
    
    def supprJSONList(self, flag, cle):
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)

        if flag in data and isinstance(data[flag], dict):
            if cle in data[flag]:
                del data[flag][cle]  # Supprime la clé spécifiée du dictionnaire
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)
    
    def suppressionJson(self, flag:str):
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)
        if flag in data:
            data[flag]="" # Supprime le champ spécifié
            with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                json.dump(data, fichier_modifie, indent=2)
    
    def suppressionJsonList(self, flag, valeur):
        with open(self.fichier, 'r', encoding='utf-8') as fichier_json:
            data = json.load(fichier_json)
        if flag in data and isinstance(data[flag], list):
            liste = data[flag]
            
            if valeur in liste:
                liste.remove(valeur)  # Supprime la valeur spécifiée de la liste
                with open(self.fichier, 'w', encoding='utf-8') as fichier_modifie:
                    json.dump(data, fichier_modifie, indent=2)

    def dictJson(self):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)
        return dict
       
    def compteurFlagJSON(self):
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        return len(dict)
    
    def supprDictReorg(self,flag):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)
            del dict[flag]
            newDict = {}
            newKey = 0
            for cle in sorted(dict.keys(), key=lambda x: int(x)):
                newDict[str(newKey)] = dict[cle]
                newKey += 1
            writeFile = open(self.fichier, 'w', encoding='utf-8')
            json.dump(newDict,writeFile,indent=2)
            writeFile.close()