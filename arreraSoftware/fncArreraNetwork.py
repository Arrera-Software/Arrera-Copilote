import random
from librairy.openSoftware import *
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *
from arreraSoftware.fonctionGPS import *
from arreraSoftware.fonctionTraduction import *
from arreraSoftware.fonctionArreraDownload import *
from arreraSoftware.fonctionCalculatrice import *
from arreraSoftware.fonctionRecherche import *
from arreraSoftware.fonctionHorloge import *
from arreraSoftware.fonctionCalendar import *
from arreraSoftware.fonctionCodeHelp import *
from arreraSoftware.fonctionArreraWork import *
from arreraSoftware.fonctionRadio import *
from arreraSoftware.fncOrthographe import *


class fncArreraNetwork:
    def __init__(self, gestionNeuron: gestionNetwork):
        # Recuperation des objet
        self.__gestionNeuron = gestionNeuron
        self.__configNeuron = self.__gestionNeuron.getConfigFile()
        self.__detecteurOS = self.__gestionNeuron.getOSObjet()
        self.__objetNetwork = self.__gestionNeuron.getNetworkObjet()
        self.__mLanguage = self.__gestionNeuron.getLanguageObjet()
        # Recuperation etat de la connextion internet
        etatConnextion = self.__objetNetwork.getEtatInternet()
        # initialisation objet
        self.__fncReading = fncLecture(self.__configNeuron, self.__detecteurOS)
        self.__actu = Actu("3b43e18afcf945888748071d177b8513")
        self.__gps = GPS("19bfbee6112be5b3d9a64d4ccec72602", etatConnextion)
        self.__meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        self.__traducteur = fncArreraTrad(self.__configNeuron, )
        self.__downloader = fncArreraVideoDownload(self.__configNeuron, self.__gestionNeuron)
        self.__calculatrice = fncCalculatrice(self.__configNeuron)
        self.__objetRecherche = fncArreraSearch(etatConnextion)
        self.__objetDate = fncDate()
        self.__objetHorloge = fncArreraHorloge()
        self.__objetCalendar = fncArreraAgenda(self.__configNeuron, self.__gestionNeuron)
        self.__objetTache = fncArreraTache(self.__objetDate, self.__configNeuron,
                                           self.__gestionNeuron.getEmplacemntfileTache())
        self.__objetCodehelp = fncCodehelp(self.__configNeuron, self.__detecteurOS, self.__gestionNeuron)
        self.__objetArreraWork = fncArreraWork(self.__objetDate, self.__gestionNeuron, self.__configNeuron,
                                               self.__detecteurOS)
        self.__objetHorloge.setAtributJSON(self.__configNeuron)
        self.__objetOpenSoft = OpenSoftware(self.__gestionNeuron)
        self.__objRadio = fncRadio(self.__objetNetwork)
        # Fonction qui on besoin d'internet
        if (etatConnextion == True):
            self.__objOrthographe = fncOrthagraphe(self.__configNeuron.lectureJSON("interfaceColor"),
                                                   self.__configNeuron.lectureJSON("interfaceTextColor"))

    def reading(self):
        self.__fncReading.fenetreLecture()
        text = self.__mLanguage.getPhraseService("6")
        return text

    def sortieActualités(self):
        sortie = self.__actu.setActu("6", "fr")
        if (sortie == True):
            listActu = self.__actu.getActu()
            if ((listActu[0] == "error") and (listActu[1] == "error")):
                return 6, [self.__mLanguage.getPhraseApi("1"), ""]
            else:
                nbrand1 = random.randint(0, 1)
                nbrand2 = random.randint(2, 3)
                nbrand3 = random.randint(4, 5)
                return 3, [listActu[nbrand1], listActu[nbrand2], listActu[nbrand3]]
        else:
            return 6, [self.__mLanguage.getPhraseApi("1"), ""]

    def sortieMeteoTowmoroMorning(self, ville):
        if ville == "":
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True:
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True:
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDateMetoTowmorowMorning(lat, lon)
                    if sortiMeteo == True:
                        nbrand = random.randint(0, 1)
                        text = self.__mLanguage.getPhraseMeteo("3", nameVille, self.__meteo.getdescription(),
                                                               self.__meteo.gettemperature())[nbrand]
                    else:
                        text = self.__mLanguage.getPhraseMeteoError("3")
                else:
                    text = self.__mLanguage.getPhraseMeteoError("3")
            else:
                text = self.__mLanguage.getPhraseMeteoError("3")
        else:
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True:
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDateMetoTowmorowMorning(lat, lon)
                if sortiMeteo == True:
                    nameVille = ville
                    nbRand = random.randint(0, 1)
                    text = self.__mLanguage.getPhraseMeteo("4", nameVille, self.__meteo.getdescription(),
                                                           self.__meteo.gettemperature())[nbRand]
                else:
                    text = self.__mLanguage.getPhraseMeteoError("4")
            else:
                text = self.__mLanguage.getPhraseMeteoError("4")
        return [text, ""]

    def sortieMeteoTowmorNoon(self, ville):
        if ville == "":
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True:
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True:
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDateMetoTowmorowNoon(lat, lon)
                    if sortiMeteo == True:
                        nbrand = random.randint(0, 1)
                        listReponse = self.__mLanguage.getPhraseMeteo("1", nameVille, self.__meteo.getdescription(),
                                                                      self.__meteo.gettemperature())
                        text = listReponse[nbrand]
                    else:
                        text = self.__mLanguage.getPhraseMeteoError("1")
                else:
                    text = self.__mLanguage.getPhraseMeteoError("1")
            else:
                text = self.__mLanguage.getPhraseMeteoError("1")
        else:
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True:
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDateMetoTowmorowNoon(lat, lon)
                if sortiMeteo == True:
                    nameVille = ville
                    nbRand = random.randint(0, 1)
                    text = self.__mLanguage.getPhraseMeteo("2", nameVille, self.__meteo.getdescription(),
                                                           self.__meteo.gettemperature())[nbRand]
                else:
                    text = self.__mLanguage.getPhraseMeteoError("2")
            else:
                text = self.__mLanguage.getPhraseMeteoError("2")

        return [text, ""]

    def sortieMeteoToday(self, ville):
        if ville == "":
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True:
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True:
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.getDataMeteoNow(lat, lon)
                    if sortiMeteo == True:
                        nbrand = random.randint(0, 1)
                        text = self.__mLanguage.getPhraseMeteo("5", nameVille, self.__meteo.getdescription(),
                                                               self.__meteo.gettemperature())[nbrand]
                    else:
                        text = self.__mLanguage.getPhraseMeteoError("5")
                else:
                    text = self.__mLanguage.getPhraseMeteoError("5")
            else:
                text = self.__mLanguage.getPhraseMeteoError("5")
        else:
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True:
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.getDataMeteoNow(lat, lon)
                if sortiMeteo == True:
                    nameVille = ville
                    nbRand = random.randint(0, 1)
                    text = self.__mLanguage.getPhraseMeteo("6", nameVille, self.__meteo.getdescription(),
                                                           self.__meteo.gettemperature())[nbRand]
                else:
                    text = self.__mLanguage.getPhraseMeteoError("6")
            else:
                text = self.__mLanguage.getPhraseMeteoError("6")

        return [text, ""]

    def sortieTemperature(self):
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True:
            lat = self.__gps.getlatPossition()
            lon = self.__gps.getlonPossition()
            sortieMeteo = self.__meteo.getDataMeteoNow(lat, lon)
            if sortieMeteo == True:
                text = self.__mLanguage.getPhraseTemperature(self.__meteo.gettemperature())
        return 4, text

    def sortieGPS(self):
        text = []
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True:
            sortieGPS = self.__gps.recuperationNameVillePosition()
            if sortieGPS == True:
                lat = self.__gps.getlatPossition()
                lon = self.__gps.getlonPossition()
                nameVille = self.__gps.getNameVille()
                text = self.__mLanguage.getPhraseCoordonnees(nameVille, lat, lon)
        return 4, text

    def sortieItineraire(self, phrase):
        """
        Extrait les adresses de départ et d'arrivée d'une phrase donnée.

        Parameters:
        phrase (str): La phrase contenant les adresses de départ et d'arrivée.

        Returns:
        tuple: Une paire (départ, arrivée) des adresses extraites.

        Phrase a utiliser :
            indique-moi l'itineraire de [depart] a [arrive] sur le GPS, s'il te plait.

            lance le GPS pour un trajet de [depart] a [arrive], s'il te plaît.
        Mots qui peuvent compter comme ville :
            domicile,residence,maison,appartement,chez moi,foyer,maison,foyer,demeure
            bureau,lieu de travail,entreprise,societe,boulot,cabinet",college,lycee,ecole,campus,universite
            la ou je suis , ma localisation
        """
        reusite = bool
        # Expressions régulières pour extraire les parties de la phrase
        pattern = re.compile(r"de\s+(.*?)\s+(?:a|comme|et)\s+(.*?)\s+(?:comme|et|s'il|destination|aller|sur|,|\.|$)",
                             re.IGNORECASE)
        match = pattern.search(phrase)
        depart = ""

        if match:
            depart = match.group(1).strip()
            arrivee = match.group(2).strip()
            reusite = True
        else:
            reusite = False
        if (reusite == True):
            if ((depart == "domicile") or (depart == "residence")
                    or (depart == "maison") or (depart == "appartement")
                    or (depart == "chez moi") or (depart == "foyer")
                    or (depart == "maison") or (depart == "foyer")
                    or (depart == "demeure")):
                depart = self.__gestionNeuron.getAdresseDomicile()
            else:
                if ((depart == "bureau") or (depart == "lieu de travail")
                        or (depart == "entreprise") or (depart == "societe")
                        or (depart == "boulot") or (depart == "cabinet")
                        or (depart == "college") or (depart == "lycee")
                        or (depart == "ecole") or (depart == "campus")
                        or (depart == "universite")):
                    depart = self.__gestionNeuron.getAdresseTravil()
                else:
                    if ((depart == "la ou je suis") or (depart == "ma localisation")):
                        if (self.__gps.recuperationNameVillePosition() != False):
                            return self.__mLanguage.getPhraseIteneraireError("1")
                        else:
                            depart = self.__gps.getNameVille()

            if ((arrivee == "domicile") or (arrivee == "residence")
                    or (arrivee == "maison") or (arrivee == "appartement")
                    or (arrivee == "chez moi") or (arrivee == "foyer")
                    or (arrivee == "maison") or (arrivee == "foyer")
                    or (arrivee == "demeure")):
                arrivee = self.__gestionNeuron.getAdresseDomicile()
            else:
                if ((arrivee == "bureau") or (arrivee == "lieu de travail")
                        or (arrivee == "entreprise") or (arrivee == "societe")
                        or (arrivee == "boulot") or (arrivee == "cabinet")
                        or (arrivee == "college") or (arrivee == "lycee")
                        or (arrivee == "ecole") or (arrivee == "campus")
                        or (arrivee == "universite")):
                    arrivee = self.__gestionNeuron.getAdresseTravil()
                else:
                    if ((arrivee == "la ou je suis") or (arrivee == "ma localisation")):
                        if (self.__gps.recuperationNameVillePosition() != False):
                            return self.__mLanguage.getPhraseIteneraireError("1")
                        else:
                            arrivee = self.__gps.getNameVille()
            sortieGMap = self.__gps.launchGoogleMapItineraire(depart, arrivee)
            if (sortieGMap == True):
                return self.__mLanguage.getPhraseIteneraire()
            else:
                return self.__mLanguage.getPhraseIteneraireError("2")
        else:
            return self.__mLanguage.getPhraseIteneraireError("3")

    def sortieHelpItineraire(self):
        return self.__mLanguage.getHelpIteneraire()

    def sortieResumerActualite(self):
        """

        Returns:
            meteoHome,meteoWork,feteJour,Actu 1,Actu 2,Actu 3,textSpeak
        """
        # var
        verif = False
        meteoHome = ""
        meteoWork = ""
        feteJour = ""
        nbrand1 = random.randint(0, 1)
        nbrand2 = random.randint(2, 3)
        nbrand3 = random.randint(4, 5)
        listOut = []

        textSpeak = self.__mLanguage.getPhraseResumerActu()

        # Partie Meteo

        domicile = self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile")
        travail = self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail")

        # Meteo a domicile
        if (domicile != ""):
            verif = self.__gps.recuperationCordonneeVille(domicile)
            if (verif == True):
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatVille(), self.__gps.getLonVille())
                if (verif == True):
                    textSpeak = textSpeak + \
                                self.__mLanguage.getPhraseMeteo("7", domicile, self.__meteo.getdescription(),
                                                                self.__meteo.gettemperature())[random.randint(0, 1)]
                    meteoHome = "Meteo lieu de residence :\nDescription : " + self.__meteo.getdescription() + "\nTemperature : " + self.__meteo.gettemperature() + "°C"
                else:
                    meteoHome = "error"
            else:
                meteoHome = "error"
        else:
            meteoHome = "error"

        # Meteo sur le lieu de travail
        if (travail != ""):
            verif = self.__gps.recuperationCordonneeVille(travail)
            if (verif == True):
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatVille(), self.__gps.getLonVille())
                if (verif == True):
                    textSpeak = textSpeak + self.__mLanguage.getPhraseMeteo("8", travail, self.__meteo.getdescription(),
                                                                            self.__meteo.gettemperature())[
                        random.randint(0, 1)]
                    meteoWork = "Meteo lieu de travail :\nDescription : " + self.__meteo.getdescription() + "\nTemperature : " + self.__meteo.gettemperature() + "°C"
                else:
                    meteoWork = "error"
            else:
                meteoWork = "error"
        else:
            meteoWork = "error"

            # Meteo sur la position que si la meteo au lieu de travail et au domicile a echouer
        if (meteoHome == "error" and meteoWork == "error"):
            verif = self.__gps.recuperationCordonneePossition()
            if (verif == True):
                verif = self.__meteo.getDataMeteoNow(self.__gps.getlatPossition(), self.__gps.getlonPossition())
                if (verif == True):
                    textSpeak = textSpeak + self.__mLanguage.getPhraseMeteo("9", self.__gps.getNameVille(),
                                                                            self.__meteo.getdescription(),
                                                                            self.__meteo.gettemperature())[
                        random.randint(0, 1)]
                    meteoWork = "Meteo a votre position :\nDescription : " + self.__meteo.getdescription() + "\nTemperature : " + self.__meteo.gettemperature() + "°C"
                else:
                    meteoWork = "error"
            else:
                meteoWork = "error"

                # fete du jour
        feteJour = self.__gestionNeuron.getFeteJour()
        textSpeak = textSpeak + "La fête du jour est " + feteJour + ". "

        # Liste des actu
        verif = self.__actu.setActu("6", "fr")
        if (verif == True):
            listeActu = self.__actu.getActu()
            textSpeak = textSpeak + "Et enfin les actualités sont " + listeActu[nbrand1] + ", " + listeActu[
                nbrand2] + " et " + listeActu[nbrand3]
            # Construction de la liste
            listOut = [meteoHome, meteoWork, feteJour, listeActu[nbrand1], listeActu[nbrand2], listeActu[nbrand3],
                       textSpeak]
            return 12, listOut
        else:
            return 11, ["error", "error"]

    def sortieTraducteur(self, langInt: str, langOut: str):
        self.__traducteur.fenetreTrad(langInt, langOut)
        return self.__mLanguage.getPhraseOpenTraducteur()

    def sortieErrorLangue(self):
        return self.__mLanguage.getPhraseErrorLangue()

    def sortieCalculatrice(self, mode):
        if mode == "0":
            text = self.__mLanguage.getPhraseSoftware("4")
        else:
            if mode == "1":
                text = self.__mLanguage.getPhraseSoftware("5")
            else:
                text = self.__mLanguage.getPhraseSoftware("6")
        self.__calculatrice.calculatrice(mode)
        return text

    def sortieOpenSoftware(self, requette):
        soft = requette.lower().replace("ouvrir",
                                        "").replace("ouvre"
                                                    , "").strip()
        return self.__mLanguage.getPhraseOpenSoftware("1", soft)

    def openSoftwareAssistant(self, requette: str):
        """
        Ouvre un logiciel à partir d'une requête textuelle.

        Args:
            requette: La demande d'ouverture d'un logiciel (ex: "ouvrir notepad")

        Returns:
            bool: True si le logiciel a été ouvert avec succès, False sinon
        """
        soft = requette.lower().replace("ouvrir",
                                        "").replace("ouvre"
                                                    , "").strip()

        listeLogiciel = self.__gestionNeuron.getListLogiciel()
        dictionnaireSoft = self.__gestionNeuron.getDictionnaireLogiciel()

        if not listeLogiciel:
            return False

        for logiciel in listeLogiciel:
            if soft in logiciel.lower():
                if self.__objetOpenSoft.setName(dictionnaireSoft[soft]):
                    self.__objetOpenSoft.open()
                    return True
                return False
        return False

    def sortieOpenYoutube(self):
        socket = self.__gestionNeuron.getSocketObjet()

        if (self.__gestionNeuron.getEtatNeuronObjet().getSocket() == True):
            if (socket.getServeurOn() == True):
                sortie = socket.sendData("website " + "https://www.youtube.com/")
            else:
                sortie = webbrowser.open("https://www.youtube.com/")
        else:
            sortie = webbrowser.open("https://www.youtube.com/")

        if sortie:
            text = self.__mLanguage.getPhraseOpen("6")
        else:
            text = self.__mLanguage.getPhraseOpenError("6")

        return text

    def sortieOpenSite(self, requette: str, etat: bool):
        site = requette.replace("ouvrir", "").replace("ouvre", "").strip().lower()
        return self.__mLanguage.getPhraseOpenSite(site, etat)

    def openWebSiteAssistant(self, requette: str):
        socket = self.__gestionNeuron.getSocketObjet()

        webSite = requette.replace("ouvrir", "").replace("ouvre", "").strip().lower()

        listeSite = self.__gestionNeuron.getListWeb()
        dictionnaireWebSite = self.__gestionNeuron.getDictionnaireWeb()

        if not listeSite:
            return False

        for site in listeSite:
            if webSite in site.lower():
                if (socket.getServeurOn() == True):
                    if (socket.sendData("website " + dictionnaireWebSite[site])):
                        return True
                    else:
                        return False
                else:
                    if webbrowser.open(dictionnaireWebSite[site]):
                        return True
                    else:
                        return False
        return False

    def sortieNoOpen(self):
        return self.__mLanguage.getPhraseOpen("7")

    def sortieRechercheSimple(self, requette: str):
        moteurDefault = self.__gestionNeuron.getMoteurRechercheDefault()
        moteurUser = self.__gestionNeuron.getValeurfichierUtilisateur("moteurRecherche")
        recherche = requette.replace("search", "")
        recherche = recherche.replace("recherche", "")
        if moteurUser == "":
            moteur = moteurDefault
        else:
            moteur = moteurUser

        match moteur:
            case "duckduckgo":
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
            case "google":
                sortieRecherche = self.__objetRecherche.googleSearch(recherche)
            case "qwant":
                sortieRecherche = self.__objetRecherche.qwantSearch(recherche)
            case "ecosia":
                sortieRecherche = self.__objetRecherche.ecosiaSearch(recherche)
            case "brave":
                sortieRecherche = self.__objetRecherche.braveSearch(recherche)
            case "bing":
                sortieRecherche = self.__objetRecherche.bingSearch(recherche)
            case "perplexity":
                sortieRecherche = self.__objetRecherche.perplexitySearch(recherche)
            case other:
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
        if sortieRecherche == False:
            text = self.__mLanguage.getPhraseSearch("3")
        else:
            text = self.__mLanguage.getPhraseSearch("4")

        return text, recherche

    def sortieGrandRecherche(self, requette: str):
        recherche = requette.replace("bigsearch", "")
        recherche = recherche.replace("grand recherche", "")
        sortieRecheche = self.__objetRecherche.bigRecherche(recherche)
        if sortieRecheche == True:
            text = self.__mLanguage.getPhraseSearch("1")
        else:
            text = self.__mLanguage.getPhraseSearch("2")
        return text, recherche

    def sortieHeure(self):
        self.__objetDate.rafraichisement()
        heure = self.__objetDate.heure()
        minute = self.__objetDate.minute()
        return self.__mLanguage.getPhraseHeure(heure, minute)

    def sortieDate(self):
        self.__objetDate.rafraichisement()
        jour = self.__objetDate.jour()
        mois = self.__objetDate.mois()
        annes = self.__objetDate.annes()
        return self.__mLanguage.getPhraseDate(jour, mois, annes)

    def sortieOpenChrono(self):
        text = self.__mLanguage.getPhraseTime("1")
        self.__objetHorloge.modeChrono()
        return text

    def sortieOpenHorloge(self):
        text = self.__mLanguage.getPhraseTime("2")
        self.__objetHorloge.modeHorloge()
        return text

    def sortieOpenSimpleMinuteur(self):
        text = self.__mLanguage.getPhraseTime("3")
        self.__objetHorloge.modeMinuteur()
        return text

    def sortieAjoutEvent(self):
        self.__objetCalendar.activeAddWindows()
        text = self.__mLanguage.getPhraseTime("4")
        return text

    def sortieSupprEvent(self):
        self.__objetCalendar.activeSupprWindows()
        text = self.__mLanguage.getPhraseTime("5")
        return text

    def sortieEvenementDay(self):
        tampons = ""
        text = ""
        nbEvent = self.__objetCalendar.getNbEventToday()
        if (nbEvent == 0):
            text = self.__mLanguage.getPhraseTime("6")
        else:
            listEvent = self.__objetCalendar.getEventToday()
            if (nbEvent == 1):
                text = self.__mLanguage.getPhraseTime("7") + listEvent[0]
            else:
                baseTexte = self.__mLanguage.getPhraseEvent(str(nbEvent))
                for i in range(0, nbEvent):
                    if (i == 0):
                        tampons = baseTexte + listEvent[i]
                    else:
                        if (i == (nbEvent - 1)):
                            text = tampons + " et " + listEvent[i]
                        else:
                            text = tampons + ", " + listEvent[i]
        return text

    def sortieOpenAgenda(self):
        text = self.__mLanguage.getPhraseTime("8")
        self.__objetCalendar.activeAgenda()
        return text

    def sortieListLogiciel(self):
        listSoft = self.__gestionNeuron.getListLogiciel()
        nb = len(listSoft)
        texte = ""
        if (nb == 0):
            return self.__mLanguage.getPhraseOpen("8")
        elif (nb == 1):
            return self.__mLanguage.getPhraseOpen("9") + listSoft[0]
        else:
            baseTexte = self.__mLanguage.getPhraseNbOpenSoftware(str(nb))
            for i in range(0, nb):
                if (i == 0):
                    texte = baseTexte + " " + listSoft[i]
                elif (i == (nb - 1)):
                    texte = texte + " et " + listSoft[i]
                else:
                    texte = texte + ", " + listSoft[i]

        return texte

    def sortieListSite(self):
        listSite = self.__gestionNeuron.getListWeb()
        nb = len(listSite)
        texte = ""
        if (nb == 0):
            return self.__mLanguage.getPhraseOpen("10")
        elif (nb == 1):
            return self.__mLanguage.getPhraseOpen("11") + listSite[0]
        else:
            baseTexte = self.__mLanguage.getPhraseNbOpenSoftware(str(nb))
            for i in range(0, nb):
                if (i == 0):
                    texte = baseTexte + " " + listSite[i]
                elif (i == (nb - 1)):
                    texte = texte + " et " + listSite[i]
                else:
                    texte = texte + ", " + listSite[i]

        return texte

    def sortieListRadio(self):
        return self.__mLanguage.getPhraseListeRadio()

    def sortieViewTache(self):
        text = self.__mLanguage.getPhraseTime("9")
        self.__objetTache.activeViewTask()
        return text

    def sortieViewTacheAdd(self):
        text = self.__mLanguage.getPhraseTime("10")
        self.__objetTache.activeViewAdd()
        return text

    def sortieViewTacheSuppr(self):
        sortie = self.__objetTache.activeViewSuppr()
        if (sortie == True):
            text = self.__mLanguage.getPhraseTime("11")
        else:
            text = self.__mLanguage.getPhraseTime("12")
        return text

    def sortieViewTacheCheck(self):
        sortie = self.__objetTache.activeViewCheck()
        if (sortie == True):
            text = self.__mLanguage.getPhraseTime("13")
        else:
            text = self.__mLanguage.getPhraseTime("14")
        return text

    def sortieNbSpeakTache(self):
        nbTache = self.__objetTache.getNbTache()
        nbToday = self.__objetTache.getNbTacheToday()
        if (nbTache == 0):
            text = self.__mLanguage.getPhraseTime("15")
        else:
            if (nbTache == 1):
                if (nbToday == 1):
                    text = self.__mLanguage.getPhraseTime("16")
                else:
                    text = self.__mLanguage.getPhraseTime("17")
            else:
                if (nbTache == 1):
                    text = self.__mLanguage.getPhraseNBTache("1", str(nbTache), "0")
                else:
                    if (nbTache > 1):
                        text = self.__mLanguage.getPhraseNBTache("1", str(nbTache), str(nbToday))
                    else:
                        text = self.__mLanguage.getPhraseNBTache("3", str(nbTache), "0")
        return text

    def sortieSpeakTacheToday(self):
        listTache = self.__objetTache.getTacheToday()
        nbTache = len(listTache)
        if (nbTache == 0):
            text = self.__mLanguage.getPhraseTime("18")
        else:
            if (nbTache == 1):
                baseText = self.__mLanguage.getPhraseTime("19") + " "
            else:
                baseText = self.__mLanguage.getPhraseNBTache("3", str(nbTache), "0") + " "
            for i in range(0, nbTache):
                if (i == 0):
                    text = baseText + listTache[i]
                else:
                    if (i == (nbTache - 1)):
                        text = text + " et " + listTache[i]
                    else:
                        text = text + ", " + listTache[i]
        return text

    def sortieSpeakTacheTowmorow(self):
        listTache = self.__objetTache.getTacheTowmorow()
        nbTache = len(listTache)
        if (nbTache == 0):
            text = self.__mLanguage.getPhraseTime("20")
        else:
            if (nbTache == 1):
                baseText = self.__mLanguage.getPhraseTime("21") + " "
            else:
                baseText = self.__mLanguage.getPhraseNBTache("5", str(nbTache), "0") + " "
            for i in range(0, nbTache):
                if (i == 0):
                    text = baseText + listTache[i]
                else:
                    if (i == (nbTache - 1)):
                        text = text + " et " + listTache[i]
                    else:
                        text = text + ", " + listTache[i]
        return text

    def sortieOpenOrgaVar(self):
        text = self.__mLanguage.getPhraseCodehelp("1")
        self.__objetCodehelp.activeOrgaVar()
        return text

    def sortieSearchDoc(self, requette: str):
        """
        Flag recherche :
            - recherche devdoc / rdevdoc / sdevdoc : Recherche dans sur devdoc
            - recherche microsoft / rmicrosoft / smicrosoft : recherche microsoft learn
            - recheche python / rpython / spython : recherche sur le site python.org
        """
        if (("recherche devdoc" in requette) or ("rdevdoc" in requette) or ("sdevdoc" in requette)):
            recherche = requette.replace("recherche devdoc", "")
            recherche = recherche.replace("rdevdoc", "")
            recherche = recherche.replace("sdevdoc", "")
            self.__objetCodehelp.rechercheDoc(1, recherche)
            text = self.__mLanguage.getPhraseCodehelp("6")
            r = "devdoc " + recherche
            return text, r
        else:
            if (("recherche microsoft" in requette) or ("rmicrosoft" in requette) or ("smicrosoft" in requette)):
                recherche = requette.replace("recherche microsoft", "")
                recherche = recherche.replace("rmicrosoft", "")
                recherche = recherche.replace("smicrosoft", "")
                self.__objetCodehelp.rechercheDoc(2, recherche)
                text = self.__mLanguage.getPhraseCodehelp("7")
                r = "microsoft " + recherche
                return text, r
            else:
                if (("recheche python" in requette) or ("rpython" in requette) or ("spython" in requette)):
                    recherche = requette.replace("recheche python", "")
                    recherche = recherche.replace("rpython", "")
                    recherche = recherche.replace("spython", "")
                    self.__objetCodehelp.rechercheDoc(3, recherche)
                    text = self.__mLanguage.getPhraseCodehelp("8")
                    r = "python " + recherche
                    return text, r

        return "", ""

    def sortieOpenColorSelecteur(self):
        text = self.__mLanguage.getPhraseCodehelp("2")
        self.__objetCodehelp.activeColorSelecteur()
        return text

    def sortieSearchGithub(self, requette: str):
        """
        Flag de recherche :
            recherche github
            rgithub
            sgithub
            search github
        """
        text = self.__mLanguage.getPhraseWork("69")

        recherche = requette.replace("recherche github", "")
        recherche = recherche.replace("rgithub", "")
        recherche = recherche.replace("sgithub", "")
        recherche = recherche.replace("search github", "")

        self.__objetCodehelp.searchGithub(recherche)

        return text, recherche

    def sortieOpenSiteGithub(self):
        text = self.__mLanguage.getPhraseCodehelp("3")
        self.__objetCodehelp.openSiteGithub()
        return text

    def sortieOpenGuiGithub(self):
        text = self.__mLanguage.getPhraseCodehelp("4")
        self.__objetCodehelp.openGestionGithub()
        return text

    def sortieOpenLibrairy(self):
        text = self.__mLanguage.getPhraseCodehelp("5")
        self.__objetCodehelp.openOutilLibrairy()
        return text

    # Partie Arrera Work
    def getWordOpen(self):
        return self.__objetArreraWork.getEtatWord()

    def getTableurOpen(self):
        return self.__objetArreraWork.getEtatTableur()

    def getProjectOpen(self):
        return self.__objetArreraWork.getEtatProject()

    def getFileTableur(self):
        return self.__objetArreraWork.getNameFileTableur()

    def getFileWord(self):
        return self.__objetArreraWork.getNameFileWord()

    def sortieOpenTableur(self):
        sortie = self.__objetArreraWork.openTableur()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("5")
        else:
            text = self.__mLanguage.getPhraseWork("6")
        return text

    def sortieOpenWord(self):
        sortie = self.__objetArreraWork.openWord()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("7")
        else:
            text = self.__mLanguage.getPhraseWork("8")
        return text

    def sortieCloseTableur(self):
        sortie = self.__objetArreraWork.closeTableur()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("10")
        else:
            text = self.__mLanguage.getPhraseWork("11")
        return text

    def sortieCloseDocx(self):
        sortie = self.__objetArreraWork.closeDocx()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("12")
        else:
            text = self.__mLanguage.getPhraseWork("13")
        return text

    def sortieWriteDocx(self, texte: str):
        sortie = self.__objetArreraWork.writeDocxFile()
        if sortie:
            return self.__mLanguage.getPhraseWork("18")
        else:
            return self.__mLanguage.getPhraseWork("19")

    def sortieReadDocx(self):
        sortie = self.__objetArreraWork.readDocxFile()
        if (sortie == "error"):
            text = self.__mLanguage.getPhraseWork("16")
        else:
            text = sortie
        return text

    def sortieFileOpen(self):
        tableur = self.getTableurOpen()
        word = self.getWordOpen()
        if ((tableur == True) and (word == True)):
            text = self.__mLanguage.getPhraseWork("21")
        else:
            if ((tableur == True) and (word == False)):
                text = self.__mLanguage.getPhraseWork("22")
            else:
                if ((tableur == False) and (word == True)):
                    text = self.__mLanguage.getPhraseWork("23")
                else:
                    text = self.__mLanguage.getPhraseWork("24")
        return text

    def sortieReadTableur(self):
        return self.__objetArreraWork.readTableur()

    def sortieErrorReadTableur(self):
        return [self.__mLanguage.getPhraseWork("17"), ""]

    def sortieAddValeurTableur(self):
        sortie = self.__objetArreraWork.tkAddValeurParole()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("25")
        else:
            text = self.__mLanguage.getPhraseWork("26")
        return text

    def sortieSupprValeurTableur(self):
        sortie = self.__objetArreraWork.tkSuppValeurParole()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("41")
        else:
            text = self.__mLanguage.getPhraseWork("42")
        return text

    def sortieAddFormuleTableur(self, mode: int):
        """
        1: Somme
        2: Moyenne
        3: Comptage
        4: Minimun
        5: Maximun
        """
        match mode:
            case 1:
                sortie = self.__objetArreraWork.tkAddFormuleParole(1)
                if (sortie == True):
                    text = self.__mLanguage.getPhraseWork("27")
                else:
                    text = self.__mLanguage.getPhraseWork("28")
            case 2:
                sortie = self.__objetArreraWork.tkAddFormuleParole(2)
                if (sortie == True):
                    text = self.__mLanguage.getPhraseWork("29")
                else:
                    text = self.__mLanguage.getPhraseWork("30")
            case 3:
                sortie = self.__objetArreraWork.tkAddFormuleParole(3)
                if (sortie == True):
                    text = self.__mLanguage.getPhraseWork("64")
                else:
                    text = self.__mLanguage.getPhraseWork("65")
            case 4:
                sortie = self.__objetArreraWork.tkAddFormuleParole(4)
                if (sortie == True):
                    text = self.__mLanguage.getPhraseWork("31")
                else:
                    text = self.__mLanguage.getPhraseWork("32")
            case 5:
                sortie = self.__objetArreraWork.tkAddFormuleParole(5)
                if (sortie == True):
                    text = self.__mLanguage.getPhraseWork("33")
                else:
                    text = self.__mLanguage.getPhraseWork("34")
            case other:
                text = self.__mLanguage.getPhraseWork("35")

        return text

    def sortieOpenSoftTableurFile(self):
        sortie = self.__objetArreraWork.openTableurOs()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("1")
        else:
            text = self.__mLanguage.getPhraseWork("2")
        return text

    def sortieOpenSoftWorkFile(self):
        sortie = self.__objetArreraWork.openWordOs()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("3")
        else:
            text = self.__mLanguage.getPhraseWork("4")
        return text

    def sortieOpenTableurGUI(self):
        sortie = self.__objetArreraWork.guiTableurWork()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("36")
        else:
            text = self.__mLanguage.getPhraseWork("37")
        return text

    def sortieOpenWordGUI(self):
        sortie = self.__objetArreraWork.guiWordWork()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("38")
        else:
            text = self.__mLanguage.getPhraseWork("39")
        return text

    def sortieBadFile(self):
        return [self.__mLanguage.getPhraseWork("40"), ""]

    def sortieCreateFolder(self, requette: str):
        tampon = requette.replace("cree un projet nommer", "")
        tampon = tampon.replace("cree un nouveau projet nommer", "")
        tampon = tampon.replace("cree un projet nomme", "")
        name = tampon.replace("cree un nouveau projet nomme", "")
        name = name.replace(" ", "")
        sortie = self.__objetArreraWork.createProject(name)
        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("4", name)
        else:
            text = self.__mLanguage.getPhraseProjetFileOpen("4", name)
        return text

    def sortieSetTypeProjet(self, requette: str):
        type = requette.replace("le type est", "")
        type = type.replace("le type du projet est", "")
        sortie = self.__objetArreraWork.setTypeProject(type)
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("43")
        else:
            text = self.__mLanguage.getPhraseWork("44")
        return text

    def sortieOpenProjet(self, requette: str):
        projet = requette.replace("ouvre le projet nommer", "")
        projet = projet.replace("ouvre le projet nomme", "")
        projet = projet.replace("ouvre le projet", "")
        projet = projet.replace(" ", "")
        sortie = self.__objetArreraWork.openProjet(projet)
        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("6", projet)
        else:
            text = self.__mLanguage.getPhraseProjetFileOpen("7", projet)
        return projet, text

    def sortieCloseProject(self):
        sortie = self.__objetArreraWork.closeProject()
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("14")
        else:
            text = self.__mLanguage.getPhraseWork("15")
        return text

    def sortieAddfile(self, type: str, name: str):
        """
        Type:
            exel
            word
            odt
            txt
            python
            h
            json
            html
            css
            md
            cpp
            c
            php
            js
            java
            kt
        """
        mode = int
        typeName = ""
        match type:
            case "exel":
                mode = 1
                typeName = "exel"
            case "word":
                mode = 2
                typeName = "word"
            case "odt":
                mode = 3
                typeName = "open document texte"
            case "txt":
                mode = 4
                typeName = "texte"
            case "python":
                mode = 5
                typeName = "python"
            case "h":
                mode = 6
                typeName = "en tête c++"
            case "json":
                mode = 7
                typeName = "json"
            case "html":
                mode = 8
                typeName = "html"
            case "css":
                mode = 9
                typeName = "css"
            case "md":
                mode = 10
                typeName = "md"
            case "cpp":
                mode = 11
                typeName = "laguage c++"
            case "c":
                mode = 12
                typeName = "language c"
            case "php":
                mode = 13
                typeName = "PHP"
            case "js":
                mode = 14
                typeName = "JavaScript"
            case "java":
                mode = 15
                typeName = "Java"
            case "kt":
                mode = 16
                typeName = "Kotlin"

        sortie = self.__objetArreraWork.createFileProject(mode, name)

        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("8", name)
        else:
            text = self.__mLanguage.getPhraseWork("45")

        return text

    def sortieCreateFileDirect(self, requette: str):
        """
        Phrase possible :
            cree un fichier #type#  #nom#
        """
        nom = requette.replace("cree un fichier", "").replace("word", "").replace("odt", "").replace("txt", "").replace(
            "python", "")
        nom = nom.replace("json", "").replace("html", "").replace("css", "").replace("md", "").replace("cpp",
                                                                                                       "").replace(
            "language c", "")
        nom = nom.replace("exel", "").replace("nommer", "").replace("texte", "").replace("en tete", "").replace("open",
                                                                                                                "").replace(
            "tableur", "")
        nom = nom.replace("language c++", "").replace("php", "").replace("javascript", "").replace("java script",
                                                                                                   "").replace("java",
                                                                                                               "").replace(
            "kotlin", "")
        nom = nom.replace("kt", "").replace("js", "").replace("document", "").replace("postite", "").replace("ab", "")
        nom = nom.replace(" ", "")  # Pas touche

        if ("word" in requette):
            typeFile = "word"
        else:
            if (("odt" in requette) or ("open texte document" in requette)):
                typeFile = "odt"
            else:
                if (("txt" in requette) or ("texte" in requette)):
                    typeFile = "txt"
                else:
                    if ("python" in requette):
                        typeFile = "python"
                    else:
                        if (("en tete" in requette)):
                            typeFile = "h"
                        else:
                            if ("json" in requette):
                                typeFile = "json"
                            else:
                                if ("html" in requette):
                                    typeFile = "html"
                                else:
                                    if ("css" in requette):
                                        typeFile = "css"
                                    else:
                                        if ("md" in requette):
                                            typeFile = "md"
                                        else:
                                            if (("cpp" in requette) or ("language c++" in requette)):
                                                typeFile = "cpp"
                                            else:
                                                if (("language c" in requette)):
                                                    typeFile = "c"
                                                else:
                                                    if (("exel" in requette) or ("tableur" in requette)):
                                                        typeFile = "exel"
                                                    else:
                                                        if ("php" in requette):
                                                            typeFile = "php"
                                                        else:
                                                            if (("javascript" in requette) or (
                                                                    "java script" in requette) or ("js" in requette)):
                                                                typeFile = "js"
                                                            else:
                                                                if ("java" in requette):
                                                                    typeFile = "java"
                                                                else:
                                                                    if (("kotlin" in requette) or ("kt" in requette)):
                                                                        typeFile = "kt"
                                                                    else:
                                                                        if ("postite" in requette) or (
                                                                                "ab" in requette):
                                                                            typeFile = "ab"
                                                                        else:
                                                                            typeFile = ""
        return self.sortieAddfile(typeFile, nom)

    def getNameProjetOpen(self):
        return self.__objetArreraWork.getNameProjet()

    def getNameLastFile(self):
        return self.__objetArreraWork.getNameLastFileCreate()

    def sortieopenFileCreated(self):
        sortie = self.__objetArreraWork.openLastFileCreate()
        print(sortie)
        if (sortie == 1):
            text = self.__mLanguage.getPhraseWork("46")
        else:
            if (sortie == 2):
                text = self.__mLanguage.getPhraseWork("47")
            else:
                if (sortie == 3):
                    text = self.__mLanguage.getPhraseWork("48")
                else:
                    if (sortie == 0):
                        text = self.__mLanguage.getPhraseWork("49")
                    else:
                        text = self.__mLanguage.getPhraseWork("49")
        return text

    def sortieListFileProject(self):
        sortie = self.__objetArreraWork.setlistFileProject()

        if (sortie == True):
            liste = self.__objetArreraWork.getListFileProjet()
            finTexte = ""
            for i in range(0, len(liste)):
                if (i == 0):
                    finTexte = liste[i]
                else:
                    if (i == (len(liste) - 1)):
                        finTexte = finTexte + " et " + liste[i]
                    else:
                        finTexte = finTexte + ", " + liste[i]
            text = self.__mLanguage.getPhraseProjetFileOpen("9", finTexte)
        else:
            text = self.__mLanguage.getPhraseWork("50")

        return text

    def sortieOpenFileProject(self, requette: str):
        """
        Phrase  :
            ouvre le fichier du projet nommer #name#
            ouvre le fichier nommer #name#
        """
        nameFile = requette.replace("ouvre le fichier du projet nommer", "")
        nameFile = nameFile.replace("ouvre le fichier nommer", "")
        nameFile = nameFile.replace(" ", "")

        sortie = self.__objetArreraWork.openFileOtherProjet(nameFile)

        if (sortie == 1):
            text = self.__mLanguage.getPhraseProjetFileOpen("1", nameFile)
        else:
            if (sortie == 0):
                text = self.__mLanguage.getPhraseWork("9")
            else:
                if (sortie == 2):
                    text = self.__mLanguage.getPhraseProjetFileOpen("2", nameFile)
                else:
                    if (sortie == 3):
                        text = self.__mLanguage.getPhraseProjetFileOpen("3", nameFile)
        return text, nameFile

    def sortieShowTacheProjet(self):
        sortie = self.__objetArreraWork.showTacheProjet()

        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("10", self.getNameProjetOpen())
        else:
            text = self.__mLanguage.getPhraseWork("51")

        return text

    def sortieAddTacheProjet(self):
        sortie = self.__objetArreraWork.addTacheProjet()
        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("11", self.getNameProjetOpen())
        else:
            text = self.__mLanguage.getPhraseWork("52")
        return text

    def sortieSupprTacheProjet(self):
        sortie = self.__objetArreraWork.supprTacheProjet()
        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("12", self.getNameProjetOpen())
        else:
            self.__mLanguage.getPhraseWork("53")
        return text

    def sortieNbTacheProjet(self):
        sortie = self.__objetArreraWork.getNbTacheProjet()
        sortie2 = self.__objetArreraWork.getNBTacheToday()

        if ((sortie != -1) and (sortie2 != -1) and (sortie != 0)):
            text = self.__mLanguage.getPhraseProjetNbTache("0", str(sortie), self.getNameProjetOpen(), str(sortie2))
        else:
            if (sortie == 0):
                text = self.__mLanguage.getPhraseProjetFileOpen("17", self.getNameProjetOpen())
            else:
                text = self.__mLanguage.getPhraseWork("56")
        return text

    def sortieListeTacheTodayProjet(self):
        sortie = self.__objetArreraWork.setListTacheTodayProjet()
        text = ""
        if (sortie == True):
            listTache = self.__objetArreraWork.getListTacheTodayProjet()
            nbTache = len(listTache)
            if (nbTache == 0):
                text = self.__mLanguage.getPhraseProjetFileOpen("13", self.getNameProjetOpen())
            else:
                if (nbTache == 1):
                    baseText = self.__mLanguage.getPhraseProjetFileOpen("14", self.getNameProjetOpen()) + " "
                else:
                    baseText = self.__mLanguage.getPhraseProjetNbTache("1", str(nbTache),
                                                                       self.getNameProjetOpen()) + " "
                for i in range(0, nbTache):
                    if (i == 0):
                        text = baseText + listTache[i]
                    else:
                        if (i == (nbTache - 1)):
                            text = text + " et " + listTache[i]
                        else:
                            text = text + ", " + listTache[i]
        else:
            text = self.__mLanguage.getPhraseWork("54")
        return text

    def sortieListTacheTowmorowProjet(self):
        text = ""
        sortie = self.__objetArreraWork.setListTacheTowmorowProjet()
        if (sortie == True):
            listTache = self.__objetArreraWork.getListTacheTowmorowProjet()
            nbTache = len(listTache)

            if (nbTache == 0):
                text = self.__mLanguage.getPhraseProjetFileOpen("15", self.getNameProjetOpen())
            else:
                if (nbTache == 1):
                    baseText = self.__mLanguage.getPhraseProjetFileOpen("16", self.getNameProjetOpen()) + " "
                else:
                    baseText = self.__mLanguage.getPhraseProjetNbTache("2", str(nbTache),
                                                                       self.getNameProjetOpen()) + " "
                for i in range(0, nbTache):
                    if (i == 0):
                        text = baseText + listTache[i]
                    else:
                        if (i == (nbTache - 1)):
                            text = text + " et " + listTache[i]
                        else:
                            text = text + ", " + listTache[i]
        else:
            text = self.__mLanguage.getPhraseWork("55")
        return text

    def sortieResumerTacheAgenda(self):
        """
        Return  : tache,agenda

        """
        # Recuperation des liste
        listEvent = self.__objetCalendar.getEventToday()
        listTache = self.__objetTache.getTacheToday()
        # Recuperation du nombre de tache et event
        nbEvent = self.__objetCalendar.getNbEventToday()
        nbTache = len(listTache)
        if (nbTache == 0):
            tacheTXT = self.__mLanguage.getPhraseTime("22")
        else:
            if (nbTache == 1):
                tacheTXT = self.__mLanguage.getPhraseNBTache("6", str(nbTache), "0") + " " + listTache[0] + "."
            else:
                tacheTXT = self.__mLanguage.getPhraseNBTache("7", str(nbTache), "0") + " "
                for i in range(0, nbTache):
                    if (i == 0):
                        tacheTXT = tacheTXT + listTache[i]
                    else:
                        if (i == (nbTache - 1)):
                            tacheTXT = tacheTXT + " et " + listTache[i]
                        else:
                            tacheTXT = tacheTXT + ", " + listTache[i]
        if (nbEvent == 0):
            eventTXT = self.__mLanguage.getPhraseTime("23")
        else:
            if (nbTache == 1):
                eventTXT = self.__mLanguage.getPhraseNBTache("8", str(nbEvent), "0") + " " + listEvent[0] + "."
            else:
                eventTXT = self.__mLanguage.getPhraseNBTache("9", str(nbEvent), "0") + " "
                for i in range(0, nbEvent):
                    if (i == 0):
                        eventTXT = eventTXT + listEvent[i]
                    else:
                        if (i == (nbEvent - 1)):
                            eventTXT = eventTXT + " et " + listEvent[i]
                        else:
                            eventTXT = eventTXT + ", " + listEvent[i]
        return 18, [tacheTXT, eventTXT]

    def sortieResumerAll(self):
        """
        Sortie NB  :
        - 19 -> OK
        - 20 -> Fail
        Sortie list :
            [Meteo home , Meteo Work , fete , Actu 1 , Actu 2 , Actu 3 , textSpeak , tache , agenda]
        """
        nb1, listAgendaTache = self.sortieResumerTacheAgenda()
        nb2, listActuMeto = self.sortieResumerActualite()

        if (nb2 == 11):
            text = self.__mLanguage.getPhraseResumerAll("1")
            return 20, [text, ""]
        else:
            listOut = listActuMeto + listAgendaTache
            listOut[6] = self.__mLanguage.getPhraseResumerAll("2")

            return 19, listOut

    def sortieStartRadio(self, radio: int):
        """
        1 = Europe 1
        2 = Europe 2
        3 = France Info
        4 = France Inter
        5 = France Musique
        6 = France Culture
        7 = France Bleu
        8 = Fun Radio
        9 = NRJ
        10 = RFM
        11 = Nostalgi
        12 = Skyrock
        13 = RTL
        """
        match radio:
            case 1:
                txtRadio = "Europe 1"
                sortieRadio = self.__objRadio.startEurope1()
            case 2:
                sortieRadio = self.__objRadio.startEurope2()
                txtRadio = "Europe 2"
            case 3:
                sortieRadio = self.__objRadio.startFranceInfo()
                txtRadio = "France Info"
            case 4:
                sortieRadio = self.__objRadio.startFranceInter()
                txtRadio = "France Inter"
            case 5:
                sortieRadio = self.__objRadio.startFranceMusique()
                txtRadio = "France Musique"
            case 6:
                sortieRadio = self.__objRadio.startFranceCulture()
                txtRadio = "France culture"
            case 7:
                sortieRadio = self.__objRadio.startFranceBleu()
                txtRadio = "France Bleu"
            case 8:
                sortieRadio = self.__objRadio.startFunRadio()
                txtRadio = "Fun Radio"
            case 9:
                sortieRadio = self.__objRadio.startNRJ()
                txtRadio = "NRJ"
            case 10:
                sortieRadio = self.__objRadio.startRFM()
                txtRadio = "RFM"
            case 11:
                sortieRadio = self.__objRadio.startNostalgi()
                txtRadio = "Nostalgi"
            case 12:
                sortieRadio = self.__objRadio.startSkyrock()
                txtRadio = "Skyrock"
            case 13:
                sortieRadio = self.__objRadio.startRTL()
                txtRadio = "RTL"

        if (sortieRadio == True):
            return self.__mLanguage.getPhraseOpenRadio(txtRadio, sortieRadio)
        else:
            return self.__mLanguage.getPhraseOpenRadio("", sortieRadio)

    def sortieDownloadMusic(self):
        self.__downloader.activeMusique()
        text = self.__mLanguage.getPhraseSoftware("1")
        return text

    def sortieDownloadVideo(self):
        self.__downloader.activeVideo()
        text = self.__mLanguage.getPhraseSoftware("2")
        return text

    def sortieNoDownload(self):
        return self.__mLanguage.getPhraseSoftware("3")

    def sortieOpenProjetDirect(self, projet: str):
        sortie = self.__objetArreraWork.openProjet(projet)
        if (sortie == True):
            text = self.__mLanguage.getPhraseProjetFileOpen("18", projet)
        else:
            text = self.__mLanguage.getPhraseProjetFileOpen("19", projet)
        return projet, text

    def sortieOpenTableurDirect(self, file: str):
        sortie = self.__objetArreraWork.openTableurDirectly(file)
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("57")
        else:
            text = self.__mLanguage.getPhraseWork("58")
        return text

    def sortieOpenWordDirect(self, file: str):
        sortie = self.__objetArreraWork.openWordDirectly(file)
        if (sortie == True):
            text = self.__mLanguage.getPhraseWork("59")
        else:
            text = self.__mLanguage.getPhraseWork("60")
        return text

    def getNamePenseBete(self):
        return self.__objPenseBete.getNamefile()

    def sortieCorrection(self, requette: str):
        if (self.__objetNetwork.getEtatInternet() == True):
            texte = requette.replace("corrige", "").strip()
            sortie = self.__objOrthographe.active(texte)
            if (sortie == True):
                text = self.__mLanguage.getPhraseService("3")
            else:
                text = self.__mLanguage.getPhraseService("4")
        else:
            text = self.__mLanguage.getPhraseService("7")
        return text

    def sortieResultatCalcule(self, resultat):
        return self.__mLanguage.getPhraseResultatCalcule(resultat)

    def sortieErrorCalcule(self):
        return self.__mLanguage.getPhraseService("1")

    def sortieOpenDocumentation(self):
        return self.__mLanguage.getPhraseService("2")

    def sortieHelpWorkTableur(self):
        return self.__mLanguage.getPhraseHelpArreraWork("1")

    def sortieHelpWorkTraitementTexte(self):
        return self.__mLanguage.getPhraseHelpArreraWork("2")

    def sortieHelpArreraWork(self):
        return self.__mLanguage.getPhraseHelpArreraWork("3")

    def sortieHelpWorkType(self):
        return self.__mLanguage.getPhraseHelpArreraWork("4")

    def sortieListeProjet(self):

        listProjet = self.__objetArreraWork.getListProjetCreated()

        if (len(listProjet) == 0):
            sortie = self.__mLanguage.getPhraseWork("68")
        elif (len(listProjet) == 1):
            sortie = self.__mLanguage.getPhraseWork("67")
        else:
            sortie = self.__mLanguage.getPhraseWork("66")

        for i in range(0, len(listProjet)):
            if (i == len(listProjet) - 1):
                if (len(listProjet) == 1):
                    sortie = sortie + " " + listProjet[i] + "."
                else:
                    sortie = sortie + " et " + listProjet[i] + "."
            elif (i == 0):
                sortie = sortie + " " + listProjet[i]
            else:
                sortie = sortie + " ," + listProjet[i]
        return sortie