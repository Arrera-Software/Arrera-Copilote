from librairy.dectectionOS import*
from librairy.network import*
from librairy.travailJSON import jsonWork
from config.confNeuron import confNeuron
from datetime import datetime

class gestionnaire:
    def __init__(self,confAssistant:confNeuron):
        # Var
        self.__dateStart = datetime.now().date()
        self.__breefIsLaunch = False
        # Importation des gestionnaires
        from gestionnaire.gestSocket import gestSocket
        from gestionnaire.gestLangue import gestLangue
        from gestionnaire.gestNeuron import gestNeuron
        from gestionnaire.gestHistorique import gestHistorique
        from gestionnaire.gestSTR import gestSTR
        from gestionnaire.gestFNC import gestFNC
        from gestionnaire.gestGUI import gestGUI
        from gestionnaire.gestUserSetting import gestUserSetting
        from gestionnaire.gestKeyword import gestKeyword
        from gestionnaire.gestIA import gestIA
        # Librairy
        # Importation des librairies
        from librairy.arrera_voice import CArreraVoice
        from librairy.arrera_date import CArreraDate
        # Declaration des librairies
        self.__detecteurOS = OS()
        self.__network = network()
        self.__arrVoice = CArreraVoice(self)
        self.__arrDate = CArreraDate()
        # Fichier JSON
        self.__config = confAssistant
        self.__userConf = gestUserSetting(self)
        self.__fichierFete = jsonWork("config/listFete.json")
        # Initialisation des tout les gestionnaires
        self.__gestHist = gestHistorique(self)
        self.__gestLang = gestLangue(self.__config.fichierLangue,
                                     self, [self.__config.name,
                                                       self.__config.bute,
                                                       self.__config.createur],
                                     self.__config.listFonction)
        self.__gestKeyword = gestKeyword(self.__config.fichierKeyword)
        self.__gestIA = gestIA(self)

        if self.__config.etatSocket == 1 :
           self.__gestSocket = gestSocket(self.__config.name)
        else :
            self.__gestSocket = None

        self.__gestSTR = gestSTR()

        self.__fnc = gestFNC(self)
        self.__gui = gestGUI(self)

        self.__gestHist = gestHistorique(self)
        self.__gestNeuron = gestNeuron(self)

        # Varriable
        self.__oldRequette = ""
        self.__oldSorti = ""

        # Mode interface
        self.__nameMode = {}
        self.__modeIsEnabled = False

    def boot(self):
        if self.__userConf.getHist() == 1:
            if self.__gestHist.loadHist():
                return self.__gestLang.bootWithHist()
            else :
                return self.__gestLang.bootNoHist()
        else :
            return self.__gestLang.bootNoHist()

    def getConfigFile(self):
        return self.__config

    def getOSObjet(self):
        return self.__detecteurOS

    def getArrVoice(self):
        """
        Methode qui retourne l'objet de la librairie de voice
        """
        return self.__arrVoice

    def getArrDate(self):
        return self.__arrDate

    def getLanguageObjet(self):
        return self.__gestLang

    def getKeywordObjet(self):
        return self.__gestKeyword

    def getGestNeuron(self):
        return self.__gestNeuron

    def getUserConf(self):
        return self.__userConf

    def getNetworkObjet(self):
        return self.__network

    def getSocketObjet(self):
        return self.__gestSocket

    def getGestHist(self):
        return self.__gestHist

    def getGestIA(self):
        return self.__gestIA
        
    def getName(self):
        return  self.__config.name

    def getIcon(self):
        return self.__config.icon

    def getGestFNC(self):
        """
        Methode qui retourne l'objet gestFNC
        """
        return self.__fnc

    def getGestGUI(self):
        """
        Methode qui retourne l'objet gestGUI
        """
        return self.__gui

    def getListVilleMeteo(self):
        return self.__userConf.getTowns()

    def getEtatLieuDomicile(self):
        if not self.__userConf.getLieuDomicile():
            lieuDomicile = True
        else :
            lieuDomicile = False
        return lieuDomicile

    def getEtatLieuTravail(self):
        if not self.__userConf.getLieuTravail():
            lieuTravail = True
        else :
            lieuTravail = False
        return lieuTravail
    
    def getMoteurRechercheDefault(self):
        return self.__config.moteurderecherche

    def getEmplacementFileAgenda(self)->str :
        return self.__userConf.getEventPath()

    def getEmplacemntfileTache(self)->str:
        return self.__userConf.getTaskPath()

    def getEmplacementFileHist(self)->str:
        return self.__userConf.getHistoriquePath()
    
    def getDictionnaireLogiciel(self):
        return self.__userConf.getSoft()

    def getListLogiciel(self):
        return self.__userConf.getSoft().keys()

    def getListWeb(self):
        return list(self.__userConf.getTowns().keys())
    
    def getDictionnaireWeb(self):
        return self.__userConf.getSite()

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1 
    
    def getFeteJour(self):
        date= datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.__fichierFete.getContentJsonMultiFlag(mois, jours)
    
    def setOld(self,output:str,input:str):
        """
        Methode qui peremt de sauvegarder oldSortie et oldRequette
        """
        self.__oldRequette = input 
        self.__oldSorti = output 
    
    def getOld(self):
        """
        Methode qui retourne une liste qui se presente comme sa [oldRequette,self.__oldSorti]
        """
        return [self.__oldRequette,self.__oldSorti]

    def getLinkDoc(self):
        """
        Methode pour donner le lien de la doc 
        """
        return self.__config.lienDoc
    
    def getTokenGithub(self):
        """
        Methode qui permet de recuperer les token github
        """
        return self.__userConf.getTokenGithub()

    def getAdresseDomicile(self):
        """
        Methode pour retourner l'adresse du domicile
        """
        return  self.__userConf.getAdresseDomicile()
    
    def getAdresseTravil(self) :
        """
        Methode pour retourner l'adresse du lieu de travail
        """
        return  self.__userConf.getAdresseTravail()

    def getWorkEmplacement(self):
        return self.__userConf.getWorkFolder()
    
    def getEmplacementDownload(self):
        return self.__userConf.getVideoDownloadFolder()

    def netoyageChaine(self,chaine:str):
        """
        Methode qui permet de netoyer une chaine de caractere
        """
        return self.__gestSTR.netoyage(chaine)

    def emplacementTaskFile(self):
        """
        Methode qui retourne l'emplacement du fichier de tache
        """
        return self.__userConf.getTaskPath()

    def getDateStart(self):
        return self.__dateStart

    def setBreefIsLaunch(self):
        self.__breefIsLaunch = True

    def getBreefIsLaunch(self):
        return self.__breefIsLaunch

    def updateDate(self):
        if self.__dateStart == datetime.now().date():
            return False
        else :
            self.__dateStart = datetime.now().date()
            self.__breefIsLaunch = False
            return True

    def getNameMode(self):
        return self.__nameMode

    def setNameMode(self,requette:str):
        try :
            requette = requette.replace("namemode","").strip()
            parts = requette.lstrip("|").split("|")

            result = {}
            for part in parts:
                key, value = part.split(":", 1)
                result[key] = value.lower()

            self.__nameMode = result
            return True
        except Exception as e :
            #print(e)
            return False

    def getModeIsEnabled(self)->bool:
        return self.__modeIsEnabled

    def setModeIsEnabled(self,etat:bool):
        self.__modeIsEnabled = etat