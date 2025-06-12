from neuron.CNeuronBase import *

class neuroneService(neuronBase) :
        
    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getService():
            #reponse du neuron main
            if (("lire" in requette or "lit" in requette or "lis" in requette) and
                    ("passage" in requette or "truc" in requette or "cela" in requette or
                     "texte" in requette or "article" in requette)) :
                self._listSortie = [self._fonctionArreraNetwork.reading(), ""]
                self._objHistorique.setAction("Lecture")
                self._valeurOut = 5
            elif "calcule" in requette :
                    requette = requette.replace("calcule","")
                    requette = requette.replace(" ","")
                    if (("1" in requette) or ("2" in requette)  or ("3" in requette) 
                        or ("4" in requette) or ("5" in requette) or ("6" in requette)  
                        or ("7" in requette) or ("8" in requette) or ("9" in requette) 
                        or( "0" in requette) and ("+" in requette) or ("-" in requette) 
                        or ( "*" in requette) or ("/" in requette)) :
                        resultat =  eval(requette)
                        self._listSortie = [self._fonctionArreraNetwork.sortieResultatCalcule(resultat), ""]
                        self._objHistorique.setAction("Calcule par texte")
                    else :
                        self._listSortie = [self._fonctionArreraNetwork.sortieErrorCalcule(), ""]
            elif ("ouvre la documentation" in requette)or("montre la documentation" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenDocumentation(), ""]
                    webbrowser.open(self._gestionNeuron.getLinkDoc())
            elif "corrige" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieCorrection(requette), ""]

            #Mise a jour de la valeur
            if self._valeurOut==0:
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])