from ObjetsNetwork.gestion import*
from arreraSoftware.fncArreraNetwork import*
from ObjetsNetwork.enabledNeuron import*
class neuroneService :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork,neuronGest:GestArreraNeuron) :
        #Init objet
        self.__gestionNeuron = gestionnaire
        self.__fonctionArreraNetwork = fncArreraNetwork
        self.__gestNeuron = neuronGest
        
    def neurone(self,requette:str,oldSortie:str,oldRequette:str):
        if self.__gestNeuron.getService() == True :
            #Initilisation des variable nbRand et text et valeur
            text = ""
            valeur = 0
            #Recuperation atribut de l'assistant
            self.__etatVous = self.__gestionNeuron.getVous()
            self.__genre = self.__gestionNeuron.getGenre()
            self.__user = self.__gestionNeuron.getUser()
            #reponse du neuron main
            if "lire un truc" in requette or  "lit un truc" in requette :
                text = self.__fonctionArreraNetwork.reading()
            else :
                if "calcule" in requette :
                    requette = requette.replace("calcule","")
                    requette = requette.replace(" ","")
                    if "1" in requette or "2" in requette  or "3" in requette or "4" in requette or "5" in requette or "6" in requette  or "7" in requette or "8" in requette or "9" in requette or "0" in requette and "+" in requette or "-" in requette or "*" in requette or "/" in requette :
                        resultat =  eval(requette)
                        if self.__etatVous == True :
                            text = "Voici le resultat de votre calcule "+self.__genre+" est "+str(resultat)
                        else :
                            text = "Voici le resultat de ton calcule "+self.__user+" est "+str(resultat)
                    else :
                        if self.__etatVous == True :
                            text = "Le calcule que vous me demander de faire "+self.__genre+" est imposible a faire."
                        else :
                            text = "Le calcule que tu me demande de faire est imposible."
            #Mise a jour de la valeur                                                               
            valeur = self.__gestionNeuron.verrifSortie(text)
            #Retour des valeur
            return valeur , text
        else :
            return 0 , ""