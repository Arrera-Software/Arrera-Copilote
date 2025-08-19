from librairy.travailJSON import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*
import speech_recognition as sr
from playsound3 import playsound as pl

class CArreraGazelle :
    def __init__(self,emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,soundMicro:str=""):
        # Fichier json
        self.__fileJsonUser = jsonWork(emplacementJsonUser)
        self.__fileJsonNeuronNetwork = jsonWork(emplacementJsonNeuronNetwork)
        self.__fileJsonAssistant = jsonWork(emplacementJsonAssistant)
        self.__soundMicro = soundMicro
        self.__record = ""
        self.__stateRecordTigerWord = False
        # Objet 
        objOS = OS()
        self.__windowsOS = objOS.osWindows()
        self.__linuxOS = objOS.osLinux()
        self.__appleOS = objOS.osMac()

        if not self.__linuxOS==False and self.__windowsOS :
            self.__softWin = gestionSoftWindows(self.__fileJsonNeuronNetwork.lectureJSON("emplacementSoftWindows"))
    
    def changeUserName(self,newName:str):
        self.__fileJsonUser.EcritureJSON("user",newName)
    
    def changeUserGenre(self,newGenre:str):
        self.__fileJsonUser.EcritureJSON("genre",newGenre)
    
    def ajoutVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if mode == 1:
            self.__fileJsonUser.EcritureJSON("lieuDomicile",ville)
            return True
        else :
            if mode==2:
                self.__fileJsonUser.EcritureJSON("lieuTravail",ville)
                return True
            else :
                if mode==3:
                    self.__fileJsonUser.EcritureJSONList("listVille",ville)
                    return True
                else :
                    return False
    
    def supprVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if (mode == 1 ):
            self.__fileJsonUser.suppressionJson("lieuDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("lieuTravail")
                return True
            else :
                if ((mode==3)and(ville != "")):
                    self.__fileJsonUser.suppressionJsonList("listVille",ville)
                    return True
                else :
                    return False
    
    def getMeteoSave(self):
        listeMeteo = self.__fileJsonUser.lectureJSONList("listVille")

        return listeMeteo

    def ajoutGPSAdresse(self,mode:int,adresse:str):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.EcritureJSON("adresseDomicile",adresse)
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.EcritureJSON("adresseTravail",adresse)
                return True
            else :
                return False
    
    def supprGPSAdresse(self,mode:int):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.suppressionJson("adresseDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("adresseTravail")
                return True
            else :
                return False

    def getGPSAdresseIsSet(self,mode:int):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            if (self.__fileJsonUser.lectureJSON("adresseDomicile")!=""):
                return True
            else :
                return False
        else :
            if (mode==2):
                if (self.__fileJsonUser.lectureJSON("adresseTravail")!=""):
                    return True
                else :
                    return False
            else :
                return False


    def addSoft(self, name: str) -> bool:
        """
        Ajoute un logiciel à la liste des logiciels connus par l'assistant.

        Args:
            name: Le nom du logiciel à ajouter

        Returns:
            bool: True si le logiciel a été ajouté avec succès, False sinon
        """
        # Si on est sous Windows et que l'emplacement des logiciels n'est pas défini
        if (not self.__linuxOS and not self.__appleOS and
                self.__windowsOS and
                self.__fileJsonNeuronNetwork.lectureJSON("emplacementSoftWindows") == ""):
            self.__fileJsonNeuronNetwork.EcritureJSON("emplacementSoftWindows", self.__softWin.setEmplacementSoft())

        # Si le nom du logiciel est vide, on ne peut pas continuer
        if not name:
            return False

        # Traitement pour Linux
        if self.__linuxOS and not self.__windowsOS and not self.__appleOS:
            # Demande à l'utilisateur si le programme est dans son répertoire home
            reponse = messagebox.askquestion(
                "Choix répertoire",
                "Le programme se trouve-t-il dans votre répertoire /home ?",
                icon="question"
            )

            # Définir le répertoire initial en fonction de la réponse
            initial_dir = os.path.expanduser("~") if reponse == "yes" else "/bin"

            # Boîte de dialogue pour sélectionner le fichier
            command = filedialog.askopenfilename(
                title="Sélectionner un programme",
                initialdir=initial_dir,
                filetypes=[("Tous les fichiers", "*")]
            )

            # Si l'utilisateur annule la sélection
            if not command:
                return False

            # Enregistrer le logiciel dans le fichier JSON pour Linux
            self.__fileJsonUser.EcritureJSONDictionnaire("dictSoftLinux", name, command)
            return True

        # Traitement pour Windows
        elif not self.__linuxOS and self.__windowsOS and not self.__appleOS:
            self.__softWin.setName(name)
            if self.__softWin.saveSoftware():
                self.__fileJsonUser.EcritureJSONDictionnaire("dictSoftWindows", name, self.__softWin.getName())
                return True
            return False
        elif not self.__linuxOS and not self.__windowsOS and self.__appleOS:
            reponse = messagebox.askquestion(
                "Choix répertoire",
                "Votre application se trouve-t-elle dans le dossier Applications ?",
                icon="question"
            )
            if reponse == "yes":
                reponse = messagebox.askquestion(
                    "Choix répertoire",
                    "Votre application se trouve-t-elle dans le dossier Applications utilisateur ?",
                    icon="question"
                )
                if reponse == "yes":
                    initial_dir = "/Users/Applications"
                else :
                    initial_dir = "/Applications"
            else:
                initial_dir = "/"

            command = filedialog.askopenfilename(
                title="Sélectionner un programme",
                initialdir=initial_dir,
                filetypes=[("Tous les fichiers", "*")]
            )

            if not command:
                return False

            # Enregistrer le logiciel dans le fichier JSON pour Linux
            self.__fileJsonUser.EcritureJSONDictionnaire("dictSoftLinux", name, command)
            return True

        else :
            # Si le système d'exploitation n'est ni Linux ni Windows ou Apple
            return False

    def supprSoft(self,name:str):
        """
        1 : Normal
        2 : Presentation
        3 : Navigateur
        4 : Musique
        5 : note
        """
        flags = ""

        if not self.__linuxOS and self.__windowsOS and not self.__appleOS:
            flags = "dictSoftWindows"
        elif self.__linuxOS or self.__appleOS and not self.__windowsOS:
            flags = "dictSoftLinux"
        else :
            return False

        self.__fileJsonUser.supprJSONList(flags,name)
        if not self.__linuxOS and not self.__appleOS and self.__windowsOS:
            self.__softWin.supprSoft(name)
            return True
        elif self.__linuxOS or self.__appleOS and not self.__windowsOS:
            return True

        return False
        
    def getListSoft(self):
        listSortie = []
        # Creation listFlag 
        if not self.__linuxOS and self.__windowsOS:
            flags = "dictSoftWindows"
        elif self.__linuxOS or self.__appleOS and not self.__windowsOS:
            flags = "dictSoftLinux"
        else :
            return ["error","error"]

        # Recuperation du dictionnaire
        dictSoft = self.__fileJsonUser.lectureJSONDict(flags)

        if (len(dictSoft)!=0) :
            listSortie = listSortie+(list(dictSoft.keys()))

        return listSortie

    def addSite(self,mode:int,name:str,link:str):
        """
        1 : normal
        2 : lien cloud
        """
        if (link == "") :
            return False

        match mode :
            case 1 :
                if (name==""):
                    return False 
                self.__fileJsonUser.EcritureJSONDictionnaire("dictSite",name,link)
                return True
            case 2 : 
                self.__fileJsonUser.EcritureJSON("lienCloud",link)
                return True
    
    def supprSite(self,mode:int,name:str):
        """
        1 : normal
        2 : lien cloud
        """
        match mode :
            case 1 :
                if (name==""):
                    return False 
                self.__fileJsonUser.supprJSONList("dictSite",name)
                return True
            case 2 : 
                self.__fileJsonUser.suppressionJson("lienCloud")
                return True
    
    def getListSite(self):
        listSortie = []
        """
        if (self.__fileJsonUser.lectureJSON("lienCloud")!=""):
            listSortie.append("Cloud")
        """
        dictSite = self.__fileJsonUser.lectureJSONDict("dictSite")
        if (len(dictSite)==0):
            return listSortie
        else :
            return listSortie + list(dictSite.keys())

    def changeMoteur(self,moteur:str):
        self.__fileJsonUser.EcritureJSON("moteurRecherche",moteur)
        return True
    
    def changeTheme(self,theme:str):
        self.__fileJsonAssistant.EcritureJSON("theme",theme)
        return True

    def getTheme(self):
        return self.__fileJsonAssistant.lectureJSON("theme")
    
    def changeSoundMicro(self,enable:bool):
        if(enable==False):
            self.__fileJsonAssistant.EcritureJSON("soundMicro","0")
            return True
        else :
            if(enable==True):
                self.__fileJsonAssistant.EcritureJSON("soundMicro","1")
                return True
            else :
                return False
    
    def getSoundMicroAsEnable(self):
        sortie = self.__fileJsonAssistant.lectureJSON("soundMicro")
        if (sortie=="1"):
            return True
        else :
            return False
    
    def getOS(self):
        if ((self.__linuxOS==True) and (self.__windowsOS==False)):
            return "linux"
        else :
            if ((self.__linuxOS==False) and (self.__windowsOS==True)):
                return "windows"
            else :
                return "other"


    def setWorkFolder(self):
        folder = filedialog.askdirectory(title="Choisir un dossier de travail")
        if folder :
            self.__fileJsonUser.EcritureJSON("wordFolder",folder)
            return True
        else :
            return False

    def setVideoDownloadFolder(self):
        folder = filedialog.askdirectory(title="Choisir un dossier pour Arrera Video Download")
        if folder :
            self.__fileJsonUser.EcritureJSON("videoDownloadFolder",folder)
            return True
        else :
            return False

    def supprWorkFolder(self):
        self.__fileJsonUser.EcritureJSON("wordFolder", "")
        return True

    def supprVideoDownloadFolder(self):
        self.__fileJsonUser.EcritureJSON("videoDownloadFolder", "")
        return True

    def workFolderExist(self):
        if (self.__fileJsonUser.lectureJSON("wordFolder")!=""):
            return True
        else :
            return False

    def downloadFolderExist(self):
        if (self.__fileJsonUser.lectureJSON("videoDownloadFolder")!=""):
            return True
        else :
            return False

    def recordTrigerWord(self):
        if (self.__soundMicro):
            pl(self.__soundMicro)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            self.__record = text
            self.__stateRecordTigerWord = True
            return True
        except sr.UnknownValueError:
            self.__stateRecordTigerWord = False
            return False
        except sr.RequestError as e:
            self.__stateRecordTigerWord = False
            return False

    def getStateRecordTigerWord(self):
        return self.__stateRecordTigerWord

    def getRecordTrigerWord(self):
        return self.__record

    def saveRecordTrigerWord(self):
        self.__fileJsonAssistant.EcritureJSONList("listWord",self.__record)
        self.__record = ""
        return True

    def getNbTrigerWord(self):
        return len(self.__fileJsonAssistant.lectureJSONList("listWord"))

    def supprTrigerWord(self,word):
        self.__fileJsonAssistant.suppressionJsonList("listWord",word)
        return True

    def getTrigerWord(self):
        return self.__fileJsonAssistant.lectureJSONList("listWord")