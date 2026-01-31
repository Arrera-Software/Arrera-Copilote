import re
from neuron.CNeuronBase import *


class neuroneChatbot(neuronBase) :
    def __init__(self, gestionnaire:gestionnaire):
        #Init objet
        super().__init__(gestionnaire)
        # self.__formule = self._gestNeuro
        self.__language = self._gestionnaire.getLanguageObjet()
        self.__gestIA = self._gestionnaire.getGestIA()
        self.__gestIA.loadIA()

    def __clear_out_ia(self,texte:str):
        texte = texte.replace("\n\n", "\n").replace("**","")
        texte = "\n".join(ligne for ligne in texte.split("\n") if ligne.strip())
        texte = re.sub(r"\s{2,}", " ", texte)
        texte = "\n".join(ligne.strip() for ligne in texte.split("\n"))

        nb = len(texte)
        if nb >= 220:
            return [5,texte]
        else :
            return [1,texte]

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if not self._keyword.checkUtils(requette, "stop"):
            if self.__gestIA.get_ia_is_enable():
                if self.__gestIA.send_request_ia(requette):
                    if self.__gestIA.get_state_ia_reponse():
                        out_ia = self.__gestIA.get_reponse_ia()
                        out_clear = self.__clear_out_ia(out_ia)
                        if out_clear[0] == 5:
                            self._gestGUI.setGUIActive("aide",[out_clear[1],
                                                               self._language.getPhraseChatBot("1")])
                        else :
                            self._listSortie = [out_clear[1],""]
                        self._valeurOut = out_clear[0]
                    else :
                        self._valeurOut = 0
                else :
                    self._valeurOut = 0
            else :
                self._valeurOut = 0