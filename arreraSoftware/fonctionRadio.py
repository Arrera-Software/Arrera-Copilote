import webbrowser
from ObjetsNetwork.network import*

class fncRadio :
    def __init__(self,network:network):
        self.__etatNetwork = network.getEtatInternet()
    
    def startEurope1(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/europe-1/")
            return True
        else :
            return False
       
    def startEurope2(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/europe-2/")
            return True
        else :
            return False
    
    def startFranceInfo(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-info/")
            return True
        else :
            return False
    
    def startFranceInter(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-inter/")
            return True
        else :
            return False
    
    def startFranceMusique(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/france-musique/")
            return True
        else :
            return False
    
    def startFranceCulture(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-france-culture/ ")
            return True
        else :
            return False
    
    def startFranceBleu(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/france-bleu-ile-de-france/")
            return True
        else :
            return False
    
    def startFunRadio(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/fun-radio/")
            return True
        else :
            return False
    
    def startNRJ(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/nrj/")
            return True
        else :
            return False
    
    def startRFM(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/rfm/")
            return True
        else :
            return False
    
    def startNostalgi(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/radio-nostalgie/")
            return True
        else :
            return False
    
    def startSkyrock(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/skyrock/")
            return True
        else :
            return False
    
    def startRTL(self):
        if (self.__etatNetwork) :
            webbrowser.open("https://www.ecouter-en-direct.com/rtl/")
            return True
        else :
            return False