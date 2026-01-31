from fnc.fncBase import fncBase,gestionnaire
from pyradios import RadioBrowser
import threading as th
import vlc

class fncRadio(fncBase) :
    def __init__(self, gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__etatNetwork = self._gestionnaire.getNetworkObjet().getEtatInternet()
        if self.__etatNetwork:
            self.__rdBrowser = RadioBrowser()
        self.__stations = []
        self.__player = None
        self.__isRunning = False
        self.__thread = None

    def __searchRadio(self, radio):
        self.__stations = []
        self.__stations = self.__rdBrowser.search(name=radio, country="France")
        return bool(self.__stations)

    def getRadioRunning(self):
        return self.__isRunning

    def __launchRadioThread(self):
        if not self.__isRunning and self.__stations and self.__etatNetwork:
            try :
                url = self.__stations[0]['url']
                self.__player = vlc.MediaPlayer(url)
                self.__isRunning = True
                self.__player.play()
            except Exception as e :
                print(f"Erreur lors de la lecture de la radio : {e}")
                self.__isRunning = False
                self.__player = None

    def __launchRadio(self):
        if not self.__isRunning:
            self.__thread = th.Thread(target=self.__launchRadioThread)
            self.__thread.start()

    def stop(self):
        if self.__player and self.__isRunning:
            self.__player.stop()
            self.__player = None
            self.__isRunning = False
            if self.__thread:
                self.__thread.join(timeout=1)
                return True
            else:
                return False
        else :
            return False

    
    def startEurope1(self):
        if self.__etatNetwork:
            if self.__searchRadio("Europe 1"):
                self.__launchRadio()
                return True
            else:
                return False
        else :
            return False
       
    def startEurope2(self):
        if self.__etatNetwork:
            if self.__searchRadio("Europe 2"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFranceInfo(self):
        if self.__etatNetwork:
            if self.__searchRadio("France Info"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFranceInter(self):
        if self.__etatNetwork:
            if self.__searchRadio("France inter"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFranceMusique(self):
        if self.__etatNetwork:
            if self.__searchRadio("France Musique"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFranceCulture(self):
        if self.__etatNetwork:
            if self.__searchRadio("France Culture"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFranceBleu(self):
        if self.__etatNetwork:
            if self.__searchRadio("France bleu"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startFunRadio(self):
        if self.__etatNetwork:
            if self.__searchRadio("Fun radio"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startNRJ(self):
        if self.__etatNetwork:
            if self.__searchRadio("NRJ"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startRFM(self):
        if self.__etatNetwork:
            if self.__searchRadio("RFM"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startNostalgi(self):
        if self.__etatNetwork:
            if self.__searchRadio("Nostalgie"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startSkyrock(self):
        if self.__etatNetwork:
            if self.__searchRadio("Skyrock"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False
    
    def startRTL(self):
        if self.__etatNetwork:
            if self.__searchRadio("RTL"):
                self.__launchRadio()
                return True
            else:
                return False
        else:
            return False