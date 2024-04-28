from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.chaineCarractere import *
from ObjetsNetwork.enabledNeuron import*

class neuroneTime :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest

    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        if self.__gestNeuron.getTime() == True :
            #Initilisation des variable nbRand et text et valeur
            text = ""
            valeur = 0
            #reponse neuron time
            if "heure" in requette :
                text = self.fonctionArreraNetwork.sortieHeure()
            else :
                if "date" in requette :
                    text = self.fonctionArreraNetwork.sortieDate()
                else :
                    if "chronometre" in requette or "chrono" in requette :
                        text = self.fonctionArreraNetwork.sortieOpenChrono()
                    else :
                        if "horloge" in requette :
                            text = self.fonctionArreraNetwork.sortieOpenHorloge()
                        else :
                            if "minuteur" in requette :
                                text = self.fonctionArreraNetwork.sortieOpenSimpleMinuteur()
                            else :
                                if "ajouter un rendez-vous" in requette or "ajout un rendez-vous"  in requette or "ajout evenement" in requette or "ajout rappel" in requette or "ajout un evenement" in requette or "ajout un rappel" in requette or "ajouter un evenement" in requette or "ajouter  un rappel" in requette:
                                    text = self.fonctionArreraNetwork.sortieAjoutEvent()
                                else :
                                    if "suppr un rendez-vous" in requette or "supprimer un rendez-vous"  in requette or "suppr evenement" in requette or "suppr rappel" in requette or "suppr un evenement" in requette or "suppr un rappel" in requette or "supprimer un evenement" in requette or "supprimer un rappel" in requette:
                                        text = self.fonctionArreraNetwork.sortieSupprEvent()
                                    else :
                                        if "evenement d'aujourd'hui" in requette or "evenement du jour" in requette or "rendez-vous d'aujourd'hui" in requette or "rappel aujourd'hui" in requette:
                                            text = self.fonctionArreraNetwork.sortieEvenementDay()
                                        
                
            #Mise a jour de la valeur                                                               
            valeur = self.__gestionNeuron.verrifSortie(text)
            #Retour des valeur
            return valeur , text
        else :
            return 0 , ""