from abc import abstractmethod
from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.historique import*

class neuronBase :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique):
        #Init objet
        self._gestionNeuron = gestionnaire
        self._fonctionArreraNetwork = fncArreraNetwork
        self._gestNeuron = self._gestionNeuron.getEtatNeuronObjet()
        self._objHistorique = objHist
        self._listSortie = ["",""]
        self._socket = self._gestionNeuron.getSocketObjet()
        self._language = self._gestionNeuron.getLanguageObjet()
        self._valeurOut = 0

    def getListSortie(self)->list:
        return self._listSortie

    def getValeurSortie(self)->int :
        return self._valeurOut

    @abstractmethod
    def neurone(self,requette:str):
        pass