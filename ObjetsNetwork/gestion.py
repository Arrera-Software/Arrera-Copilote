from datetime import datetime, timedelta
from ObjetsNetwork.gestSocket import *
from librairy.dectectionOS import*
from ObjetsNetwork.CAlanguage import *
from ObjetsNetwork.network import*
from ObjetsNetwork.enabledNeuron import*
from ObjetsNetwork.userConf import *
from librairy.asset_manage import resource_path


class gestionNetwork:
    def __init__(self,configFile:str,userConf:userConf):
        # Fichier JSON
        self.__configFile = jsonWork(configFile)
        self.__fileUser = jsonWork(userConf.getUserSettingPath())
        self.__fichierFete = jsonWork(self.__configFile.lectureJSON("fileFete"))
        self.__userConf = userConf
        # Objet
        self.__detecteurOS = OS()
        if OS().osMac():
            self.__mLanguage = CAlanguage(resource_path(self.__configFile.lectureJSON("moduleLanguage")),
                                          self.__fileUser,[self.__configFile.lectureJSON("name"),
                                                           self.__configFile.lectureJSON("bute"),
                                                           self.__configFile.lectureJSON("createur")],
                                          self.getListFonction())
        else:
            self.__mLanguage = CAlanguage(self.__configFile.lectureJSON("moduleLanguage"),
                                          self.__fileUser,[self.__configFile.lectureJSON("name"),
                                                           self.__configFile.lectureJSON("bute"),
                                                           self.__configFile.lectureJSON("createur")],
                                          self.getListFonction())
        self.__etatNeuron = CArreraEnabledNeuron(self.__configFile)
        self.__network = network()
        self.__serveurSocket = socketAssistant(self.__configFile.lectureJSON("name"),self.__etatNeuron.getSocket())
        # Varriable
        self.__oldRequette = ""
        self.__oldSorti = ""

    def getConfigFile(self):
        return self.__configFile

    def getOSObjet(self):
        return self.__detecteurOS

    def getLanguageObjet(self):
        return self.__mLanguage

    def getEtatNeuronObjet(self):
        return self.__etatNeuron

    def getNetworkObjet(self):
        return self.__network

    def getSocketObjet(self):
        return self.__serveurSocket
        
    def getName(self):
        return  str(self.__configFile.lectureJSON("name"))
    
    def getNbListFonction(self):
        return len(self.__configFile.lectureJSONList("listFonction"))
    
    def getListFonction(self):
        return self.__configFile.lectureJSONList("listFonction")
    
    def getnbVilleMeteo(self):
        return int(self.__configFile.lectureJSON("nombreVilleMeteo"))
    
    def getListVilleMeteo(self):
        
        return self.__fileUser.lectureJSONList("listVille")

    def getEtatLieuDomicile(self):
        if self.__configFile.lectureJSON("lieuDomicile") == "1":
            lieuDomicile = True
        else :
            lieuDomicile = False
        return lieuDomicile

    def getEtatLieuTravail(self):
        if self.__configFile.lectureJSON("lieuTravail") == "1":
            lieuTravail = True
        else :
            lieuTravail = False
        return lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.__fileUser.lectureJSON(flag)
    
    def getMoteurRechercheDefault(self):
        return str(self.__configFile.lectureJSON("moteurRechercheDefault"))

    def getEmplacementFileAgenda(self)->str :
        return self.__userConf.getEventPath()

    def getEmplacemntfileTache(self)->str:
        return self.__userConf.getTaskPath()

    def getEmplacementFileHist(self)->str:
        return self.__userConf.getTaskPath()
    
    def getDictionnaireLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        etatMac = self.__detecteurOS.osMac()
        if etatWindows == True and etatLinux == False :
            return self.__fileUser.lectureJSONDict("dictSoftWindows")
        elif etatWindows == False and etatLinux == True or etatMac == True:
            return self.__fileUser.lectureJSONDict("dictSoftLinux")
        else :
            return None

    def getListLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        etatMac = self.__detecteurOS.osMac()
        if etatWindows == True and etatLinux == False and etatMac == False:
            return list(self.__fileUser.lectureJSONDict("dictSoftWindows").keys())
        elif etatWindows == False and etatLinux == True or etatMac == True :
            return list(self.__fileUser.lectureJSONDict("dictSoftLinux").keys())
        else :
            return None

    def getListWeb(self):
        return list(self.__fileUser.lectureJSONDict("dictSite").keys())
    
    def getDictionnaireWeb(self):
        return self.__fileUser.lectureJSONDict("dictSite")

    def verrifSortie(self,sortieNeuron):
        if sortieNeuron == "":
            return 0
        else :
            return 1 
    
    def getFeteJour(self):
        date= datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.__fichierFete.lectureJSONMultiFlag(mois,jours)
    
    def getEmplacementSoftwareWindows(self):
        return self.__configFile.lectureJSON("emplacementSoftWindows")
    
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
        return self.__configFile.lectureJSON("lienDoc")
    
    def getTokenGithub(self):
        """
        Methode qui permet de recuperer les token github
        """
        return self.__fileUser.lectureJSON("tokenGithub")

    def getAdresseDomicile(self):
        """
        Methode pour retourner l'adresse du domicile
        """
        return  self.__fileUser.lectureJSON("adresseDomicile")
    
    def getAdresseTravil(self) :
        """
        Methode pour retourner l'adresse du lieu de travail
        """
        return  self.__fileUser.lectureJSON("adresseTravail")

    def getWorkEmplacement(self):
        return self.__fileUser.lectureJSON("wordFolder")
    
    def getEmplacementDownload(self):
        return self.__fileUser.lectureJSON("videoDownloadFolder")