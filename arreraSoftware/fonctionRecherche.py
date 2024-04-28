import webbrowser
import requests
import time
from translate import*


class fncArreraSearch :
    def __init__(self,etatConnextion:bool):
        self.__etatConnexion = etatConnextion
        
    
    def braveSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://search.brave.com/search?q='
            urllink = requests.get(url+query+"&source=web")
            lienBrave = urllink.url
            webbrowser.open(lienBrave)
            return True
        else :
            return False

    def AmazonSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://www.amazon.fr/s?k='
            urllink = requests.get(url+query)
            lienAmazon = urllink.url
            webbrowser.open(lienAmazon)
            return True
        else :
            return False

    def googleSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://www.google.com/search?q'
            query = {'q': query}
            urllink = requests.get(url, params=query)
            liengoogle = urllink.url
            webbrowser.open(liengoogle)
            return True
        else :
            return False

    def duckduckgoSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://duckduckgo.com/?q='
            lienduck = url+query
            webbrowser.open(lienduck) 
            return True
        else :
            return False 

    def QwantSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://www.qwant.com/?l=fr&q'
            query = {'q': query}
            urllink = requests.get(url, params=query)
            lienQwant = urllink.url
            webbrowser.open(lienQwant)
            return True
        else :
            return False


    def EcosiaSearch(self,query:str):
        if self.__etatConnexion == True :
            url = 'https://www.ecosia.org/search'
            query = {'q': query}
            urllink = requests.get(url,query)
            lienEcosia = urllink.url
            webbrowser.open(lienEcosia) 
            return True
        else :
            return False

    def bingSearch(self,query:str):
        if self.__etatConnexion == True :
            url = "https://www.bing.com/search"
            query = {'q': query}
            urllink = requests.get(url, params=query)
            lienbing = urllink.url
            webbrowser.open(lienbing)
            return True
        else :
            return False
    
    def GrandRecherche(self,query:str):
        if self.__etatConnexion == True :
            i = 0
            while(i!=7):
                if (i==1) :
                    self.googleSearch(query)
                    time.sleep(1.5)
                else :
                    if (i==2):                
                        self.QwantSearch(query)
                        time.sleep(1.5)
                    else :
                        if(i==3):
                            self.duckduckgoSearch(query)
                            time.sleep(1.5)
                        else :
                            if(i==4):
                                self.EcosiaSearch(query)
                                time.sleep(1.5)
                            else :
                                if(i==5):
                                    self.braveSearch(query)
                                    time.sleep(1.5)
                                else :
                                    if(i==6):
                                        self.bingSearch(query)
                                        time.sleep(1.5)
                i = i + 1
            return True
        else :
            return False