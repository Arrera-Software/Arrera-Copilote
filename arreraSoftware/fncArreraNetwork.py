#module pyhon
from tkinter import*
import random
#librairy Arrera
from librairy.travailJSON import *
from librairy.openSoftware import*
#objet de fonctionement du reseau
from ObjetsNetwork.gestion import*
from ObjetsNetwork.network import*
#differente fonctionnalitée
from arreraSoftware.fonctionLecture import *
from arreraSoftware.fonctionMeteoActu import *
from arreraSoftware.fonctionGPS import*
from arreraSoftware.fonctionTraduction import*
from arreraSoftware.fonctionArreraDownload import *
from arreraSoftware.fonctionCalculatrice import * 
from arreraSoftware.fonctionRecherche import *
from arreraSoftware.fonctionDate import *
from arreraSoftware.fonctionHorloge import*
from arreraSoftware.fonctionCalendar import *

class fncArreraNetwork:
    def __init__(self,fichierConfigurationNeuron:jsonWork,gestionNeuron:gestionNetwork,decteurOS:OS,network:network):
        #Recuperation des objet
        self.__configNeuron = fichierConfigurationNeuron
        self.__gestionNeuron = gestionNeuron
        self.__detecteurOS = decteurOS
        self.__objetNetwork =  network
        #Recuperation varriable
        self.__etatVous = self.__gestionNeuron.getVous()
        self.__user = self.__gestionNeuron.getUser()
        self.__genre = self.__gestionNeuron.getGenre()
        #Recuperation etat de la connextion internet
        etatConnextion = self.__objetNetwork.getEtatInternet()
        #initialisation objet 
        self.__fncReading = fncLecture(self.__configNeuron,self.__detecteurOS)
        self.__actu = Actu("3b43e18afcf945888748071d177b8513","6","fr","fr")
        self.__gps = GPS("19bfbee6112be5b3d9a64d4ccec72602",etatConnextion)
        self.__meteo = Meteo("19bfbee6112be5b3d9a64d4ccec72602")
        self.__itineraires = GPSItineraires()
        self.__traducteur = fncArreraTrad(self.__configNeuron)
        self.__downloader = fncArreraVideoDownload(self.__configNeuron)
        self.__calculatrice = fncCalculatrice(self.__configNeuron)  
        self.__objetRecherche = fncArreraSearch(etatConnextion)
        self.__objetDate = fncDate()
        self.__objetHorloge = fncArreraHorloge()
        self.__objetCalendar = fncArreraCalendar(self.__configNeuron,self.__gestionNeuron)
        self.__objetHorloge.setAtributJSON(self.__configNeuron)    
        self.__objetOpenSoft = OpenSoftware(self.__gestionNeuron)
        
    def reading(self):
        self.__fncReading.fenetreLecture()
        if self.__etatVous == True :
            text = "Voila "+self.__genre+" J'éspére que sa vous sera utile"
        else :
            text = "Voila "+self.__user+".Je suis toujour la si tu as besoin de moi."
        return text

    def sortieActualités(self):
        listActu = self.__actu.Actu()
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        return 3 , [listActu[nbrand1],listActu[nbrand2],listActu[nbrand3]]
        
    
    def sortieMeteo(self,ville):
        if ville == "" :
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True :
                sortieGPS = self.__gps.recuperationNameVillePosition()
                if sortieGPS == True :
                    nameVille = self.__gps.getNameVille()
                    lon = self.__gps.getlonPossition()
                    lat = self.__gps.getlatPossition()
                    sortiMeteo = self.__meteo.recuperationDataMeteo(lat,lon)
                    if sortiMeteo == True :
                        if self.__etatVous == True :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a votre localisation est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                            text =  listReponse[nbrand]
                        else :
                            nbrand = random.randint(0,1)
                            listReponse = ["La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C",
                                            "La meteo a ta localisation est de "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"]
                        
                            text =  listReponse[nbrand]
                    else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."
            else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."
        else :
            sortieGPS = self.__gps.recuperationCordonneeVille(ville)
            if sortieGPS == True :
                lat = self.__gps.getlatVille()
                lon = self.__gps.getLonVille()
                sortiMeteo = self.__meteo.recuperationDataMeteo(lat,lon)
                if  sortiMeteo == True:
                    nameVille =  ville
                    if self.__etatVous == True :
                        text= "La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"             
                    else :
                        text = "La meteo a "+nameVille+" est "+self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()+" °C"            
                else :
                        if self.__etatVous == True :
                            text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                        else :
                            text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
            else :
                if self.__etatVous == True :
                    text = "Je suis désoler "+self.__genre+" "+self.__user+". Mais je ne parvien pas a recuperer la meteo"
                else :
                    text = "Je suis désoler "+self.__user+" je n'arrive pas a savoir la meteo."  
        
        return 4 , [text,""]
    
    def sortieTemperature(self):
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True :
            lat = self.__gps.getlatPossition()
            lon = self.__gps.getlonPossition()
            sortieMeteo = self.__meteo.recuperationDataMeteo(lat,lon)
            if sortieMeteo == True :
                if self.__etatVous == True :
                    text = ["La temperature actuel dehors et de "+self.__meteo.gettemperature()+"°C",""]
                else :
                    text = ["Il fais "+self.__meteo.gettemperature()+"°C",""]     
        return 4 , text
    
    def sortieGPS(self):
        text = []
        sortieGPS = self.__gps.recuperationCordonneePossition()
        if sortieGPS == True :
            sortieGPS = self.__gps.recuperationNameVillePosition()
            if sortieGPS == True :
                lat = self.__gps.getlatPossition()
                lon = self.__gps.getlonPossition()
                nameVille = self.__gps.getNameVille()
                if self.__etatVous == True :
                    text = ["Votre localisation est latitude "+lat+" longitude "+lon+" Ce qui correspond a la ville de "+nameVille+".",""]
                else :
                    text = ["Tu es localiser a la latitude "+lat+" longitude "+lon+" .Ce qui correspond a la ville de "+nameVille+" .",""]
        return 0,text
    
    def sortieItineraires(self,loc1:str,loc2:str):
        if loc1 == "loc" :
            sortieGPS = self.__gps.recuperationCordonneePossition()
            if sortieGPS == True :
                self.__gps.recuperationNameVillePosition()
                loc = self.__gps.getNameVille()
                sortieGPS = self.__itineraires.ouvertureItineraires(loc,loc2)
        else :
            sortieGPS = self.__itineraires.ouvertureItineraires(loc1,loc2)
        return sortieGPS
    
    def ResumerActualite(self):
        #var 
        verif = False
        meteoHome = ""
        meteoWork =  ""
        feteJour = ""
        nbrand1 = random.randint(0,1)
        nbrand2 = random.randint(2,3)
        nbrand3 = random.randint(4,5)
        listOut = []

        #meteo home
        verif = self.__gps.recuperationCordonneeVille(self.__gestionNeuron.getValeurfichierUtilisateur("lieuDomicile"))
        if verif == False :
            return 11 , ["error",""]
        else :
            verif = self.__meteo.recuperationDataMeteo(self.__gps.getlatVille(),self.__gps.getLonVille())
            if verif == False :
                return 11 , ["error",""]
            else : 
                if self.__etatVous == True :
                    meteoHome = "La météo a votre domicile est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()
                else :
                    meteoHome = "La météo chez toi est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()
                
                #meteo travail
                verif = self.__gps.recuperationCordonneeVille(self.__gestionNeuron.getValeurfichierUtilisateur("lieuTravail"))
                if verif == False :
                    return 11 , ["error",""]
                else :
                    verif = self.__meteo.recuperationDataMeteo(self.__gps.getlatVille(),self.__gps.getLonVille())
                    if verif == False :
                        return 11 , ["error",""]
                    else :
                        if self.__etatVous == True :
                            meteoWork = "La météo a votre lieu de travail est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature()
                        else :
                            meteoWork = "La météo a ton boulot est "+ self.__meteo.getdescription()+" avec une température de "+self.__meteo.gettemperature() 
                        #fete du jour
                        feteJour = self.__gestionNeuron.getFeteJour()
                        #Liste des actu
                        listeActu = self.__actu.Actu()
                        #Construction de la liste

                        listOut = [meteoHome,meteoWork,feteJour,listeActu[nbrand1],listeActu[nbrand2],listeActu[nbrand3]]

                        return 12 , listOut

    def sortieTraducteur(self,langInt:str,langOut:int):
        self.__traducteur.fenetreTrad(langInt,langOut)
        
    
    def sortieDownload(self,mode):
        self.__downloader.fenetreDownload(mode)
        if self.__etatVous == True:
            if mode == "music" :
                text = "J'espère que la musique que vous avez téléchargée vous rendra heureux "+self.__genre+" ."
            else :
                text = "J'espère que la vidéo que vous avez téléchargée vous rendra heureux "+self.__genre+" ."
        else :
            if mode == "music" :
                text =  "J'espère que la musique que vous avez téléchargée vous fera plaisir "+self.__user+"."
            else :
                text =  "J'espère que la vidéo que vous avez téléchargée vous fera plaisir "+self.__user+"."
        
        return text
    
    def sortieCalculatrice(self,mode):
        if mode == "0":
            if self.__etatVous == True :
                text = "Voila votre calculatrice "+self.__genre
            else :
                text = "Voici la calculatrice"
        else :
            if mode == "1":
                if self.__etatVous == True :
                    text = "Voila votre calculatrice en mode nombre complex "+self.__genre
                else :
                    text = "Voici la calculatrice en mode complexe" 
            else :
                if self.__etatVous == True :
                    text = "Voila votre calculatrice en mode pythagore "+self.__genre
                else :
                    text = "Voici la calculatrice en mode pythagore" 
        self.__calculatrice.calculatrice(mode)
        return text
    
    def sortieOpenSoftware(self,soft):
        dictionnaireSoft = self.__gestionNeuron.getDictionnaireLogiciel()
        sortie = self.__objetOpenSoft.setName(dictionnaireSoft[soft])
        if sortie == True :
            if self.__etatVous == True :
                text = "Ok je vous ouvre "+soft+" "+self.__genre
            else :
                text = "Voici "+soft
            self.__objetOpenSoft.open()
        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir "+soft
            else :
                text = "Il un probleme qui m'empeche d'ouvrir "+soft
        return text
    
    def sortieOpenTraitementTexte(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("wordWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("wordLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de traitement de texte "+self.__genre+" "+self.__user,
                               "Je vous ai ouvert votre logiciel de traitement de texte. En quoi puis-je vous aider de plus "+self.__genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de traitement de texte " +self.__user,
                                "Je t'ai ouvert ton logiciel de traitement de texte. En quoi puis-je t'aider de plus " + self.__user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel traitement de texte"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel traitement de texte"
        return text
    
    def sortieOpenTableur(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("exelWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("exelLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de tableur "+self.__genre+" "+self.__user,
                               "Je vous ai ouvert votre logiciel de tableur. En quoi puis-je vous aider de plus "+self.__genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de tableur " +self.__user,
                                "Je t'ai ouvert ton logiciel de tableur. En quoi puis-je t'aider de plus " + self.__user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel tableur"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel tableur"
        return text
    
    def sortieOpenDiapo(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("diapoWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("diapoLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,1)
                listReponse = ["Voici votre logiciel de diaporama "+self.__genre+" "+self.__user,
                               "Je vous ai ouvert votre logiciel de présentation. En quoi puis-je vous aider de plus "+self.__genre+" ?"]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,1)
                listReponse = ["Voici ton logiciel de présentation " +self.__user,
                                "Je t'ai ouvert ton logiciel de diaporama. En quoi puis-je t'aider de plus " + self.__user + " ?"]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel de présentation"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel de présentation"
        return text
    
    def sortieOpenBrowser(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("browserWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("browserLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
                nbrand = random.randint(0,5)
                listReponse = ["Voici votre navigateur web "+self.__genre+" "+self.__user,
                               "Ok je vous ouvre votre explorateur web "+self.__genre+" "+self.__user,
                               "Voila votre explorateur web "+self.__genre,
                               "Voici votre navigateur internet "+self.__genre+" "+self.__user,
                               "Ok je vous ouvre votre explorateur internet "+self.__genre+" "+self.__user,
                               "Voila votre explorateur internet "+self.__genre,]
                text = listReponse[nbrand]
            else :
                nbrand = random.randint(0,5)
                listReponse = ["Voici ton navigateur web "+self.__genre+" "+self.__user,
                               "Ok je t'ouvre ton explorateur web "+self.__genre+" "+self.__user,
                               "Voila ton explorateur web "+self.__genre,
                               "Voici ton navigateur internet "+self.__genre+" "+self.__user,
                               "Ok je t'ouvre ton explorateur internet "+self.__genre+" "+self.__user,
                               "Voila ton explorateur internet "+self.__genre,]
                text = listReponse[nbrand]

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre navigateur internet"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton navigateur internet"
        return text
    
    def sortieOpenNote(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("noteWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("noteLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
               text = "Voici vos notes "+self.__genre
            else :
                text = "Voici tes notes "+self.__user

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir vos notes"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir tes notes"
        return text
    
    def sortieOpenMusic(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("musicWindows")
        else :
            if etatWindows == False and etatLinux == True :
                logiciel = self.__gestionNeuron.getValeurfichierUtilisateur("musicLinux")
        sortie = self.__objetOpenSoft.setName(logiciel)
        self.__objetOpenSoft.open()
        if sortie == True :
            if self.__etatVous == True :
               text = "Voici "+self.__genre+" ,bonne écoute"
            else :
                text = "Voici "+self.__user+" ,bonne écoute"

        else :
            if self.__etatVous == True :
                text = "Je suis desoler "+self.__genre+" .Mais il a un probleme qui m'empeche d'ouvrir votre logiciel d'écoute musicale"
            else :
                text = "Il un probleme qui m'empeche d'ouvrir ton logiciel d'écoute musicale"
        return text
    
    def sortieOpenYoutube(self):
        webbrowser.open("https://www.youtube.com/")
        if self.__etatVous == True :
            text = "Ok, je vous ai ouvert YouTube."
        else :
            text = "Ok, je t'ai ouvert YouTube."
        
        return text
    
    def sortieOpenCloud(self):
        lien= self.__gestionNeuron.getValeurfichierUtilisateur("lienCloud")
        webbrowser.open(lien)
        if self.__etatVous == True :
            text = "Ok, je vous ai ouvert votre stokage distant."
        else :
            text = "Ok, je t'ai ouvert ton stokage distant."
        
        return text
    
    def sortieOpenSite(self,site):
        dictionnaireSoft = self.__gestionNeuron.getDictionnaireWeb()
        webbrowser.open(dictionnaireSoft[site])
        if self.__etatVous == True :
            text = "Ok je vous ouvre "+site+" "+self.__genre
        else :
            text = "Voici "+site  
            
    def sortieRechercheSimple(self,requette:str):
        moteurDefault = self.__gestionNeuron.getMoteurRechercheDefault()
        moteurUser = self.__gestionNeuron.getValeurfichierUtilisateur("moteurRecherche")
        recherche = requette.replace("search","")
        recherche = recherche.replace("recherche","")
        if moteurUser == "":
            moteur = moteurDefault
        else :
            moteur = moteurUser
    
        match moteur :
            case "duckduckgo" :
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "google" :
                sortieRecherche = self.__objetRecherche.googleSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "qwant" :
                sortieRecherche = self.__objetRecherche.QwantSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "ecosia" :
                sortieRecherche = self.__objetRecherche.EcosiaSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "brave" :
                sortieRecherche = self.__objetRecherche.braveSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case "bing":
                sortieRecherche = self.__objetRecherche.bingSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Voici votre recherche. Voulez vous rechercher autre chose ?"
                else :
                    text = "Voici ta recherche "
            case other :
                sortieRecherche = self.__objetRecherche.duckduckgoSearch(recherche)
                if self.__etatVous ==  True:
                    text = "Je vous ai fais votre recherche sur duckduckgo car il un probleme avec mes fichier de configuration"
                else :
                    text = "Je t'ai fais ta recherche sur duckduckgo car il un probleme avec mes fichier de configuration"
        if sortieRecherche == False :
            if self.__etatVous ==  True:
                return "Je suis désoler "+self.__genre+" . Mais je peux pas faire votre recherche si je ne suis pas connecter a internet"
            else :
                return "Désoler "+self.__user+" je suis pas connecter a internet"
        else :
            return text
    
    def sortieGrandRecherche(self,requette:str):
        recherche = requette.replace("bigsearch","")
        recherche = recherche.replace("grand recherche","")
        sortieRecheche = self.__objetRecherche.GrandRecherche(recherche)
        if sortieRecheche == True :
            if self.__etatVous == True :
                text = "Voici le resultat de votre recherche sur plusieur moteur de recherche "+self.__genre
            else :
                text = "Voici ton resultat " 
        else :
            if self.__etatVous == True :
                text = "Votre appareil n'est pas connecter internet "+self.__genre
            else :
                text = "Je suis desoler mais je suis pas connecter a internet"
                
        return text
    
    def sortieHeure(self):
        self.__objetDate.rafraichisement()
        heure = self.__objetDate.heure()
        minute = self.__objetDate.minute()
        return "Il est "+heure+" heure "+minute + "  minute" 
    
    def sortieDate(self):
        self.__objetDate.rafraichisement()
        jour = self.__objetDate.jour()
        mois = self.__objetDate.mois()
        annes = self.__objetDate.annes()
        return "On est le "+jour+" "+mois+" "+annes
    
    def sortieOpenChrono(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance le chronométre "+self.__genre
        else :
            text = "Okay je te lance le chronométre"
        self.__objetHorloge.modeChrono()
        return text

    def sortieOpenHorloge(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance l'horloge "+self.__genre
        else :
            text = "Okay je te lance l'horloge"
        self.__objetHorloge.modeHorloge()
        return text
    
    def sortieOpenSimpleMinuteur(self):
        if self.__etatVous == True :
            text = "Tres bien je vous lance l'application minuteur "+self.__genre
        else :
            text = "Okay je te lance l'application minuteur"
        self.__objetHorloge.modeMinuteur()
        return text   
    
    def sortieAjoutEvent(self):
        self.__objetCalendar.addEvenemnt()
        return "Ok"    
    
    def sortieSupprEvent(self):
        self.__objetCalendar.supprEvenement()
        return "Ok"    
    
    def sortieEvenementDay(self):
        nb , listEvent = self.__objetCalendar.checkEvenement()  
        if nb == 0 :
            if self.__etatVous == True :
                return "Vous avez aucun évenement aujourd'hui"
            else :
                return "Tu as rien de prévu aujourd'hui"  
        else :
            if self.__etatVous == True :
                text = "Vous avez "+str(nb)+" prévu évenement aujourd'hui "
            else :
                text = "Tu as "+str(nb)+" prévu évenement aujourd'hui "
            if nb > 1 :
                text = text + "qui sont "
            else :
                text = text + "qui est "
            for i in range(0,nb) :
                if i == nb-1:
                    text = text + listEvent[i] + "."  
                else :
                    if i == nb-2 :
                        text = text + listEvent[i] + " et "
                    else :
                        text = text + listEvent[i] + "," 
                
            
            return text