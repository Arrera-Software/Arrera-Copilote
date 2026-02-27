import requests
class network:
    def __init__(self) :
        self.__etatConnexion = False

    def __check(self):
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        except Exception :
            self.__etatConnexion = False
    
    def getEtatInternet(self):
        self.__check()
        return self.__etatConnexion