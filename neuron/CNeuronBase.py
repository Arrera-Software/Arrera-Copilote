from abc import abstractmethod
from gestionnaire.gestion import gestionnaire

class neuronBase :
    def __init__(self,gestionnaire:gestionnaire):
        #Init objet
        self._gestionnaire = gestionnaire
        self._gestFNC = self._gestionnaire.getGestFNC()
        self._gestGUI = self._gestionnaire.getGestGUI()
        self._gestHist = self._gestionnaire.getGestHist()
        self._userConf = self._gestionnaire.getUserConf()
        self._objHistorique = None
        self._listSortie = ["",""]
        self._socket = self._gestionnaire.getSocketObjet()
        self._language = self._gestionnaire.getLanguageObjet()
        self._keyword = self._gestionnaire.getKeywordObjet()
        self._valeurOut = 0

    def getListSortie(self)->list:
        return self._listSortie

    def getValeurSortie(self)->int :
        return self._valeurOut

    @abstractmethod
    def neurone(self,requette:str):
        pass