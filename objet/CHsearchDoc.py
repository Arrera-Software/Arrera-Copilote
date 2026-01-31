import webbrowser as w

class CHsearchDoc :
    def __init__(self):
        self.__lienDevDoc = "https://devdocs.io/#q="
        self.__lienMicrosoft = "https://learn.microsoft.com/en-us/search/?terms="
        self.__lienPython = "https://www.python.org/search/?q="

    def searchDevDoc(self, recherche:str)->bool:
        if recherche == "":
            return False
        url = self.__lienDevDoc+recherche
        return w.open(url)
    
    def searchMicrosoft(self, recherche:str)->bool:
        if recherche == "":
            return False
        url = self.__lienMicrosoft+recherche
        return w.open(url)
    
    def searchPython(self, recherche:str):
        if recherche == "":
            return False
        url = self.__lienPython+recherche
        return w.open(url)