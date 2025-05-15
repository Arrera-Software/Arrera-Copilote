import requests
from datetime import datetime, timedelta

class Actu :
    def __init__(self,keyActu:str):
        self.__keyActu = keyActu
        self.__nbPage = 0
        self.__URLbase = "https://newsapi.org/v2/everything?apiKey="

    def setActu(self,nbPage:str,lang:str):
        listFlag = ["&language="+lang,
                    "&pageSize="+nbPage,"&q=France"]
        self.__jsonActu = requests.get(self.__URLbase+self.__keyActu+
                                     listFlag[0]+
                                     listFlag[1]+
                                     listFlag[2]).json()
        sortieRequest = self.__jsonActu["status"]
        nomResute = self.__jsonActu["totalResults"]
        if (sortieRequest=="ok" and nomResute != 0):
            self.__nbPage = int(nbPage)
            return True
        else :
            self.__nbPage = 0
            return False


    def getActu(self):
        if (self.__nbPage!=0):
            listeDescription = []
            retourActu = self.__jsonActu["articles"]
            for i in range(0,self.__nbPage) :
                listeDescription.append(retourActu[i]["title"])
            return listeDescription
        else :
            return ["error","error"]
    
    
class Meteo : 
    def __init__(self,keyAPI : str):
        self.__keyApi= keyAPI
        self.__url="https://api.openweathermap.org/data/2.5/"
        
        self.__temperature = ""
        self.__humiditer =  ""
        self.__description =  ""
        self.__icon =  ""
    
    def getDataMeteoNow(self,latitude:str,longitude:str):
        self.__latitude = latitude
        self.__longitude = longitude
        reponse=requests.get(self.__url+"weather?lat="+str(self.__latitude)+"&lon="+str(self.__longitude)+"&lang=fr&units=metric&appid="+self.__keyApi).json()
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

    def getDateMetoTowmorowMorning(self,latitude:str,longitude:str):
        self.__latitude = latitude
        self.__longitude = longitude
        reponse=requests.get(self.__url+"forecast?lat="+str(self.__latitude)+"&lon="+str(self.__longitude)+"&lang=fr&units=metric&appid="+self.__keyApi).json()
        if reponse["cod"] == "401" or reponse["cod"] == "400" :
            return False
        else :
            tomorrow = (datetime.now() + timedelta(days=1)).date()
            # Filtrer les prévisions pour demain midi
            forecast_tomorrow_noon = [
                forecast for forecast in reponse['list']
                if datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == tomorrow and
                datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').hour == 9
            ]

            # Afficher les prévisions pour demain midi
            for forecast in forecast_tomorrow_noon:
                reponseData = forecast['main']
                reponseDescription = forecast['weather'][0]
                self.__temperature = str(reponseData["temp"])
                self.__humiditer =  str(reponseData["humidity"])
                self.__description =  str(reponseDescription["description"])
                self.__icon =  str(reponseDescription['icon'])
            return True
    
    def getDateMetoTowmorowNoon(self,latitude:str,longitude:str):
        self.__latitude = latitude
        self.__longitude = longitude
        reponse=requests.get(self.__url+"forecast?lat="+str(self.__latitude)+"&lon="+str(self.__longitude)+"&lang=fr&units=metric&appid="+self.__keyApi).json()
        if reponse["cod"] == "401" or reponse["cod"] == "400" :
            return False
        else :
            tomorrow = (datetime.now() + timedelta(days=1)).date()
            # Filtrer les prévisions pour demain midi
            forecast_tomorrow_noon = [
                forecast for forecast in reponse['list']
                if datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == tomorrow and
                datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S').hour == 12
            ]

            # Afficher les prévisions pour demain midi
            for forecast in forecast_tomorrow_noon:
                reponseData = forecast['main']
                reponseDescription = forecast['weather'][0]
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