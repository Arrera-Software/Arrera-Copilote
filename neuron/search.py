from neuron.CNeuronBase import *

class neuroneSearch(neuronBase) :

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getSearch():
            #reponse neuron search
            if ("bigsearch" in requette)or ("grand recherche" in requette):
                text,recherche = self._fonctionArreraNetwork.sortieGrandRecherche(requette)
                self._listSortie = [text, ""]
                self._objHistorique.setAction("bigrecherche " + recherche)
                self._valeurOut = 1
            elif ("search" in requette) or ("recherche" in requette):
                if self._gestNeuron.getSocket() == True  and self._socket.getServeurOn() == True :
                    recherche = requette.replace("recherche","").strip()
                    self._socket.sendData("recherche " + recherche)
                    self._listSortie = [self._language.getPhraseSearch("4"),""]
                    self._valeurOut = 1
                else :
                    text,recherche = self._fonctionArreraNetwork.sortieRechercheSimple(requette)
                    self._listSortie = [text, ""]
                    self._objHistorique.setAction("recherche " + recherche)
                    self._valeurOut = 1