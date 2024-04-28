import requests
import geocoder

class Actu :
    def __init__(self,keyActu:str,nbPage:int,pay:str,lang:str):
        self.__nbPage = int(nbPage)
        self.__pay = pay
        self.__keyActu = keyActu
        self.__langue = lang
        self.__URLActu = "https://newsapi.org/v2/top-headlines?"+"apiKey="+self.__keyActu+"&country="+self.__pay+"&category=general"+"&pageSize="+str(self.__nbPage)+"&language="+self.__langue
        
    def Actu(self):
        retourActu = requests.get(self.__URLActu).json()["articles"]
        listeDescription = []
        for i in range(0,self.__nbPage) :
            listeDescription.append(retourActu[i]["title"])
        
        return listeDescription
    
    
class Meteo : 
    def __init__(self,keyAPI : str):
        self.__keyApi= keyAPI
        self.__url="https://api.openweathermap.org/data/2.5/weather?"
        
        self.__temperature = ""
        self.__humiditer =  ""
        self.__description =  ""
        self.__icon =  ""
    
    def recuperationDataMeteo(self,latitude:str,longitude:str):
        self.__latitude = latitude
        self.__longitude = longitude
        reponse=requests.get(self.__url+"lat="+str(self.__latitude)+"&lon="+str(self.__longitude)+"&lang=fr&units=metric&appid="+self.__keyApi).json()
        if reponse["cod"] == "401" or reponse["cod"] == "400" :
            return False
        else :
            reponseData = reponse["main"]
            reponseDescription = reponse["weather"][0]
            self.__temperature = str(reponseData["temp"])
            self.__humiditer =  str(reponseData["humidity"])
            self.__description =  str(reponseDescription["description"])
            self.__icon =  str(reponseDescription['icon'])
            return True
            
       
    def gettemperature(self):#permet de recuperé la temperature
        return self.__temperature
    
    def gethumiditer(self):#permet de recuperé le taux d'humiditer en %
       return self.__humiditer
    
    def getdescription(self):#permet de recuperé la description de temp en fr
        return self.__description
        
    def geticon(self):
        return self.__icon