from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneSearch:
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__gestNeuron = neuronGest
        self.__fonctionArreraNetwork = fncArreraNetwork

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        if self.__gestNeuron.getSearch() == True :
            #Initilisation des variable nbRand et text et valeur
            text = ""
            valeur = 0
            #reponse neuron search
            if "bigsearch" in requette or "grand recherche" in requette :
                text = self.__fonctionArreraNetwork.sortieGrandRecherche(requette)
            else :
                if "search" in requette or "recherche" in requette :
                    text = self.__fonctionArreraNetwork.sortieRechercheSimple(requette)    
            #Mise a jour de la valeur                                                               
            valeur = self.__gestionNeuron.verrifSortie(text)
            #Retour des valeur
            return valeur , text
        else :
            return 0 , ""
            