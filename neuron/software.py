from neuron.CNeuronBase import *

class neuroneSoftware(neuronBase) :

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getSoftware():
            #reponse neuron software
            if "telecharge" in requette:
                if "video" in requette :
                    self._listSortie = [self._fonctionArreraNetwork.sortieDownloadVideo(), ""]
                    self._valeurOut = 5
                    self._objHistorique.setAction("Ouverture du logiciel de telechargement en mode video")
                elif "musique" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieDownloadMusic(), ""]
                        self._valeurOut = 5
                        self._objHistorique.setAction("Ouverture du logiciel de telechargement en mode musique")
                else :
                    self._listSortie = [self._fonctionArreraNetwork.sortieNoDownload(), ""]

            if ("calculatrice" in requette) or ("calculette" in requette):
                if "nombre complex" in requette or "nb complex" in requette :
                    self._listSortie = [self._fonctionArreraNetwork.sortieCalculatrice("1"), ""]
                    self._objHistorique.setAction("Ouverture de la calculatrice en mode nombre complex")
                    self._valeurOut = 5
                elif "pythagore" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieCalculatrice("2"), ""]
                        self._objHistorique.setAction("Ouverture de la calculatrice en mode pythagore")
                        self._valeurOut = 5
                else :
                    self._listSortie = [self._fonctionArreraNetwork.sortieCalculatrice("0"), ""]
                    self._objHistorique.setAction("Ouverture de la calculatrice")
                    self._valeurOut = 5
                    
                                        
            #Mise a jour de la valeur 
            if (self._valeurOut==0):
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])