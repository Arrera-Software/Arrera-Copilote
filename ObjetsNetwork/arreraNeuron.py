import threading as th
from neuron.chatBots import*
from ObjetsNetwork.formule import*
from neuron.service import*
from neuron.API import*
from neuron.software import*
from neuron.open import *
from neuron.search import*
from neuron.time import*
from neuron.codehelp import*
from neuron.work import*

class ArreraNetwork :
    def __init__(self,fichierConfiguration:str):
        # Declaration des diferente var 
        self.__listOut =  [] 
        self.__valeurOut = 0
        self.__networkRunning = True
        #Ouverture fichier de configuration
        self.__configNeuron = jsonWork(fichierConfiguration)
        self.__fichierUtilisateur = jsonWork(self.__configNeuron.lectureJSON("fileUser"))
        self.__fichierVille = jsonWork(self.__configNeuron.lectureJSON("fileFete"))
        # Gestionnaire
        self.__gestionnaire = gestionNetwork(fichierConfiguration)
        # Partie serveur
        self.__socket = self.__gestionnaire.getSocketObjet()
        #initilisation du gestionnaire du reseau de neuron
        self.__fonctionAssistant = fncArreraNetwork(self.__gestionnaire)
        self.__historique = CHistorique(self.__fonctionAssistant,self.__gestionnaire)
        self.__formuleNeuron = formule(self.__gestionnaire,self.__historique)
        #recuperation etat du reseau
        self.__etatReseau = self.__gestionnaire.getNetworkObjet().getEtatInternet()
        #initilisation des neuron
        self.__chatBot = neuroneDiscution(self.__fonctionAssistant,self.__gestionnaire,self.__historique,self.__formuleNeuron)
        self.__service = neuroneService(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__api = neuroneAPI(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__software = neuroneSoftware(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__open = neuroneOpen(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__search = neuroneSearch(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__time = neuroneTime(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__codehelp = neuroneCodehelp(self.__fonctionAssistant,self.__gestionnaire,self.__historique)
        self.__work = neuronWork(self.__fonctionAssistant,self.__gestionnaire,self.__historique)

    def getNeuronRunning(self):
        return self.__networkRunning

    def boot(self,mode:int):
        """_summary_

        Args:
            mode (int): 1.no hist | 2. Hist

        Returns:
            _type_: _description_
        """
        hour = datetime.now().hour
        if mode == 1 :
            text= self.__formuleNeuron.bootNoHist(hour)
        else :
            text= self.__formuleNeuron.bootWithHist(hour)
        self.__gestionnaire.setOld("boot","boot")
        return str(text)
    
    def shutdown(self):
        self.__historique.saveHistorique()
        hour = datetime.now().hour
        text = self.__formuleNeuron.aurevoir(hour)
        if (self.__socket.getServeurOn() == True):
            self.__socket.stopSocket()
        return str(text)
    
    def getListSortie(self)->list :
        return self.__listOut 

    def getValeurSortie(self)->int :
        """
        0 : Aucun sortie
        1 : Sortie normale
        3 : Sortie actu
        4 : Meteo / temperature / GPS
        5 : Sortie avec fenetre tkinter
        6 : Erreur actu
        7 : Ouverture de fichier
        8 : Fermeture de fichier
        9 : Lecture fichier
        10 : Creation d'un projet
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        13 : Lecture tableur
        14 : Ouverture d'un projet
        15 : Arret de l'assistant
        16 : Creation d'un fichier dans un projet
        17 : Affichage aide
        18 : Resumer tache / agenda
        19 : Resumer all ok 
        20 : Resumer all fail
        21 : Close projet
        """
        return self.__valeurOut
    
    def getTableur(self):
        return self.__fonctionAssistant.getTableurOpen()
    
    def getWord(self):
        return self.__fonctionAssistant.getWordOpen()

    def getProject(self):
        return self.__fonctionAssistant.getProjectOpen()

    def getUserData(self):
        return self.__gestionnaire.getLanguageObjet().getDataUser()

    def neuron(self,var:str) :
        # Var local
        requette = chaine.netoyage(str(var))
        # Var de l'objet
        self.__valeurOut = 0
        self.__listOut =  []
        # Service
        self.__service.neurone(requette)
        self.__valeurOut = self.__service.getValeurSortie()
        if self.__valeurOut == 0 :
            #software
            self.__software.neurone(requette)
            self.__valeurOut = self.__software.getValeurSortie()
            if self.__valeurOut == 0 :
                #time
                self.__time.neurone(requette)
                self.__valeurOut = self.__time.getValeurSortie()

                if self.__valeurOut == 0 :
                    #code help
                    self.__codehelp.neurone(requette)
                    self.__valeurOut = self.__codehelp.getValeurSortie()
                    if (self.__valeurOut == 0 ):
                        #work
                        self.__work.neurone(requette)
                        self.__valeurOut = self.__work.getValeurSortie()
                        if (self.__valeurOut == 0 ):
                            #open
                            self.__open.neurone(requette)
                            self.__valeurOut = self.__open.getValeurSortie()
                            if self.__valeurOut == 0 :
                                #search
                                if self.__etatReseau == True :
                                    self.__search.neurone(requette)
                                    self.__valeurOut = self.__search.getValeurSortie()
                                    print(self.__valeurOut)
                                else :
                                    self.__valeurOut = 0

                                if self.__valeurOut == 0 :
                                    self.__chatBot.neurone(requette)
                                    self.__valeurOut = self.__chatBot.getValeurSortie()

                                    if self.__valeurOut == 0 :
                                        #api
                                        if self.__etatReseau == True :
                                            self.__api.neurone(requette)
                                            self.__valeurOut = self.__api.getValeurSortie()
                                        else :
                                            self.__valeurOut = 0

                                        if self.__valeurOut == 0 :
                                            if (("stop" in requette) or ("au revoir" in requette)
                                                or ("quitter" in requette) or ("bonne nuit" in requette)
                                                or ("adieu" in requette) or ("bonne soirée" in requette)
                                                or ("arreter" in requette)) :
                                                self.__listOut = [self.shutdown(),""]
                                                self.__valeurOut = 15
                                            else :
                                                self.__valeurOut = 0
                                                self.__listOut = [self.__formuleNeuron.nocomprehension(),""]
                                        else :
                                            self.__listOut = self.__api.getListSortie()
                                    else :
                                        self.__listOut = self.__chatBot.getListSortie()
                                else :
                                    self.__listOut = self.__search.getListSortie()
                            else :
                                self.__listOut = self.__open.getListSortie()
                        else :
                            self.__listOut = self.__work.getListSortie()
                    else :
                        self.__listOut = self.__codehelp.getListSortie()
                else :
                    self.__listOut = self.__time.getListSortie()
            else :
                self.__listOut = self.__software.getListSortie()
        else :
            self.__listOut = self.__service.getListSortie()

        #Sauvegarde de la sortie et de l'entrée
        if ((self.__valeurOut  == 3) or (self.__valeurOut == 12) or (self.__valeurOut == 11)) :
            self.__gestionnaire.setOld("requette api",requette)
        else :
            self.__gestionnaire.setOld(self.__listOut[0],requette)