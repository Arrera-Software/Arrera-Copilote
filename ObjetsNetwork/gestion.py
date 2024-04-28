import datetime
from librairy.travailJSON import *
from librairy.dectectionOS import*

class gestionNetwork:
    def __init__(self,fileUser:jsonWork,ConfigFile:jsonWork,detecteurOS:OS,fileFete:jsonWork):
        self.__fileUser = fileUser
        self.__configFile = ConfigFile
        self.__fichierVille = fileFete
        self.__vous = False
        self.__lieuDomicile = False
        self.__lieuTravail = False
        self.__genre =""
        self.__name  =""
        self.__user =""
        self.__bute =""
        self.__listFonction = []
        self.__createur =""
        self.__nbDiscution =0
        self.__nbVilleMeteo = 0
        self.__listVille = []
        self.__detecteurOS = detecteurOS
        self.__moteurRechercheDefault = ""
    
    def setVous(self):
        if self.__configFile.lectureJSON("utilisationVous") == "1":
            self.__vous = True
        else :
            self.__vous = False
    
    def setGenre(self):
        self.__genre =  self.__fileUser.lectureJSON("genre")
        
    def setName(self):
        self.__name =  self.__configFile.lectureJSON("name").lower
        
    def setUser(self):
        self.__user =  self.__fileUser.lectureJSON("user")
    
    def setBute(self):
        self.__bute =   self.__configFile.lectureJSON("bute")
    
    def setCreateur(self):
        self.__createur = self.__configFile.lectureJSON("createur")
    
    def setListFonction(self):
        self.__listFonction = self.__configFile.lectureJSON("listFonction")
      
    def setLieu(self):
        if self.__configFile.lectureJSON("lieuDomicile") == "1":
            self.__lieuDomicile = True
        else :
            self.__lieuDomicile = False
        if self.__configFile.lectureJSON("lieuTravail") == "1":
            self.__lieuTravail = True
        else :
            self.__lieuTravail = False
        
    def addDiscution(self):
        self.__nbDiscution =+ 1
    
    
    def setAll(self):
        if self.__configFile.lectureJSON("utilisationVous") == "1":
            self.__vous = True
        else :
            self.__vous = False
        if self.__configFile.lectureJSON("lieuDomicile") == "1":
            self.__lieuDomicile = True
        else :
            self.__lieuDomicile = False
        if self.__configFile.lectureJSON("lieuTravail") == "1":
            self.__lieuTravail = True
        else :
            self.__lieuTravail = False
        self.__genre =  self.__fileUser.lectureJSON("genre")
        self.__name =  str(self.__configFile.lectureJSON("name")).lower()
        self.__user =  str(self.__fileUser.lectureJSON("user"))
        self.__bute =   self.__configFile.lectureJSON("bute")
        self.__createur =   str(self.__configFile.lectureJSON("createur"))
        self.__listFonction = self.__configFile.lectureJSON("listFonction")
        self.__nbVilleMeteo = int(self.__configFile.lectureJSON("nombreVilleMeteo"))
        self.__moteurRechercheDefault = str(self.__configFile.lectureJSON("moteurRechercheDefault"))
    
    def setVilleMeteo(self):
        self.__listVille = self.__fileUser.lectureJSONList("listVille")
    
    def getVous(self):
        return bool(self.__vous)
    
    def getGenre(self):
        return str(self.__genre) 
        
    def getName(self):
        return  str(self.__name )
        
    def getUser(self):
        return  str(self.__user )
    
    def getBute(self):
        return  str(self.__bute )
    
    def getCreateur(self):
        return  str(self.__createur )
        
    def getDiscution(self):
        return  str(self.__nbDiscution)

    def getNbDiscution(self):
        return int(self.__nbDiscution)
    
    def getNbListFonction(self):
        return len(self.__listFonction)
    
    def getListFonction(self):
        return self.__listFonction
    
    def getnbVilleMeteo(self):
        return self.__nbVilleMeteo
    
    def getListVilleMeteo(self):
        return self.__listVille

    def getEtatLieuDomicile(self):
        return self.__lieuDomicile

    def getEtatLieuTravail(self):
        return self.__lieuTravail
    
    def getValeurfichierUtilisateur(self,flag:str):
        return self.__fileUser.lectureJSON(flag)
    
    def getMoteurRechercheDefault(self):
        return self.__moteurRechercheDefault
    
    def getDictionnaireLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return self.__fileUser.lectureJSONDict("dictSoftWindows")
        else :
            if etatWindows == False and etatLinux == True :
                return self.__fileUser.lectureJSONDict("dictSoftLinux")
    
    def getListLogiciel(self):
        etatWindows = self.__detecteurOS.osWindows()
        etatLinux = self.__detecteurOS.osLinux()
        if etatWindows == True and etatLinux == False :
            return list(self.__fileUser.lectureJSONDict("dictSoftWindows").keys())
        else :
            if etatWindows == False and etatLinux == True :
                return list(self.__fileUser.lectureJSONDict("dictSoftLinux").keys())
            
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
        date= datetime.datetime.now()
        jours = str(date.day)
        mois = str(date.month)
        return self.__fichierVille.lectureJSONMultiFlag(mois,jours)
    
    def getEmplacementSoftwareWindows(self):
        return self.__configFile.lectureJSON("emplacementSoftWindows")