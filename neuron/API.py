from ObjetsNetwork.chaineCarractere import*
from neuron.CNeuronBase import neuronBase

class neuroneAPI(neuronBase) :


    def neurone(self,requette:str):

        listeLang = ["anglais","francais","espagnol","allemand", "chinois simplifie","chinois traditionnel",
                            "arabe", "russe","japonais","coreen","italien","portugais","neerlandais",
                            "suedois","danois","norvegien","finnois","grec","hebreu","indonesien"]

        dictLang = {"anglais":"en","francais":"fr","espagnol":"es","allemand":"de", "chinois simplifie":"zh-CN",
                           "chinois traditionnel":"zh-TW","arabe":"ar", "russe":"ru","japonais":"ja",
                           "coreen":"ko","italien":"it","portugais":"pt","neerlandais":"nl","suedois":"sv",
                           "danois":"da","norvegien":"no","finnois":"fi","grec":"el","hebreu":"he","indonesien":"id"}

        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0
        etatVilleDomicile = self._gestionNeuron.getEtatLieuDomicile()
        etatVilleTravail = self._gestionNeuron.getEtatLieuTravail()

        if self._gestNeuron.getAPI() == True :
            #reponse du neuron main
            if (("resumer actualites" in requette) or ("resumer actu" in requette)) :
                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieResumerActualite()
                self._objHistorique.setAction("Resumer actualiter")
            elif (("resumer" in requette) and (("jour" in requette) or ("aujourd'hui" in requette))) :
                nb,listout = self._fonctionArreraNetwork.sortieResumerAll()
                self._listSortie = listout
                self._valeurOut = nb
                self._objHistorique.setAction("Resumer complete de la journee")
            elif "actualites" in requette or "actu" in requette:
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieActualités()
                    self._objHistorique.setAction("Actualités")
            elif "meteo" in requette :
                    nb = self._gestionNeuron.getnbVilleMeteo()
                    villes = self._gestionNeuron.getListVilleMeteo()
                    resultat = 0
                    if ("demain midi" in requette):
                        for i in range(0,nb):
                            ville = chaine.netoyage(villes[i])
                            if ville in requette :
                                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmorNoon(villes[i])
                                resultat = 1
                                break
                            else :
                                resultat = 0
                        if resultat == 0 :
                            if etatVilleDomicile == True or etatVilleTravail == True :
                                if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmorNoon(self._gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                elif "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmorNoon(self._gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                else :
                                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmorNoon("")
                            else :
                                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmorNoon("")
                        self._objHistorique.setAction("Meteo demain midi")
                    elif (("demain matin" in requette) or ("demain" in requette)):
                            for i in range(0,nb):
                                ville = chaine.netoyage(villes[i])
                                if ville in requette :
                                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmoroMorning(villes[i])
                                    resultat = 1
                                    break
                                else :
                                    resultat = 0
                                if resultat == 0 :
                                    if etatVilleDomicile == True or etatVilleTravail == True :
                                        if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                            self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmoroMorning(self._gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                        elif "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmoroMorning(self._gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                        else :
                                            self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmoroMorning("")
                                    else :
                                        self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoTowmoroMorning("")
                                        self._objHistorique.setAction("Meteo demain matin")
                    else :
                        for i in range(0,nb):
                            ville = chaine.netoyage(villes[i])
                            if ville in requette :
                                self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoToday(villes[i])
                                self._objHistorique.setAction("Meteo aujourd'hui dans " + ville[i])
                                resultat = 1
                                break
                            else :
                                resultat = 0
                            if resultat == 0 :
                                if etatVilleDomicile == True or etatVilleTravail == True :
                                    if "domicile" in requette or "residence" in requette or "maison" in requette or "appartement" in requette or "chez moi" in requette or "foyer" in requette or "maison" in requette or "foyer" in requette or "demeure "in requette :
                                        self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoToday(self._gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
                                        self._objHistorique.setAction("Meteo aujourd'hui au domicile")
                                    elif "bureau" in requette or "lieu de travail" in requette or "entreprise" in requette or "societe" in requette or "boulot" in requette or "cabinet" in requette or "college" in requette or "lycee" in requette or "ecole" in requette or "campus" in requette or "universite" in requette :
                                        self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoToday(self._gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                                        self._objHistorique.setAction("Meteo aujourd'hui au lieu de travail")
                                    else :
                                        self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoToday("")
                                        self._objHistorique.setAction("Meteo aujourd'hui a la localisation")
                                else :
                                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieMeteoToday("")
                                    self._objHistorique.setAction("Meteo aujourd'hui a la localisation")

            elif "temperature" in requette :
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieTemperature()
                    self._objHistorique.setAction("Temperature")
            elif "coordonnee gps" in requette or "position gps" in requette :
                    self._valeurOut,self._listSortie = self._fonctionArreraNetwork.sortieGPS()
                    self._objHistorique.setAction("Possition gps")
            elif ((("indique moi l'itineraire de" in requette)and("sur le gps" in requette))
                    or(("lance le gps pour un trajet de" in requette )and("a" in requette))):
                    self._listSortie = [self._fonctionArreraNetwork.sortieItineraire(requette), ""]
                    self._valeurOut = 1
                    self._objHistorique.setAction("Ouverture d'un itineraire sur google map")
            elif ("gps aide" in requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieHelpItineraire(), ""]
                    self._valeurOut = 1
            elif "traduis" in requette or "traduction" in requette or "traduire" in requette :
                    chaineCarractere = str(requette).lower()
                    presenceLang = False
                    self._objHistorique.setAction("Outil de traduction")
                    for i in range(0,len(listeLang)-1):
                        if listeLang[i] in chaineCarractere :
                            presenceLang = True
                            break
                    if presenceLang == True :
                        presenceLang = False
                        firstLang = chaine.firstMots(chaineCarractere,listeLang)
                        chaineCarractere = chaineCarractere.replace(firstLang,"")
                        for i in range(0,len(listeLang)-1):
                            if listeLang[i] in chaineCarractere :
                                presenceLang = True
                                break
                        if presenceLang == True :
                            secondLang = chaine.firstMots(chaineCarractere,listeLang)
                            self._listSortie= [
                                self._fonctionArreraNetwork.sortieTraducteur(dictLang[firstLang], dictLang[secondLang])
                                ,""]
                            self._valeurOut = 3
                        else :
                            self._listSortie = [self._fonctionArreraNetwork.sortieErrorLangue(), ""]
                            self._valeurOut = 1
                    else :
                        self._listSortie = [self._fonctionArreraNetwork.sortieErrorLangue(), ""]
                        self._valeurOut = 1