import webbrowser as w

class CHsearchDoc :
    def __init__(self):
        self.__lienDevDoc = "https://devdocs.io/#q="
        self.__lienMicrosoft = "https://learn.microsoft.com/en-us/search/?terms="
        self.__lienPython = "https://www.python.org/search/?q="

    def rechercheDevDoc(self,recherche:str)->bool:
        url = self.__lienDevDoc+recherche
        return w.open(url)
    
    def rechercheMicrosoft(self,recherche:str)->bool:
        url = self.__lienMicrosoft+recherche
        return w.open(url)
    
    def recherchePython(self,recherche:str):
        url = self.__lienPython+recherche
        return w.open(url)