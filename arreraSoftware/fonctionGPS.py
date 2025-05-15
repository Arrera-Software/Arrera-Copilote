import geocoder
import requests
import webbrowser
import urllib.parse

class GPS:
    def __init__(self,KeyGPS:str,etatConnextion:bool):
        self.__url = "http://api.openweathermap.org/geo/1.0/"
        self.__key = KeyGPS
        if etatConnextion == True :
            self.__g = geocoder.ip('me')
        else :
            self.__g = ""
            
    def recuperationCordonneePossition(self):
        if self.__g.ok:
            self.loc = self.__g.latlng
            return True
        else:
            return False
    
    def getlatPossition(self):
        return str(self.loc[0])

    def getlonPossition(self):
        return str(self.loc[1]) 
    
    def recuperationCordonneeVille(self,ville:str):
        reponse = requests.get(self.__url+"direct?q="+ville+"&appid="+self.__key+"&limit=1")
        if reponse.status_code == 400 :
            return False
        else :
            self.loc = reponse.json()[0]
            return True
    
    def getlatVille(self):
        return self.loc["lat"]

    def getLonVille(self):
        return self.loc["lon"]  
    
    def recuperationNameVillePosition(self):
        reponse = requests.get(self.__url+"reverse?"+"lat="+str(self.loc[0])+"&lon="+str(self.loc[1])+"&appid="+self.__key)
        if reponse.status_code == 400 :
            return False
        else :
            self.nameVille = reponse.json()[0]["name"]
            return True
    
    def getNameVille(self):
        return self.nameVille
    
    def launchGoogleMapItineraire(self,depart:str, arrivee:str):
        """
        Lance un itinéraire Google Maps depuis l'adresse de départ jusqu'à l'adresse d'arrivée.
        
        Parameters:
        depart (str): Adresse de départ en langage naturel.
        arrivee (str): Adresse d'arrivée en langage naturel.
        """
        if (depart!="" and arrivee!=""):
            base_url = "https://www.google.com/maps/dir/?api=1"
            params = {
                "origin": depart,
                "destination": arrivee
            }
            
            # Encoder les paramètres pour les inclure dans l'URL
            url_params = urllib.parse.urlencode(params)
            full_url = f"{base_url}&{url_params}"
            
            # Ouvrir l'URL dans le navigateur par défaut
            return webbrowser.open(full_url)
        else :
            return False