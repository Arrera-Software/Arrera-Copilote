from neuron.CNeuronBase import neuronBase


class neuroneCodehelp(neuronBase) :

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getCodeHelp():
            if "ouvre" in requette:
                if ("organisateur de variable" in requette)or("orga var" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenOrgaVar(), ""]
                    self._objHistorique.setAction("Ouverture organisateur de varriable")
                    self._valeurOut = 5
                elif (("color selecteur" in requette) or ("couleur selecteur" in requette)
                        or ("selecteur de couleur" in requette)):
                    self._listSortie=[self._fonctionArreraNetwork.sortieOpenColorSelecteur(), ""]
                    self._objHistorique.setAction("Ouverture selecteur de couleur")
                    self._valeurOut = 5
                elif "site github" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenSiteGithub(), ""]
                    self._objHistorique.setAction("Ouverture du site github")
                elif ("gestion github" in requette) or ("gest github" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenGuiGithub(), ""]
                    self._objHistorique.setAction("Ouverture de logiciel de gestion github")
                    self._valeurOut = 5
                elif "librairy" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenLibrairy(), ""]
                    self._objHistorique.setAction("Ouverture de la librairy codehelp")
                    self._valeurOut = 5
            elif ("recherche devdoc" in requette or "rdevdoc" in requette or
                  "sdevdoc" in requette or "recherche microsoft" in requette or
                  "rmicrosoft" in requette or "smicrosoft" in requette or
                  "recheche python" in requette or "rpython" in requette or
                  "spython" in requette):
                text , recherche = self._fonctionArreraNetwork.sortieSearchDoc(requette)
                self._listSortie = [text, ""]
                self._objHistorique.setAction("Recherche documentation " + recherche)
            elif (("recherche github" in requette) or ("rgithub" in requette) or
                    ("sgithub" in requette) or ("search github" in requette)):
                text,recherche = self._fonctionArreraNetwork.sortieSearchGithub(requette)
                self._listSortie = [text, ""]
                self._objHistorique.setAction("Recherche github " + recherche)

            
            #Mise a jour de la valeur
            if self._valeurOut == 0:
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])