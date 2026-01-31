from fnc.fncBase import fncBase,gestionnaire
import webbrowser as wb
# Codehelp
from objet.CHsearchDoc import CHsearchDoc
from gui.codehelp.CHGithub import CHGithub
from gui.codehelp.CHLibrairy import CHLibrairy
from gui.codehelp.CHOrgraVarriable import CHOrgraVarriable
from gui.codehelp.CCHcolorSelector import CCHcolorSelector

class fncCodehelp(fncBase) :
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)
        self.__orgaVar = CHOrgraVarriable(gestionnaire)
        self.__searchDoc = CHsearchDoc()
        self.__colorSelector = CCHcolorSelector(gestionnaire)
        self.__githubObjet = CHGithub(gestionnaire)
        self.__librairyCodehelp = CHLibrairy(gestionnaire)
        self.__guiLaunch = ""

    def searchDocInDevDoc(self, recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchDevDoc(recherche)
        else :
            return False

    def searchDocInMicrosoft(self,recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchMicrosoft(recherche)
        else :
            return False

    def searchDocInPython(self,recherche:str)->bool:
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__searchDoc.searchPython(recherche)
        else :
            return False

    def searchGithub(self, requette: str):
        if self._gestionnaire.getNetworkObjet().getEtatInternet():
            return self.__githubObjet.search(requette)
        else :
            return False

    def setGUICodeHelp(self,gui:str):
        """
        GUIColorSelector
        GUIGithubGestion
        GUILibrairy
        GUIOrgaVar
        """
        self.__guiLaunch = gui

    def launchGui(self):
        """
        GUIColorSelector
        GUIGithubGestion
        GUILibrairy
        GUIOrgaVar
        """
        if self.__guiLaunch == "GUIColorSelector":
            self.__colorSelector.active()
            return True
        elif self.__guiLaunch == "GUIGithubGestion":
            self.__githubObjet.active()
            return True
        elif self.__guiLaunch == "GUILibrairy":
            self.__librairyCodehelp.active()
            return True
        elif self.__guiLaunch == "GUIOrgaVar":
            self.__orgaVar.active()
            return True
        else :
            return False


    def openSiteGithub(self):
        wb.open("https://github.com/")

    def openGUIColorSelector(self):
        self.__colorSelector.active()

    def openGUIGithubGestion(self):
        self.__githubObjet.active()

    def openGUILibrairy(self):
        self.__librairyCodehelp.active()

    def openGUIOrgaVar(self):
        self.__orgaVar.active()