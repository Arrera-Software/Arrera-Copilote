from neuron.CNeuronBase import *

class neuronWork(neuronBase):

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0
        if self._gestNeuron.getWork():

            if self.__neuronTableur(requette) == 1:
                return
            elif self.__neuronProjet(requette) == 1:
                return
            elif self.__neuronWord(requette) == 1:
                return
            elif ((("comment" in requette) and ("utiliser" in requette)
                   and ("arrera work" in requette)) or ("aide work" in requette)):

                self._listSortie = ["Les fonction d'Arrera work sont :" +
                                     "\n- Edition tableur (Taper aide tableur)" +
                                     "\n- Edition fichier de traitement de texte (Taper aide word)" +
                                     "\n- Fonction Arrera projet (Taper aide projet)","work"]
                self._valeurOut = 17
            elif (("ouvert" in requette) and (("document" in requette) or
                ("tableur" in requette) or ("fichier" in requette) or ("word" in requette))):
                    self._listSortie = [self._fonctionArreraNetwork.sortieFileOpen(), ""]
                    self._valeurOut = 1

    def __neuronTableur(self,requette:str):
        if self._fonctionArreraNetwork.getTableurOpen() == False:
            if "ouvre" in requette and (("exel" in requette) or ("tableur" in requette) or ("excel" in requette)):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenTableur(), ""]
                self._objHistorique.setAction("Ouverture d'un fichier exel "+self._fonctionArreraNetwork.getFileTableur())
                self._valeurOut = 7
                return 1
            elif "aide tableur" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieHelpWorkTableur()
                    ,"tableur"]
                self._valeurOut = 17
                return 1
            else :
                return 0
        else :
            if "ouvre" in requette and (("exel" in requette or "tableur" in requette) and ("ordinateur" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenSoftTableurFile(), ""]
                    self._objHistorique.setAction("Ouverture du fichier tableur "+self._fonctionArreraNetwork.getFileTableur()+" sur l'ordinateur")
                    self._valeurOut = 1
                    return 1
            elif ("ferme" in requette) and(("exel" in requette) or ("tableur" in requette)):
                name = self._fonctionArreraNetwork.getFileTableur()
                self._listSortie = [self._fonctionArreraNetwork.sortieCloseTableur(), ""]
                self._objHistorique.setAction("Fermeture du fichier exel "+name)
                self._valeurOut = 8
                return 1
            elif ("lis" in requette) and ("liste" not in requette) and ("tableur" in requette):
                sortieTableur = self._fonctionArreraNetwork.sortieReadTableur()
                if sortieTableur[0] == "error":
                    self._valeurOut = 1
                    self._listSortie = self._fonctionArreraNetwork.sortieErrorReadTableur()
                else :
                    self._listSortie = sortieTableur
                    self._valeurOut = 13
                    self._objHistorique.setAction("Lecture du fichier tableur "+self._fonctionArreraNetwork.getFileTableur())
                return 1
            elif (("ajoute" in requette) or ("rajoute" in requette) or ("ajout" in requette)) and ("tableur" in requette):
                if "valeur" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddValeurTableur(), ""]
                    self._objHistorique.setAction("Ajout d'une valeur au tableur "+
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
                elif "somme" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddFormuleTableur(1), ""]
                    self._objHistorique.setAction("Ajout d'une formule somme au tableur " +
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
                elif "moyenne" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddFormuleTableur(2), ""]
                    self._objHistorique.setAction("Ajout d'une formule moyenne au tableur " +
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
                elif "comptage" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddFormuleTableur(3), ""]
                    self._objHistorique.setAction("Ajout d'une formule comptage au tableur " +
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
                elif "minimun" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddFormuleTableur(4), ""]
                    self._objHistorique.setAction("Ajout d'une formule minimun au tableur " + self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
                elif "maximun" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieAddFormuleTableur(1), ""]
                    self._objHistorique.setAction("Ajout d'une formule maximun au tableur " +
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return  1
                else :
                    return 0
            elif (("supprime" in requette) or ("suppr" in requette)) and (("tableur" in requette) or ("exel" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieSupprValeurTableur(), ""]
                    self._objHistorique.setAction("Suppression d'une valeur au tableur " +
                                                  self._fonctionArreraNetwork.getFileTableur())
                    self._valeurOut = 5
                    return 1
            elif "aide tableur" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieHelpWorkTableur()
                        ,"tableur"]
                    self._valeurOut = 17
                    return 1
            elif ("montre" in requette) and(("exel" in requette) or ("tableur" in requette)):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenTableurGUI(), ""]
                self._objHistorique.setAction("Ouverture du tableur " +
                                              self._fonctionArreraNetwork.getFileTableur() +
                                              " dans l'interface de l'assistant")
                self._valeurOut = 5
                return 1
            else :
                return 0

    def __neuronProjet(self,requette:str):
        oldRequette,oldSortie = self._gestionNeuron.getOld()

        if self._fonctionArreraNetwork.getProjectOpen() == False:
            if (("ouvre le projet nommer" in requette) or
                    ("ouvre le projet nomme" in requette) or
                    ("ouvre le projet" in requette)):
                projet,text = self._fonctionArreraNetwork.sortieOpenProjet(requette)
                self._listSortie = [text, ""]
                self._objHistorique.setAction("Ouverture du projet " + projet)
                self._valeurOut = 14
                return 1

            elif (("cree un projet nommer" in requette) or ("cree un nouveau projet nommer" in requette )
                  or ("cree un projet nomme" in requette) or ("cree un nouveau projet nomme" in requette)):
                self._listSortie = [self._fonctionArreraNetwork.sortieCreateFolder(requette), ""]
                self._objHistorique.setAction("Creation d'un projet nommer " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 10
                return 1

            elif "aide projet" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieHelpArreraWork()
                    ,"projet"]
                self._valeurOut = 17
                return 1

            elif "liste" in requette and "projet" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieListeProjet(),"liste projet"]
                self._valeurOut = 1
                return 1

            else :
                return 0

        elif ("ouvre" in requette) and ("projet" in requette) and ("nommer" in requette) and ("le" in requette):
            text,file = self._fonctionArreraNetwork.sortieOpenFileProject(requette)
            self._listSortie = [text, ""]
            if ("Il a peux être pas un projet ouvert." not in self._listSortie[0]):
                self._objHistorique.setAction("Ouverture du fichier "
                                              + file + " du projet " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 7
            else :
                self._valeurOut = 1
            return 1

        elif "aide projet" in requette:
            self._listSortie = [self._fonctionArreraNetwork.sortieHelpArreraWork()
                ,"projet"]
            self._valeurOut = 17
            return 1

        elif "cree un fichier" in requette:
            if ("nommer" in requette and (
                    ("word"in requette) or ("odt"in requette) or
                    ("txt"in requette) or ("python" in requette)
                    or ("json" in requette) or ("html" in requette) or
                    ("css" in requette) or("md" in requette) or
                    ("cpp" in requette) or ("exel" in requette) or
                    ("texte" in requette) or ("en tete" in requette)or
                    ("open texte document " in requette) or ("tableur" in requette)
                    or ("language c++" in requette) or ("php" in requette) or
                    ("javascript" in requette) or ("java script" in requette) or
                    ("js" in requette) or ("java" in requette) or
                    ("kotlin" in requette )or ("kt" in requette) or
                    ("postite" in requette) or ("ab" in requette))):
                self._listSortie = [self._fonctionArreraNetwork.sortieCreateFileDirect(requette), ""]
                self._objHistorique.setAction("Creation du fichier " + self._fonctionArreraNetwork.getNameLastFile() +
                                              " dans le projet " + self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 16
                return 1

        elif (("Voulez-vous l'ouvrir ?" in oldSortie or "Es que tu veux que je te l'ouvre ?" in oldSortie) and
              ("oui" in requette or "ouvre le" in requette or "vasy" in requette or "comme tu veux" in requette)):
            nameFile = self._fonctionArreraNetwork.getNameLastFile()
            self._listSortie = [self._fonctionArreraNetwork.sortieopenFileCreated(), ""]
            self._objHistorique.setAction("Ouverture du fichier " + nameFile + " du projet " +
                                          self._fonctionArreraNetwork.getNameProjetOpen())
            self._valeurOut = 7
            return 1

        elif (("liste" in requette) and ("fichier" in requette) and
              (("projet" in requette ) or ("project" in requette ))):
            self._listSortie = [self._fonctionArreraNetwork.sortieListFileProject(), ""]
            self._objHistorique.setAction("Liste de fichier du projet " +
                                          self._fonctionArreraNetwork.getNameProjetOpen())
            self._valeurOut = 1
            return 1
        elif ("taches" in requette or "tache" in requette) and "projet" in requette:
            if "montre" in requette or "fais voir" in requette or "ouvre" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieShowTacheProjet(), ""]
                self._objHistorique.setAction("Activation de l'interface des tache du projet " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 5
                return 1
            elif ("ajoute" in requette or "ajouter" in requette
                  or "ajout" in requette or "add" in requette) :
                self._listSortie = [self._fonctionArreraNetwork.sortieAddTacheProjet(), ""]
                self._objHistorique.setAction("Ajout d'une tache au projet " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 5
                return 1
            elif "supprime" in requette or "supprimer" in requette or "suppr" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieSupprTacheProjet(), ""]
                self._objHistorique.setAction("Suppression d'une tache au projet " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 5
                return 1
            elif "finir" in requette or "terminer" in requette or "termine" in requette or "fini" in requette:
                self._listSortie = [self._fonctionArreraNetwork.sortieSupprTacheProjet(), ""]
                self._objHistorique.setAction("Finnision d'une tache au projet " +
                                              self._fonctionArreraNetwork.getNameProjetOpen())
                self._valeurOut = 5
                return 1
            elif ("dit moi" in requette) and (("nombre" in requette) or ("combien" in requette)):
                if ("jour" in requette) or ("aujourd'hui" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieListeTacheTodayProjet(), ""]
                    self._objHistorique.setAction("Enumeration des taches du " +
                                                  self._fonctionArreraNetwork.getNameProjetOpen() + " pour aujourd'hui")
                    self._valeurOut = 1
                    return 1
                elif "demain" in requette:
                    self._listSortie = [self._fonctionArreraNetwork.sortieListTacheTowmorowProjet(), ""]
                    self._objHistorique.setAction("Enumeration des taches du " + self._fonctionArreraNetwork.getNameProjetOpen() + " pour demain")
                    self._valeurOut = 1
                    return 1
                else :
                    self._listSortie = [self._fonctionArreraNetwork.sortieNbTacheProjet(), ""]
                    self._objHistorique.setAction("Enumeration des taches du " +
                                                  self._fonctionArreraNetwork.getNameProjetOpen())
                    self._valeurOut = 1
                    return 1
            else :
                return 0

        elif ("Quelle est le type de projet ?" in oldSortie) and ("le type est" in requette):
            self._listSortie = [self._fonctionArreraNetwork.sortieSetTypeProjet(requette), ""]
            self._objHistorique.setAction("Mise en place d'un type au projet")
            self._valeurOut = 5
            return 1

        elif "le type du projet est" in requette:
            self._listSortie = [self._fonctionArreraNetwork.sortieSetTypeProjet(requette), ""]
            self._objHistorique.setAction("Mise en place d'un type au projet")
            self._valeurOut = 5
            return 1

        elif "ferme" in requette and "projet" in requette:
            nameProjet = self._fonctionArreraNetwork.getNameProjetOpen()
            self._listSortie = [self._fonctionArreraNetwork.sortieCloseProject(), ""]
            self._objHistorique.setAction("Fermeture du projet " + nameProjet)
            self._valeurOut = 21
            return 1

        elif "type fichier" in requette:
            self._listSortie = [self._fonctionArreraNetwork.sortieHelpWorkType()
                ,"fichier"]
            self._valeurOut = 17
            return 1
        else :
            return 0
        return 0

    def __neuronWord(self,requette:str):
        if (self._fonctionArreraNetwork.getWordOpen() == False):
            if (("ouvre" in requette) and (("word" in requette) or
                ("traitement de texte" in requette) or ("document" in requette))):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenWord(), ""]
                self._objHistorique.setAction("Ouverture d'un fichier word " +
                                              self._fonctionArreraNetwork.getFileWord())
                self._valeurOut = 7
                return 1
            elif ("aide word" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieHelpWorkTraitementTexte()
                    ,"word"]
                self._valeurOut = 17
                return 1
        else :
            if (("ouvre" in requette) and (("word" in requette)or
                                           ("traitement de texte" in requette)or (
                                                   "document" in requette))and ("ordinateur" in requette)):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenSoftWorkFile(), ""]
                self._objHistorique.setAction(
                    "Ouverture du fichier word " +
                    self._fonctionArreraNetwork.getFileWord() + " sur l'ordinateur"
                )
                self._valeurOut = 1
                return 1

            elif (("ferme" in requette)and (("word" in requette)or ("traitement de texte" in requette))):
                name = self._fonctionArreraNetwork.getFileWord()
                self._listSortie = [self._fonctionArreraNetwork.sortieCloseDocx(), ""]
                self._objHistorique.setAction("Fermeture du fichier word " + name)
                self._valeurOut = 8
                return 1

            elif (("lis" in requette)and ("word" in requette)and ("liste" not in requette)):
                self._listSortie = [self._fonctionArreraNetwork.sortieReadDocx(), ""]
                self._objHistorique.setAction(
                    "Lecture du fichier word " +
                    self._fonctionArreraNetwork.getFileWord()
                )
                self._valeurOut = 9
                return 1

            elif (("ecrit" in requette)and ("word" in requette)):
                # C'est plus souple, reconnaît toute phrase avec ces deux mots !
                self._listSortie = [self._fonctionArreraNetwork.sortieWriteDocx(requette), ""]
                self._objHistorique.setAction(
                    "Ecriture dans le fichier docx " +
                    self._fonctionArreraNetwork.getFileWord()
                )
                self._valeurOut = 1
                return 1

            elif (("montre" in requette)and (("word" in requette)or
                 ("traitement de texte" in requette)or ("document" in requette))):
                self._listSortie = [self._fonctionArreraNetwork.sortieOpenWordGUI(), ""]
                self._objHistorique.setAction(
                    "Ouverture du word " +
                    self._fonctionArreraNetwork.getFileWord() +
                    " dans l'interface de l'assistant"
                )
                self._valeurOut = 5
                return 1

            elif ("aide word" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieHelpWorkTraitementTexte(), "word"]
                self._valeurOut = 17
                return 1

            else :
                return 0
        return 0