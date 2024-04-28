import geocoder
import requests
import webbrowser
import platform
import os
import subprocess

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
    
class GPSItineraires :
    def __init__(self):
        os = platform.system()
        if os == "Windows":
           self.__chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        else :
            if os == "Linux":
                self.__chrome = "/usr/bin/google-chrome"
        
        self.__baseURL = "https://www.google.fr/maps/dir/"
                
    def ouvertureItineraires(self,loc1:str,loc2:str):
        nameOS = platform.system()
        if nameOS == "Windows":
            try:
               # Vérifie si la clé de registre pour Google Chrome existe
               key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
               os.path.exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
               etat = True
            except:
                etat = False 
        else :
            if nameOS == "Linux":
                try:
                    # Exécute la commande "which" pour rechercher l'exécutable de Google Chrome
                    subprocess.check_output(["which", "google-chrome"])
                    etat = True
                except subprocess.CalledProcessError:
                    etat = False
            else :
                etat = False
        
        if etat == True :
            webbrowser.get(self.__chrome).open(self.__baseURL+loc1+"/"+loc2)
            return True
        else :
            return False