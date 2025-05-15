from neuron.CNeuronBase import *

class neuroneTime(neuronBase):

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0
        if self._gestNeuron.getTime() == True :
            #reponse neuron time
            if ((("resumer" in requette) and ("tache" in requette)) or
                    (("resumer" in requette) and ("agenda" in requette))):
                    nb,listout = self._fonctionArreraNetwork.sortieResumerTacheAgenda()
                    self._listSortie = listout
                    self._valeurOut = nb
                    self._objHistorique.setAction("Resumer des tache et des evenement du jour")
            elif self.__neuronTime(requette) == 1:
                if (self._valeurOut==0):
                    self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])
            elif self.__neuronAgenda(requette) == 1:
                if (self._valeurOut==0):
                    self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])
            elif self.neuronTache(requette) == 1:
                if (self._valeurOut==0):
                    self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])

    def __neuronTime(self,requette:str):
        if ("heure" in requette) :
            self._listSortie = [self._fonctionArreraNetwork.sortieHeure(), ""]
            self._valeurOut = 1
            return 1
        elif ("date" in requette) :
            self._listSortie = [self._fonctionArreraNetwork.sortieDate(), ""]
            self._valeurOut = 1
            return 1
        elif ("chronometre" in requette or "chrono" in requette):
            self._listSortie = [self._fonctionArreraNetwork.sortieOpenChrono(), ""]
            self._valeurOut = 5
            return 1
        elif ("horloge" in requette) :
            self._listSortie = [self._fonctionArreraNetwork.sortieOpenHorloge(), ""]
            self._valeurOut = 5
            return 1
        elif ("minuteur" in requette) :
            self._listSortie = [self._fonctionArreraNetwork.sortieOpenSimpleMinuteur(), ""]
            self._valeurOut = 5
            return 1
        else :
            return 0

    def __neuronAgenda(self,requette:str): # Rendez-vous
        if "evenement" in requette or "agenda" in requette or "rendez vous" in requette or "rappel" in requette:
            if "ajoute" in requette or "ajouter" in requette or "add" in requette or "ajout" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieAjoutEvent(), ""]
                self._objHistorique.setAction("Ajout d'un rendez-vous dans l'agenda")
                self._valeurOut = 5
                return 1
            elif "supprime" in requette or "supprimer" in requette or "suppr" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieSupprEvent(), ""]
                self._objHistorique.setAction("Suppression d'un rendez-vous dans l'agenda")
                self._valeurOut = 5
                return 1
            elif ("montre" in requette or "fais voir" in requette) and ("aujourd'hui" in requette or "jour" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieEvenementDay(), ""]
                self._objHistorique.setAction("Consulation des rendez-vous enregistrer dans l'agenda")
                self._valeurOut = 5
                return 1
            elif "montre" in requette or "ouvre" in requette or "fais voir" in requette :
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenAgenda(), ""]
                self._objHistorique.setAction("Ouverture de l'interface agenda")
                self._valeurOut = 5
                return 1
            else :
                return 0
        else :
            return 0

    def neuronTache(self,requette:str):
        if ("taches" in requette or "tache" in requette) and "projet" not in requette:
            if ("montre" in requette or "fais voir" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTache(), ""]
                self._objHistorique.setAction("Consulation des taches enregistrer")
                self._valeurOut = 5
                return 1
            elif ("ajoute" in requette or "ajouter" in requette
                  or "ajout" in requette or "add" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheAdd(), ""]
                self._objHistorique.setAction("Ajout d'une tache dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("supprime" in requette or "supprimer" in requette or "suppr" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheSuppr(), ""]
                self._objHistorique.setAction("Suppression d'une tache dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("finir" in requette or "terminer" in requette or "termine" in requette or "fini" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieViewTacheCheck(), ""]
                self._objHistorique.setAction("Mise d'une tache a fini dans l'assistant")
                self._valeurOut = 5
                return 1
            elif ("dit moi" in requette) and (("nombre" in requette) or ("combien" in requette)):
                if  (("jour" in requette) or ("aujourd'hui" in requette)) :
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheToday(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour aujourd'hui")
                    self._valeurOut = 1
                    return 1
                elif ("demain" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieSpeakTacheTowmorow(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer pour demain")
                    self._valeurOut = 1
                    return 1
                else :
                    self._listSortie = [self._fonctionArreraNetwork.sortieNbSpeakTache(), ""]
                    self._objHistorique.setAction("Consultation du nombre de tache enregistrer")
                    self._valeurOut = 1
                    return 1
            else :
                return 0
        else:
            return 0