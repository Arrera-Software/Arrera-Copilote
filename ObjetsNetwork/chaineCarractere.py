class chaine :
    def netoyage(chaine):
        chaine = str(chaine)
        chaine.replace("-"," ")
        chaine.replace('"'," ")
        chaine.replace("_"," ")
        chaine.replace('/'," ")
        chaine.replace("é","e")
        chaine.replace("è","e")
        chaine.replace("à","a")
        chaine.replace("ç","c")
        return chaine.lower()
    
    def firstMots(chaine:str,liste:list):
        listeMots = liste
        indexMin = float('inf')
        motsMin = ""
        for mots in listeMots:
            index = chaine.find(mots)
            if index != -1 and index < indexMin:
                indexMin = index
                motsMin = mots

        return motsMin