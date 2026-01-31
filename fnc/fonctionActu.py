import requests
from fnc.fncBase import fncBase,gestionnaire

class fncActualiter(fncBase) :
    def __init__(self,gestionnaire:gestionnaire,keyActu:str):
        super().__init__(gestionnaire)
        self.__keyActu = keyActu
        self.__nbPage = 0
        self.__URLbase = "https://newsapi.org/v2/everything?apiKey="
        self.__articles = []

    def setActu(self,nbPage:int,lang:str):
        listFlag = ["&language="+lang,
                    "&pageSize="+str(nbPage),"&q=France"]
        try :
            jsonActu = requests.get(self.__URLbase+self.__keyActu+
                                         listFlag[0]+
                                         listFlag[1]+
                                         listFlag[2]).json()
            sortieRequest = jsonActu["status"]
            nomResute = jsonActu["totalResults"]
            if sortieRequest== "ok" and nomResute != 0:
                self.__nbPage = int(nbPage)
                self.__articles = jsonActu["articles"]
                return True
            else :
                self.__nbPage = 0
                return False
        except requests.exceptions.RequestException as e:
            # print(f"Erreur lors de la requête : {e}")
            self.__nbPage = 0
            return False


    def getActu(self):
        if self.__nbPage!=0:
            listeDescription = []
            retourActu = self.__articles
            for i in range(0,self.__nbPage) :
                listeDescription.append(retourActu[i]["title"])
            return listeDescription
        else :
            return ["error","error"]