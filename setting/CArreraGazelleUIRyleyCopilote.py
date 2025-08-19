from librairy.arrera_tk import *
from setting.arreraGazelle import*
from tkinter.messagebox import*
from typing import Union
from librairy.asset_manage import resource_path
import threading as th

class CArreraGazelleUIRyleyCopilote :
    def __init__(self,atk:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],
                 emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,
                 emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet

        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)

        # Var qui contient les thead
        self.__threadSaveVoicePrint = th.Thread()

        # Mise de la fenetre dans un atribut

        self.__windows = windows
        self.__arrTK = atk

        # Varriable
        tailleTitle = 27
        tailleMain = 23
        self.__varMoteurRecherce = StringVar(self.__windows)
        self.__varGenre = StringVar(self.__windows)
        self.__varChoixLieu = StringVar(self.__windows)
        self.__varSupprLieu = StringVar(self.__windows)
        self.__varSupprSoft = StringVar(self.__windows)
        self.__varChoixSite =  StringVar(self.__windows)
        self.__varSupprSite =  StringVar(self.__windows)
        self.__varChoixTheme  =  StringVar(self.__windows)
        self.__varSonsEmis =  StringVar(self.__windows)
        self.__varChoixSupprMeteo = StringVar(self.__windows)
        startX = 60    # Position X de départ
        startY = 25 # Position Y de départ
        spacingHorizontal = 150 # Espacement horizontal entre les colonnes
        spacingVertical = 150  # Espacement vertical entre les lignes

        # Image
        imgSoft = self.__arrTK.createImage(resource_path(jsonSetting.lectureJSON("iconSoft")),
                                           tailleX=90,tailleY=90)

        # Liste
        listeTheme = jsonSetting.lectureJSONList("listeTheme")
        self.__listMoteur = jsonSetting.lectureJSONList("listMoteurRecherche")
        self.__listGenre = jsonSetting.lectureJSONList("listGenre")
        listChoixLieu = ["Simple","Domicile","Travail"]
        listChoixSite = ["Autre","Cloud"]

        self.__listChoixMicro = ["ON","OFF"]

        # Creation des Frame
        # Acceuil
        self.__mainFrame = self.__arrTK.createFrame(self.__windows,width=500,height=630)
        self.__cadreMenu = self.__arrTK.createFrame(self.__windows,width=150,height=630)

        # User
        self.__cadreUser = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__userAcceuil = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        self.__userName = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        self.__userGenre = self.__arrTK.createFrame(self.__cadreUser,width=325,height=630)
        # Meteo
        self.__cadreMeteo = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__meteoAcceuil = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoDomicile = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoWork = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoVille = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)
        self.__meteoSuppr = self.__arrTK.createFrame(self.__cadreMeteo,width=325,height=630)

        # GPS
        self.__cadreGPS = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__gpsAcceuil = self.__arrTK.createFrame(self.__cadreGPS,width=325,height=630)
        self.__gpsHome = self.__arrTK.createFrame(self.__cadreGPS,width=325,height=630)
        self.__gpsWork = self.__arrTK.createFrame(self.__cadreGPS,width=325,height=630)
        # Recherche
        self.__cadreRecherche = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Logiciel
        self.__cadreSoft = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__softAcceuil = self.__arrTK.createFrame(self.__cadreSoft,width=325,height=630)
        self.__softSuppr = self.__arrTK.createFrame(self.__cadreSoft,width=325,height=630)
        self.__softAdd = self.__arrTK.createFrame(self.__cadreSoft,width=325,height=630)
        self.__softList = self.__arrTK.createFrame(self.__cadreSoft,width=325,height=630)
        # Internet
        self.__cadreSite = self.__arrTK.createFrame(self.__windows, width=350, height=630)
        self.__acceuilSite = self.__arrTK.createFrame(self.__cadreSite, width=325, height=630)
        self.__faddSite = self.__arrTK.createFrame(self.__cadreSite, width=325, height=630)
        self.__fsupprSite = self.__arrTK.createFrame(self.__cadreSite, width=325, height=630)
        self.__listSite = self.__arrTK.createFrame(self.__cadreSite, width=325, height=630)
        # Theme
        self.__cadreTheme = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        # Micro
        self.__cadreMicro = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__acceuilMicro = self.__arrTK.createFrame(self.__cadreMicro,width=325,height=630)
        self.__fTigerVoice = self.__arrTK.createFrame(self.__cadreMicro,width=325,height=630)
        self.__fSonsEmis = self.__arrTK.createFrame(self.__cadreMicro,width=325,height=630)
        self.__fSaveWord = self.__arrTK.createFrame(self.__cadreMicro,width=325,height=630)
        self.__fmicroDuringSave = self.__arrTK.createFrame(self.__cadreMicro,width=500,height=330)
        self.__fviewWord = self.__arrTK.createFrame(self.__cadreMicro,width=325,height=630)

        # Arrera Work
        self.__cadreArreraWork = self.__arrTK.createFrame(self.__windows, width=350, height=630)
        # Download
        self.__cadreVideoDownload = self.__arrTK.createFrame(self.__windows, width=350, height=630)


        #Widget
        labelTitreMenu = self.__arrTK.createLabel(self.__cadreMenu, text="Menu", ppolice="arial", ptaille=tailleTitle)
        
        boutonMenu = [
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Acceuil",command=self.__backAcceuil,width=20),#0
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Utilisateur",command=self.__showUserFrame,width=20),#1
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial", ptaille=23,
                                                  text="Meteo", command=lambda : self.__viewMeteo(), width=20),#2
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="GPS",command=lambda : self.__viewGPS(),width=20),#3
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Recherche",command=self.__showRechercheFrame,width=20),#4
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Logiciel",command=lambda : self.__viewSoft(),width=20),#5
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Site Web",command=self.__viewSite,width=20),#6
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Theme",command=self.__showThemeFrame,width=20),#7
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                                text="Arrera Work", command=self.__showArreraWorkFolder, width=20),#8
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                      text="Downloader",command=self.__showArreraDownloadFolder, width=20),  # 9
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial", ptaille=23,
                                                  text="Micro", command=self.__viewMicro, width=20),#10
        ]

        #mainFrame

        self.__boutonMenuMain = [
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="",image=imgSoft),#0
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nde\nl'utilisateur",command=self.__showUserFrame),#1
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nmeteo",command = lambda : self.__viewMeteo()),#2
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nGPS",command=lambda : self.__viewGPS()),#3
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nde\nrecherche",command=self.__showRechercheFrame),#4
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndes\nlogiciels",command=lambda :self.__viewSoft()),#5
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndes sites\ninternet",command=self.__viewSite),#6
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\ndu\ntheme",command=self.__showThemeFrame),#7
            self.__arrTK.createButton(self.__mainFrame, ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nArrera\nWork",command=self.__showArreraWorkFolder),#8
            self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=100,height=100,
                                      text="Gestion\nArrera\nDownload",command=self.__showArreraDownloadFolder),#10
            self.__arrTK.createButton(self.__mainFrame, ppolice="arial", ptaille=17, width=100, height=100,
                                      text="Gestion\ndu\nmicro", command=self.__viewMicro),  # 9
        ]

        self.__btnQuitMainFrame = self.__arrTK.createButton(self.__mainFrame,ppolice="arial",ptaille=17,width=200,
                                  text="Quitter")

        # Cadre User
        # Acceuil User
        labelTitleUserAcceuil = self.__arrTK.createLabel(self.__userAcceuil,text="Gestion de l'utilisateur",
                                                         ppolice="Arial", ptaille=tailleTitle)
        btnName = self.__arrTK.createButton(self.__userAcceuil,ppolice = "arial" , ptaille = tailleMain
                                            ,text="Nom de\nl'utilisateur",command=self.__viewUserName)
        btnGenre = self.__arrTK.createButton(self.__userAcceuil,ppolice = "arial" , ptaille = tailleMain
                                             ,text="genre de\nl'utilisateur",command=self.__viewUserGenre)
        # Genre User
        labelTitleUserGenre = self.__arrTK.createLabel(self.__userGenre,text="Genre de l'utilisateur",
                                                         ppolice="Arial", ptaille=tailleTitle)
        menuSelectGenreUser = self.__arrTK.createOptionMenu(self.__userGenre,var=self.__varGenre,value=self.__listGenre)
        btnValidateGenreUser = self.__arrTK.createButton(self.__userGenre,text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=self.__validerUserGenre)
        btnCancelGenreUser = self.__arrTK.createButton(self.__userGenre,text="Annuler",
                                                         ppolice = "arial" , ptaille = tailleMain,command=self.__viewUser)
        # Name User
        labelTitleUserName = self.__arrTK.createLabel(self.__userName,text="Nom de l'utilisateur",
                                                       ppolice="Arial", ptaille=tailleTitle)
        self.__entryNameUser = self.__arrTK.createEntry(self.__userName,ppolice="Arial",ptaille=tailleMain,width=250)
        btnValidateNameUser = self.__arrTK.createButton(self.__userName,text="Valider",
                                                         ppolice = "arial" , ptaille = tailleMain,command=self.__validerUserName)
        btnCancelNameUser = self.__arrTK.createButton(self.__userName,text="Annuler",
                                                       ppolice = "arial" , ptaille = tailleMain,command=self.__viewUser)

        # Cadre Meteo
        # Acceuil Meteo
        labelTitleMainMeteo = self.__arrTK.createLabel(self.__meteoAcceuil, text="Gestion de la meteo"
                                                       ,ppolice="Arial", ptaille=tailleTitle)
        btnAddMeteoHome = self.__arrTK.createButton(self.__meteoAcceuil,text="Lieu\nTravail",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddWork)
        btnAddMeteoWork = self.__arrTK.createButton(self.__meteoAcceuil,text="Lieu\nDomicile",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddDomicile)
        btnAddMeteoTown = self.__arrTK.createButton(self.__meteoAcceuil,text="Autre\nVille",
                                                    ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoAddVille)
        btnSupprMeteo = self.__arrTK.createButton(self.__meteoAcceuil,text="Supprimer\nlieu",
                                                  ppolice = "arial" , ptaille = tailleMain,command=self.__viewMeteoSuppr)
        # Lieu de travail meteo
        labelTitleAddWordMeteo = self.__arrTK.createLabel(self.__meteoWork, text="Ajouter le lieu travail"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoWork = self.__arrTK.createEntry(self.__meteoWork,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddValideMeteoWork = self.__arrTK.createButton(self.__meteoWork,text="Ajouter",
                                                        ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoWork)
        btnCancelMeteoWork = self.__arrTK.createButton(self.__meteoWork,text="Annuler",
                                                       ppolice="Arial",ptaille=tailleMain,
                                                       command=lambda : self.__viewMeteo())
        # Lieu de domicile meteo
        labelTitleAddHomeMeteo = self.__arrTK.createLabel(self.__meteoDomicile, text="Ajouter le lieu domicile"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoDomicile = self.__arrTK.createEntry(self.__meteoDomicile,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddMeteoDomicile = self.__arrTK.createButton(self.__meteoDomicile,text="Ajouter",
                                                        ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoHome)
        btnCancelMeteoDomicile = self.__arrTK.createButton(self.__meteoDomicile,text="Annuler",
                                                           ppolice="Arial",ptaille=tailleMain,
                                                           command=lambda : self.__viewMeteo())

        labelTitleAddTwonMeteo = self.__arrTK.createLabel(self.__meteoVille, text="Ajouter une\nville pour la meteo"
                                                          ,ppolice="Arial", ptaille=tailleTitle)
        self.__entryMeteoTwon = self.__arrTK.createEntry(self.__meteoVille,ppolice="Arial",ptaille=tailleMain,width=220)
        btnAddMeteoTwon = self.__arrTK.createButton(self.__meteoVille,text="Ajouter",
                                                    ppolice="Arial",ptaille=tailleMain,command=self.__addMeteoVille)
        btnCancelMeteoTwon = self.__arrTK.createButton(self.__meteoVille,text="Annuler",
                                                       ppolice="Arial",ptaille=tailleMain,
                                                       command=lambda : self.__viewMeteo())

        labelTitleSupprMeteo = self.__arrTK.createLabel(self.__meteoSuppr, text="Supprimer un lieu\nde meteo"
                                                        ,ppolice="Arial", ptaille=tailleTitle)
        self.__menuSupprMeteo = None
        self.__labelNoMeteo = self.__arrTK.createLabel(self.__meteoSuppr, text="Aucun lieu de meteo\najouté",
                                                       ppolice="Arial",ptaille=tailleMain)
        btnValidateSupprMeteo = self.__arrTK.createButton(self.__meteoSuppr,text="Supprimer",
                                                          ppolice="Arial",ptaille=tailleMain,command=self.__supprMeteo)
        btnCancelSupprMeteo = self.__arrTK.createButton(self.__meteoSuppr,text="Annuler",
                                                          ppolice="Arial",ptaille=tailleMain,command=self.__viewMeteo)

        # Cadre GPS
        # Acceuil GPS
        labelTitleGpsAcceuil = self.__arrTK.createLabel(self.__gpsAcceuil, text="Gestion des\nadresses GPS",
                                                        ppolice="Arial", ptaille=tailleTitle)
        btnGpsHomeAcceuil = self.__arrTK.createButton(self.__gpsAcceuil,text="Adresse\nDomicile",
                                                        ppolice = "arial" , ptaille = tailleMain,command=self.__viewGPSHome)
        btnGpsWorkAcceuil = self.__arrTK.createButton(self.__gpsAcceuil,text="Adresse\nTravail",
                                                      ppolice = "arial" , ptaille = tailleMain,command=self.__viewGPSWork)
        # Work GPS
        labelTitleGpsWork = self.__arrTK.createLabel(self.__gpsWork, text="Adresse de votre\nlieu de travail",
                                                        ppolice="Arial", ptaille=tailleTitle)
        self.__entryGpsWork = self.__arrTK.createEntry(self.__gpsWork,ppolice="Arial",ptaille=tailleMain,width=220)
        btnValideGpsWork = self.__arrTK.createButton(self.__gpsWork,text="Ajouter",
                                                        ppolice="Arial",ptaille=tailleMain,command=self.__validateGpsWork)
        btnCancelGpsWork = self.__arrTK.createButton(self.__gpsWork,text="Annuler",
                                                         ppolice="Arial",ptaille=tailleMain,command=self.__viewGPS)
        # Home GPS
        labelTitleGpsHome = self.__arrTK.createLabel(self.__gpsHome, text="Adresse de\nvotre domicile",
                                                     ppolice="Arial", ptaille=tailleTitle)
        self.__entryGpsHome = self.__arrTK.createEntry(self.__gpsHome,ppolice="Arial",ptaille=tailleMain,width=220)
        btnValideGpsHome = self.__arrTK.createButton(self.__gpsHome,text="Ajouter",
                                                     ppolice="Arial",ptaille=tailleMain,command=self.__validateGpsHome)
        btnCancelGpsHome = self.__arrTK.createButton(self.__gpsHome,text="Annuler",
                                                     ppolice="Arial",ptaille=tailleMain,command=self.__viewGPS)
        # Cadre Rechecrhe
        labelTitreRecherche = self.__arrTK.createLabel(self.__cadreRecherche, text="Choisissez votre moteur\nde recherche"
                                                       , ppolice="Arial", ptaille=tailleTitle)
        menuMoteurRecherche = self.__arrTK.createOptionMenu(self.__cadreRecherche,
                                                            var = self.__varMoteurRecherce,value = self.__listMoteur)
        btnvaliderMoteur = self.__arrTK.createButton(self.__cadreRecherche,text="Valider"
                                                            ,ppolice = "arial" , ptaille = tailleMain,command=self.__validerMoteur)

        # Cadre Software
        # Acceuil Software
        labelTitleAcceuilSoft = self.__arrTK.createLabel(self.__softAcceuil,text="Gestion des logiciels", ppolice="Arial", ptaille=tailleTitle)
        btnAjoutLogicielAcceuil = self.__arrTK.createButton(self.__softAcceuil,text="Ajout\nlogiciel",
                                                            ppolice="arial",ptaille=tailleMain,command=self.__viewSoftAdd)
        btnListLogicielAcceuil = self.__arrTK.createButton(self.__softAcceuil,text="Liste\nlogiciel",
                                                           ppolice="arial",ptaille=tailleMain,command=self.__viewSoftList)
        btnSupprSoftAcceuil = self.__arrTK.createButton(self.__softAcceuil,text="Supprimer\nlogiciel",
                                                        ppolice="arial",ptaille=tailleMain,command=self.__viewSoftSuppr)

        # suppr software
        labelTitleSupprSoftware = self.__arrTK.createLabel(self.__softSuppr, text="Supprimer un logiciel",
                                                           ppolice="Arial", ptaille=tailleTitle)
        self.__menuSupprSoftware = None
        self.__labelSupprSoftware = self.__arrTK.createLabel(self.__softSuppr,
                                                             text="Il a pas de logiciel\nenregister dans l'assistant",
                                                             ppolice="arial",ptaille=tailleMain)
        self.__btnValidateSupprSoftware = self.__arrTK.createButton(self.__softSuppr,text="Valider",
                                                             ppolice="arial",ptaille=tailleMain,command=self.__supprSoft)
        self.__btnCancelSupprSoftware = self.__arrTK.createButton(self.__softSuppr,text="Annuler",
                                                           ppolice="Arial",ptaille=tailleMain,command=self.__backAcceuilSoft)

        # Liste software
        labelTitleListSoftware = self.__arrTK.createLabel(self.__softList, text="Liste des logiciels\nenregistrés",
                                                              ppolice="Arial", ptaille=tailleTitle)
        self.__listSoftware = ctk.CTkTextbox(self.__softList, width=300, height=350,
                                             wrap="word", state="normal", font=("Arial", tailleMain))
        self.__labelNoSoftSave = self.__arrTK.createLabel(self.__softList, text="Aucun logiciel\najouté",
                                                          ppolice="Arial", ptaille=tailleMain)
        btnRetourListSoft = self.__arrTK.createButton(self.__softList,text="Retour",
                                                        ppolice="arial",ptaille=tailleMain,
                                                        command=self.__backAcceuilSoft)
        # Ajout software
        labelTitleAddSoftware = self.__arrTK.createLabel(self.__softAdd,text="Ajout d'un logiciel",
                                                         ppolice="Arial", ptaille=tailleMain)
        self.__entryNameSoft = self.__arrTK.createEntry(self.__softAdd,ppolice="Arial",
                                                        ptaille=tailleMain,width=220)
        btnAddSoftware = self.__arrTK.createButton(self.__softAdd,text="Ajouter",
                                                   ptaille=tailleMain,command=lambda : self.__addSoft())
        btnCancelSoftware = self.__arrTK.createButton(self.__softAdd,text="Annuler",
                                                      ptaille=tailleMain,command=self.__backAcceuilSoft)

        # Cadre Internet
        # Acceuil Site
        labelTitleAcceuilSite = self.__arrTK.createLabel(self.__acceuilSite, text="Gestion des sites internet",
                                                            ppolice="Arial", ptaille=tailleTitle)
        btnAddSiteAcceuil = self.__arrTK.createButton(self.__acceuilSite, text="Ajouter\nun site",
                                                        ppolice = "arial", ptaille = tailleMain,
                                                      command=self.__viewAddSite)
        btnSupprSiteAcceuil = self.__arrTK.createButton(self.__acceuilSite, text="Supprimer\nun site",
                                                        ppolice = "arial", ptaille = tailleMain,
                                                        command=self.__viewSupprSite)
        btnListSiteAcceuil = self.__arrTK.createButton(self.__acceuilSite, text="Liste\ndes sites",
                                                        ppolice = "arial", ptaille = tailleMain,command=self.__viewListSite)
        # add Site
        labelTitleAddSite = self.__arrTK.createLabel(self.__faddSite, text="Ajouter un site internet",
                                                     ppolice="Arial", ptaille=tailleTitle)
        wNameSite,self.__entryNameSite = self.__arrTK.createEntryLegend(self.__faddSite, text="Nom du site : ", ppolice="Arial", ptaille=tailleMain)
        wLinkSite,self.__entryLinkSite = self.__arrTK.createEntryLegend(self.__faddSite, text="Lien du site : ", ppolice="Arial", ptaille=tailleMain)
        btnValidateAddSite = self.__arrTK.createButton(self.__faddSite, text="Valider",
                                                       ppolice = "arial", ptaille = tailleMain, command=self.__addSite)
        btnCancelAddSite = self.__arrTK.createButton(self.__faddSite, text="Annuler", command = self.__backAcceuilSite,
                                                     ppolice = "arial", ptaille = tailleMain)
        # Suppr Site
        labelTitleSupprSite = self.__arrTK.createLabel(self.__fsupprSite, text="Supprimer un site internet",
                                                       ppolice="Arial", ptaille=tailleTitle)
        self.__menuSupprSite =  None
        self.__labelNoSite = self.__arrTK.createLabel(self.__fsupprSite, text="Aucun site internet\najouté",
                                                      ppolice="Arial", ptaille=tailleMain)
        self.__btnValidateSupprSite = self.__arrTK.createButton(self.__fsupprSite, text="Supprimer",
                                                                ppolice = "arial", ptaille = tailleMain,
                                                                command=self.__supprSite)
        self.__btnCancelSupprSite = self.__arrTK.createButton(self.__fsupprSite, text="Annuler",
                                                              ppolice = "arial", ptaille = tailleMain,
                                                              command=self.__backAcceuilSite)

        # List Site
        labelTitleListSite = self.__arrTK.createLabel(self.__listSite, text="Liste des sites internet\nenregistrés",
                                                        ppolice="Arial", ptaille=tailleTitle)
        self.__listSiteInternet = ctk.CTkTextbox(self.__listSite, width=300, height=350,
                                                    wrap="word", state="normal", font=("Arial", tailleMain))
        self.__labelNoSiteSave = self.__arrTK.createLabel(self.__listSite, text="Aucun site internet\najouté",
                                                            ppolice="Arial", ptaille=tailleMain)
        btnRetourListSite = self.__arrTK.createButton(self.__listSite, text="Retour",command=self.__backAcceuilSite,
                                                        ppolice="arial", ptaille=tailleMain)
        # Cardre theme 
        labelTitreTheme = self.__arrTK.createLabel(self.__cadreTheme, text="Choix du thème\nde l'interface"
                                                   , ppolice="Arial", ptaille=tailleTitle)
        menuChoixTheme = self.__arrTK.createOptionMenu(self.__cadreTheme,var = self.__varChoixTheme,value=listeTheme)
        btnValiderTheme = self.__arrTK.createButton (self.__cadreTheme,text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=self.__validerTheme)
        # Cadre Micro
        # Acceuil Micro
        labelTitreAcceuilMicro = self.__arrTK.createLabel(self.__acceuilMicro, text="Paramètre du micro",
                                                          ppolice="Arial", ptaille=tailleTitle)
        btnAcceuilTigerVoice = self.__arrTK.createButton(self.__acceuilMicro, text="Empreinte\nvocale",
                                                        ppolice = "arial" , ptaille = tailleMain,
                                                         command=self.__viewTigerVoice)
        btnAcceuilSonsEmis = self.__arrTK.createButton(self.__acceuilMicro, text="Sons\némis",
                                                       ppolice = "arial", ptaille = tailleMain,
                                                       command=self.__viewMicroSound)
        # Tiger Voice
        labelTitleTigerWordMicro = self.__arrTK.createLabel(self.__fTigerVoice, text="Empreinte vocale",
                                                              ppolice="Arial", ptaille=tailleTitle)
        self.__btnVoicePrint1 = self.__arrTK.createButton(self.__fTigerVoice, text="Empreinte\nVocale 1",
                                                              ppolice = "arial" , ptaille = tailleMain,
                                                          command = lambda : self.__viewSaveTigerWord(1))
        self.__btnVoicePrint2 = self.__arrTK.createButton(self.__fTigerVoice, text="Empreinte\nVocale 2",
                                                          ppolice = "arial" , ptaille = tailleMain
                                                          ,command = lambda : self.__viewSaveTigerWord(2))
        self.__btnVoicePrint3 = self.__arrTK.createButton(self.__fTigerVoice, text="Empreinte\nVocale 3",
                                                          ppolice = "arial" , ptaille = tailleMain
                                                          ,command = lambda : self.__viewSaveTigerWord(3))
        btnBackAcceuilTigerVoice = self.__arrTK.createButton(self.__fTigerVoice, text="Retour",command=self.__backAcceuilMicro,
                                                                ppolice = "arial" , ptaille = tailleMain)
        # Sons Emis
        labelTitleSonsEmisMicro = self.__arrTK.createLabel(self.__fSonsEmis, text="Sons émis par le micro",
                                                            ppolice="Arial", ptaille=tailleTitle)
        menuSonsEmis = self.__arrTK.createOptionMenu(self.__fSonsEmis,value=self.__listChoixMicro,var=self.__varSonsEmis)
        btnValiderSonsEmis = self.__arrTK.createButton(self.__fSonsEmis, text="Valider",
                                                        ppolice = "arial" , ptaille = tailleMain,command=self.__validerSoundMicro)
        btnBackAcceuilSonsEmis = self.__arrTK.createButton(self.__fSonsEmis, text="Retour",
                                                            ppolice = "arial" , ptaille = tailleMain,command=self.__backAcceuilMicro)
        # Save Word
        self.__labelTitleSaveWordMicro = self.__arrTK.createLabel(self.__fSaveWord, text="Sauvegarde des mots",
                                                            ppolice="Arial", ptaille=tailleTitle)
        self.__btnSaveWord = self.__arrTK.createButton(self.__fSaveWord, text="Enregistrer",
                                                        ppolice = "arial" , ptaille = tailleMain,command=self.__recordTigerWord)
        self.__btnSupprWord = self.__arrTK.createButton(self.__fSaveWord, text="Supprimer",
                                                       ppolice = "arial" , ptaille = tailleMain)
        self.__labelShowSavedWord = self.__arrTK.createLabel(self.__fSaveWord,ppolice = "arial" , ptaille = tailleMain)
        
        self.__btnBackSaveWord = self.__arrTK.createButton(self.__fSaveWord, text="Retour",
                                                        ppolice = "arial" , ptaille = tailleMain,
                                                        command=self.__viewTigerVoice)
        # view Word
        labelTitleViewWordMicro = self.__arrTK.createLabel(self.__fviewWord, text="Enregistrement de\nl'empreinte vocale",
                                                            ppolice="Arial", ptaille=tailleTitle)
        self.__labelViewWordSave = self.__arrTK.createLabel(self.__fviewWord,ppolice="Arial", ptaille=tailleTitle)
        self.__btnValidateWordSaved = self.__arrTK.createButton(self.__fviewWord, text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=self.__saveTigerWord)
        btnCancelSavedWord = self.__arrTK.createButton(self.__fviewWord, text="Annuler",
                                                        ppolice = "arial" , ptaille = tailleMain,command=self.__viewTigerVoice)

        # fmicroDuringSave
        labelDuringSave = self.__arrTK.createLabel(self.__fmicroDuringSave, text="Enregistrement en cours...\nVeuillez patienter"
                                                   ,ppolice = "arial" , ptaille = tailleMain)
        
        # Cader Work folder
        labelTitreArreraWork = self.__arrTK.createLabel(self.__cadreArreraWork,
                                                        text="Choisir le dossier\npour Arrera Work",
                                                        ppolice="Arial", ptaille=tailleTitle)

        self.__btnFolderArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Choisir le dossier",
                                                               ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerFolderWork(1))
        self.__btnSupprArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Supprimer le dossier",
                                                              ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderWork(2))
        # Cadre Download folder
        labelTitreDownload = self.__arrTK.createLabel(self.__cadreVideoDownload,
                                                             text="Choisir le dossier pour\nArrera video download",
                                                             ppolice="Arial", ptaille=tailleTitle)
        self.__btnFolderDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Choisir le dossier",
                                                             ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(1))
        self.__btnSupprDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Supprimer le dossier",
                                                            ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(2))
        # Placement widget
        self.__arrTK.placeTopCenter(labelTitreMenu)
        
        boutonMenu[0].place(relx=0.0,y=50)
        boutonMenu[1].place(relx=0.0,y=100)
        boutonMenu[2].place(relx=0.0,y=150)
        boutonMenu[3].place(relx=0.0,y=200)
        boutonMenu[4].place(relx=0.0,y=250)
        boutonMenu[5].place(relx=0.0,y=300)
        boutonMenu[6].place(relx=0.0,y=350)
        boutonMenu[7].place(relx=0.0,y=400)
        boutonMenu[8].place(relx=0.0,y=450)
        boutonMenu[9].place(relx=0.0,y=500)

        self.__arrTK.placeTopCenter(labelTitreRecherche)
        self.__arrTK.placeCenter(menuMoteurRecherche)
        self.__arrTK.placeBottomCenter(btnvaliderMoteur)

        self.__arrTK.placeTopCenter(labelTitleAcceuilSoft)
        self.__arrTK.placeCenterOnWidth(btnAjoutLogicielAcceuil,100)
        self.__arrTK.placeCenterOnWidth(btnListLogicielAcceuil,200)
        self.__arrTK.placeCenterOnWidth(btnSupprSoftAcceuil,300)

        self.__arrTK.placeTopCenter(labelTitleAddSoftware)
        self.__arrTK.placeCenter(self.__entryNameSoft)
        self.__arrTK.placeLeftBottom(btnCancelSoftware)
        self.__arrTK.placeRightBottom(btnAddSoftware)

        self.__arrTK.placeTopCenter(labelTitleListSoftware)
        self.__arrTK.placeBottomCenter(btnRetourListSoft)

        self.__arrTK.placeTopCenter(labelTitleSupprSoftware)

        self.__arrTK.placeTopCenter(labelTitreTheme)
        self.__arrTK.placeCenter(menuChoixTheme)
        self.__arrTK.placeBottomCenter(btnValiderTheme)

        self.__arrTK.placeTopCenter(labelTitreAcceuilMicro)
        self.__arrTK.placeCenterOnWidth(btnAcceuilTigerVoice,100)
        self.__arrTK.placeCenterOnWidth(btnAcceuilSonsEmis,200)

        self.__arrTK.placeTopCenter(labelTitleTigerWordMicro)
        self.__arrTK.placeBottomCenter(btnBackAcceuilTigerVoice)

        self.__arrTK.placeTopCenter(labelTitleSonsEmisMicro)
        self.__arrTK.placeCenter(menuSonsEmis)
        self.__arrTK.placeLeftBottom(btnBackAcceuilSonsEmis)
        self.__arrTK.placeRightBottom(btnValiderSonsEmis)
        
        self.__arrTK.placeTopCenter(self.__labelTitleSaveWordMicro)

        self.__arrTK.placeTopCenter(labelTitleViewWordMicro)
        self.__arrTK.placeCenter(self.__labelViewWordSave)
        self.__arrTK.placeRightBottom(self.__btnValidateWordSaved)
        self.__arrTK.placeLeftBottom(btnCancelSavedWord)

        self.__arrTK.placeTopCenter(labelDuringSave)

        self.__arrTK.placeTopCenter(labelTitreDownload)
        self.__arrTK.placeTopCenter(labelTitreArreraWork)


        for index, bouton in enumerate(self.__boutonMenuMain):
            x = startX + (index % 3) * spacingHorizontal  # Calculer la position X (colonne pour 3 boutons par ligne)
            y = startY + (index // 3) * spacingVertical # Calculer la position Y (ligne)
            bouton.place(x=x, y=y)

        if (jsonSetting.lectureJSON("gestionMicro")=="1"):
            boutonMenu[10].place(relx=0.0,y=550)
        else :
            self.__boutonMenuMain[10].place_forget()

        # Cadre Meteo
        self.__arrTK.placeTopCenter(labelTitleMainMeteo)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoHome,100)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoWork,200)
        self.__arrTK.placeCenterOnWidth(btnAddMeteoTown,300)
        self.__arrTK.placeCenterOnWidth(btnSupprMeteo,400)

        self.__arrTK.placeTopCenter(labelTitleAddHomeMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoDomicile)
        self.__arrTK.placeLeftBottom(btnCancelMeteoDomicile)
        self.__arrTK.placeRightBottom(btnAddMeteoDomicile)

        self.__arrTK.placeTopCenter(labelTitleAddWordMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoWork)
        self.__arrTK.placeLeftBottom(btnCancelMeteoWork)
        self.__arrTK.placeRightBottom(btnAddValideMeteoWork)

        self.__arrTK.placeTopCenter(labelTitleAddTwonMeteo)
        self.__arrTK.placeCenter(self.__entryMeteoTwon)
        self.__arrTK.placeLeftBottom(btnCancelMeteoTwon)
        self.__arrTK.placeRightBottom(btnAddMeteoTwon)

        self.__arrTK.placeTopCenter(labelTitleSupprMeteo)
        self.__arrTK.placeLeftBottom(btnCancelSupprMeteo)
        self.__arrTK.placeRightBottom(btnValidateSupprMeteo)

        self.__arrTK.placeTopCenter(labelTitleUserAcceuil)
        self.__arrTK.placeCenterOnWidth(btnName,100)
        self.__arrTK.placeCenterOnWidth(btnGenre,200)

        self.__arrTK.placeTopCenter(labelTitleUserGenre)
        self.__arrTK.placeCenter(menuSelectGenreUser)
        self.__arrTK.placeLeftBottom(btnCancelGenreUser)
        self.__arrTK.placeRightBottom(btnValidateGenreUser)

        self.__arrTK.placeTopCenter(labelTitleUserName)
        self.__arrTK.placeCenter(self.__entryNameUser)
        self.__arrTK.placeLeftBottom(btnCancelNameUser)
        self.__arrTK.placeRightBottom(btnValidateNameUser)

        self.__arrTK.placeTopCenter(labelTitleGpsAcceuil)
        self.__arrTK.placeCenterOnWidth(btnGpsHomeAcceuil,100)
        self.__arrTK.placeCenterOnWidth(btnGpsWorkAcceuil,200)

        self.__arrTK.placeTopCenter(labelTitleGpsHome)
        self.__arrTK.placeCenter(self.__entryGpsHome)
        self.__arrTK.placeLeftBottom(btnCancelGpsHome)
        self.__arrTK.placeRightBottom(btnValideGpsHome)

        self.__arrTK.placeTopCenter(labelTitleGpsWork)
        self.__arrTK.placeCenter(self.__entryGpsWork)
        self.__arrTK.placeLeftBottom(btnCancelGpsWork)
        self.__arrTK.placeRightBottom(btnValideGpsWork)

        self.__arrTK.placeTopCenter(labelTitleAcceuilSite)
        self.__arrTK.placeCenterOnWidth(btnAddSiteAcceuil,100)
        self.__arrTK.placeCenterOnWidth(btnSupprSiteAcceuil,200)
        self.__arrTK.placeCenterOnWidth(btnListSiteAcceuil,300)

        self.__arrTK.placeTopCenter(labelTitleAddSite)
        self.__arrTK.placeCenterOnWidth(wNameSite,200)
        self.__arrTK.placeCenterOnWidth(wLinkSite,300)
        self.__arrTK.placeLeftBottom(btnCancelAddSite)
        self.__arrTK.placeRightBottom(btnValidateAddSite)

        self.__arrTK.placeTopCenter(labelTitleSupprSite)

        self.__arrTK.placeTopCenter(labelTitleListSite)
        self.__arrTK.placeBottomCenter(btnRetourListSite)

    def active(self):
        self.__arrTK.setResizable(True)
        self.__arrTK.setGeometry(500,630)
        self.__arrTK.setResizable(False)
        self.__mainFrame.pack()

    def passQUITFNC(self,quitFNC):
        self.__btnQuitMainFrame.configure(command=lambda : self.__leaveSetting(quitFNC))
        self.__arrTK.placeBottomCenter(self.__btnQuitMainFrame)

    def __leaveSetting(self, quitFnc):
        self.leaveSetting()
        quitFnc()

    def leaveSetting(self):
        self.__disableAllFrame()
        self.__cadreMenu.pack_forget()

    def __backAcceuil(self):
        self.__mainFrame.pack()
        self.__cadreMenu.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreSite.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
    
    def __disableAllFrame(self):
        self.__mainFrame.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreSite.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
        self.__cadreMenu.pack(side="left")
    
    def __showUserFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreUser)
        self.__viewUser()

    def __showRechercheFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreRecherche)

    def __viewSoft(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreSoft)
        self.__arrTK.placeCenter(self.__softAcceuil)

    def __viewSoftAdd(self):
        self.__softAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__softAdd)

    def __viewSoftList(self):
        self.__softAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__softList)

        self.__labelNoSoftSave.place_forget()
        self.__listSoftware.place_forget()

        self.__listSoftware.configure(state="normal")
        self.__listSoftware.delete(1.0, END)
        listSoft = self.__gazelle.getListSoft()

        if len(listSoft) == 0 :
            self.__arrTK.placeCenter(self.__labelNoSoftSave)
        else :
            for i in range(0,len(listSoft)):
                self.__listSoftware.insert(END, listSoft[i] + "\n")
            self.__arrTK.placeCenter(self.__listSoftware)

        self.__listSoftware.configure(state="disabled")


    def __viewSoftSuppr(self):
        self.__labelSupprSoftware.place_forget()
        self.__btnCancelSupprSoftware.place_forget()
        self.__btnValidateSupprSoftware.place_forget()
        listSoft = self.__gazelle.getListSoft()

        if len(listSoft) == 0 :
            self.__arrTK.placeCenter(self.__labelSupprSoftware)
            self.__arrTK.placeBottomCenter(self.__btnCancelSupprSoftware)
        else :
            self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__softSuppr,listSoft,self.__varSupprSoft)
            self.__arrTK.placeCenter(self.__menuSupprSoft)
            self.__arrTK.placeLeftBottom(self.__btnCancelSupprSoftware)
            self.__arrTK.placeRightBottom(self.__btnValidateSupprSoftware)

        self.__softAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__softSuppr)

    def __backAcceuilSoft(self):
        self.__softSuppr.place_forget()
        self.__softAdd.place_forget()
        self.__softList.place_forget()
        self.__arrTK.placeCenter(self.__softAcceuil)

    def __addSoft(self):
        soft = self.__entryNameSoft.get()
        if (soft == ""):
            showerror("Parametre", "Impossible d'ajouter un logiciel sans nom")
        else:
            self.__gazelle.addSoft(soft)
            showinfo("Parametre", "Logiciel ajouté")
            self.__entryNameSoft.delete(0, END)

        self.__backAcceuilSoft()



    def __supprSoft(self):
        soft = self.__varSupprSoft.get()
        if self.__gazelle.supprSoft(soft):
            showinfo("Parametre", "Logiciel supprimé")
        else :
            showerror("Parametre", "Impossible de supprimer ce logiciel")

        self.__menuSupprSoft.place_forget()
        self.__menuSupprSoft = None
        self.__backAcceuilSoft()

    def __viewSite(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreSite)
        self.__arrTK.placeCenter(self.__acceuilSite)

    def __backAcceuilSite(self):
        self.__disableSiteFrame()
        self.__arrTK.placeCenter(self.__acceuilSite)

    def __disableSiteFrame(self):
        self.__acceuilSite.place_forget()
        self.__faddSite.place_forget()
        self.__fsupprSite.place_forget()
        self.__listSite.place_forget()

    def __viewAddSite(self):
        self.__disableSiteFrame()
        self.__arrTK.placeCenter(self.__faddSite)
        self.__entryNameSite.delete(0,END)
        self.__entryLinkSite.delete(0,END)
    
    def __viewSupprSite(self):
        self.__disableSiteFrame()
        self.__arrTK.placeCenter(self.__fsupprSite)
        listSite = self.__gazelle.getListSite()
        self.__labelNoSite.place_forget()
        self.__btnCancelSupprSite.place_forget()
        self.__btnValidateSupprSite.place_forget()
        if (self.__menuSupprSite != None):
            self.__menuSupprSite.place_forget()
            self.__menuSupprSite = None
        if len(listSite) == 0:
            self.__arrTK.placeCenter(self.__labelNoSite)
            self.__arrTK.placeBottomCenter(self.__btnCancelSupprSite)
        else :
            self.__menuSupprSite = self.__arrTK.createOptionMenu(self.__fsupprSite,
                                                                 var = self.__varSupprSite,
                                                                 value = listSite)
            self.__arrTK.placeBottomLeft(self.__btnCancelSupprSite)
            self.__arrTK.placeBottomRight(self.__btnValidateSupprSite)
            self.__arrTK.placeCenter(self.__menuSupprSite)


    def __viewListSite(self):
        self.__disableSiteFrame()
        self.__arrTK.placeCenter(self.__listSite)

        self.__labelNoSiteSave.place_forget()
        self.__listSiteInternet.place_forget()

        self.__listSiteInternet.configure(state="normal")
        self.__listSiteInternet.delete(1.0, END)
        listSite = self.__gazelle.getListSite()

        if len(listSite) == 0 :
            self.__arrTK.placeCenter(self.__labelNoSiteSave)
        else :
            for i in range(0,len(listSite)):
                self.__listSiteInternet.insert(END, listSite[i] + "\n")
            self.__arrTK.placeCenter(self.__listSiteInternet)

        self.__listSiteInternet.configure(state="disabled")

    def __supprSite(self):
        site = self.__varSupprSite.get()
        if (site == ""):
            showerror("Parametre", "Impossible de supprimer un site sans nom")
        else:
            if (self.__gazelle.supprSite(1,site)):
                showinfo("Parametre", "Site supprimé")
            else :
                showerror("Parametre", "Impossible de supprimer ce site")

        self.__menuSupprSite.place_forget()
        self.__backAcceuilSite()

    def __addSite(self):
        name = self.__entryNameSite.get()
        link = self.__entryLinkSite.get()
        if (name == "" or link == ""):
            showerror("Parametre", "Impossible d'ajouter un site sans nom ou lien")
        else:
            self.__gazelle.addSite(1,name, link)
            showinfo("Parametre", "Site ajouté")
            self.__entryNameSite.delete(0, END)
            self.__entryLinkSite.delete(0, END)

        self.__backAcceuilSite()


    
    def __showThemeFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreTheme)

    def __backAcceuilMicro(self):
        self.__disableMicroFrame()
        self.__arrTK.placeCenter(self.__acceuilMicro)

    def __viewMicro(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreMicro)
        self.__arrTK.placeCenter(self.__acceuilMicro)

    def __disableMicroFrame(self):
        self.__acceuilMicro.place_forget()
        self.__fTigerVoice.place_forget()
        self.__fSonsEmis.place_forget()
        self.__fSaveWord.place_forget()
        self.__fviewWord.place_forget()
        self.__fmicroDuringSave.place_forget()
    
    def __viewMicroSound(self):
        self.__disableMicroFrame()
        self.__arrTK.placeCenter(self.__fSonsEmis)
        etatMicro = self.__gazelle.getSoundMicroAsEnable()
        if (etatMicro==True):
            self.__varSonsEmis.set(self.__listChoixMicro[0])
        else :
            self.__varSonsEmis.set(self.__listChoixMicro[1])

    def __viewTigerVoice(self):
        self.__disableMicroFrame()
        self.__arrTK.placeCenter(self.__fTigerVoice)

        self.__btnVoicePrint1.place_forget()
        self.__btnVoicePrint2.place_forget()
        self.__btnVoicePrint3.place_forget()

        nbTiger = self.__gazelle.getNbTrigerWord()

        if nbTiger == 0:
            self.__arrTK.placeCenter(self.__btnVoicePrint1)
        elif nbTiger == 1:
            self.__arrTK.placeCenterOnWidth(self.__btnVoicePrint1,150)
            self.__arrTK.placeCenterOnWidth(self.__btnVoicePrint2,250)
        else :
            self.__arrTK.placeCenterOnWidth(self.__btnVoicePrint1,100)
            self.__arrTK.placeCenterOnWidth(self.__btnVoicePrint2,200)
            self.__arrTK.placeCenterOnWidth(self.__btnVoicePrint3,300)
    
    def __viewSaveTigerWord(self,nbTiger:int):
        
        self.__disableMicroFrame()
        self.__arrTK.placeCenter(self.__fSaveWord)

        self.__btnSaveWord.place_forget()
        self.__btnBackSaveWord.place_forget()
        self.__labelShowSavedWord.place_forget()
        self.__btnSupprWord.place_forget()

        listWord = self.__gazelle.getTrigerWord()
        nb = len(listWord)
        
        match nbTiger:
            case 1:
                self.__labelTitleSaveWordMicro.configure(text="Gestion empreinte\nvocale 1")
                
                if nb == 0:
                    self.__arrTK.placeCenter(self.__btnSaveWord)
                    self.__arrTK.placeBottomCenter(self.__btnBackSaveWord)
                else :
                    self.__arrTK.placeCenter(self.__labelShowSavedWord)
                    self.__labelShowSavedWord.configure(text=listWord[0])

                    self.__arrTK.placeRightBottom(self.__btnSupprWord)
                    self.__arrTK.placeLeftBottom(self.__btnBackSaveWord)
                    self.__btnSupprWord.configure(command=lambda : self.__supprTrigerWord(1))
            case 2:
                self.__labelTitleSaveWordMicro.configure(text="Gestion empreinte\nvocale 2")
                if nb == 1:
                    self.__arrTK.placeCenter(self.__btnSaveWord)
                    self.__arrTK.placeBottomCenter(self.__btnBackSaveWord)
                else :
                    self.__arrTK.placeCenter(self.__labelShowSavedWord)
                    self.__labelShowSavedWord.configure(text=listWord[1])

                    self.__arrTK.placeRightBottom(self.__btnSupprWord)
                    self.__arrTK.placeLeftBottom(self.__btnBackSaveWord)
                    self.__btnSupprWord.configure(command=lambda : self.__supprTrigerWord(2))
            case 3:
                self.__labelTitleSaveWordMicro.configure(text="Gestion empreinte\nvocale 3")
                if nb == 2:
                    self.__arrTK.placeCenter(self.__btnSaveWord)
                    self.__arrTK.placeBottomCenter(self.__btnBackSaveWord)
                else :
                    self.__arrTK.placeCenter(self.__labelShowSavedWord)
                    self.__labelShowSavedWord.configure(text=listWord[2])

                    self.__arrTK.placeRightBottom(self.__btnSupprWord)
                    self.__arrTK.placeLeftBottom(self.__btnBackSaveWord)
                    self.__btnSupprWord.configure(command=lambda : self.__supprTrigerWord(3))

            case other:
                return

    def __recordTigerWord(self):
        self.__threadSaveVoicePrint = th.Thread(target=self.__thsaveTigerWord)
        self.__threadSaveVoicePrint.start()
        self.__disableMicroFrame()
        self.__arrTK.placeCenter(self.__fmicroDuringSave)
        self.__windows.after(100, self.__duringSaveTigerWord)

    def __thsaveTigerWord(self):
        sortie = self.__gazelle.recordTrigerWord()
        if sortie:
            self.__labelViewWordSave.configure(text="Mots enregistrer : "+self.__gazelle.getRecordTrigerWord())

    def __duringSaveTigerWord(self):
        if self.__threadSaveVoicePrint.is_alive():
            self.__windows.update()
            self.__windows.after(100, self.__duringSaveTigerWord)
        else :
            self.__disableMicroFrame()
            self.__arrTK.placeCenter(self.__fviewWord)


    def __saveTigerWord(self):
        self.__backAcceuilMicro()
        self.__gazelle.saveRecordTrigerWord()
        messagebox.showinfo("Parametre","Le mot déclencheur ont bien été enregistrés.")

    def __supprTrigerWord(self,mode:int):
        self.__backAcceuilMicro()

        word = self.__gazelle.getTrigerWord()[mode-1]

        self.__gazelle.supprTrigerWord(word)


    def __viewUser(self):
        self.__arrTK.placeCenter(self.__userAcceuil)
        self.__userName.place_forget()
        self.__userGenre.place_forget()

    def __viewUserName(self):
        self.__entryNameUser.delete(0,END)
        self.__arrTK.placeCenter(self.__userName)
        self.__userAcceuil.place_forget()
        self.__userGenre.place_forget()

    def __viewUserGenre(self):
        self.__varGenre.set(self.__listGenre[0])
        self.__arrTK.placeCenter(self.__userGenre)
        self.__userAcceuil.place_forget()
        self.__userName.place_forget()
    
    def __validerUserName(self):
        name = self.__entryNameUser.get()
        self.__entryNameUser.delete(0,END)
        if (name == ""):
            showerror("Parametre","Impossible d'enregistrer un nom vide")
        else :
            self.__gazelle.changeUserName(name)
            showinfo("Parametre","Nom enregistré")
        self.__viewUser()

    def __validerUserGenre(self):
        genre = self.__varGenre.get()
        self.__gazelle.changeUserGenre(genre)
        showinfo("Parametre","Nom enregistré")
        self.__viewUser()


    def __viewMeteo(self):
        self.__disableAllFrame()
        self.__meteoDomicile.place_forget()
        self.__meteoWork.place_forget()
        self.__meteoVille.place_forget()
        self.__meteoSuppr.place_forget()
        self.__arrTK.packRight(self.__cadreMeteo)
        self.__arrTK.placeTopCenter(self.__meteoAcceuil)

    def __viewMeteoAddDomicile(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoDomicile)

    def __viewMeteoAddWork(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoWork)

    def __viewMeteoAddVille(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoVille)

    def __viewMeteoSuppr(self):
        self.__meteoAcceuil.place_forget()
        self.__arrTK.placeCenter(self.__meteoSuppr)
        listVille = self.__gazelle.getMeteoSave()
        self.__labelNoMeteo.place_forget()
        self.__menuSupprMeteo = None
        if len(listVille) == 0:
            self.__arrTK.placeCenter(self.__labelNoMeteo)
        else :
            self.__menuSupprMeteo = self.__arrTK.createOptionMenu(self.__meteoSuppr,
                                                                  var = self.__varChoixSupprMeteo,
                                                                  value = listVille)
            self.__arrTK.placeCenter(self.__menuSupprMeteo)
    
    def __addMeteoHome(self):
        home = self.__entryMeteoDomicile.get()
        if (home==""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoDomicile.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(1,home) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __addMeteoWork(self):
        work = self.__entryMeteoWork.get()
        if (work== ""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoWork.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(2, work) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __addMeteoVille(self):
        twon = self.__entryMeteoTwon.get()
        if (twon== ""):
            showerror("Parametre","Impossible d'enregistrer une ville vide")
        else :
            self.__entryMeteoTwon.delete(0,END)
            if (self.__gazelle.ajoutVilleMeteo(3, twon) == False):
                showerror("Parametre","Impossible d'enregistrer cette ville")
            else :
                showinfo("Parametre","Ville enregistré")
                self.__viewMeteo()

    def __supprMeteo(self):
        ville = self.__varChoixSupprMeteo.get()
        if (ville == ""):
            showerror("Parametre","Impossible de supprimer une ville vide")
        else :
            if (self.__gazelle.supprVilleMeteo(3,ville) == False):
                showerror("Parametre","Impossible de supprimer cette ville")
            else :
                showinfo("Parametre","Ville supprimé")

        self.__menuSupprMeteo.place_forget()
        self.__menuSupprMeteo = None
        self.__viewMeteo()
    
    def __viewGPS(self):
        self.__disableAllFrame()
        self.__gpsWork.place_forget()
        self.__gpsHome.place_forget()
        self.__arrTK.packRight(self.__cadreGPS)
        self.__arrTK.placeCenter(self.__gpsAcceuil)
    
    def __viewGPSHome(self):
        self.__gpsAcceuil.place_forget()
        self.__gpsWork.place_forget()
        self.__arrTK.placeCenter(self.__gpsHome)

    def __viewGPSWork(self):
        self.__gpsAcceuil.place_forget()
        self.__gpsHome.place_forget()
        self.__arrTK.placeCenter(self.__gpsWork)
    
    def __validateGpsHome(self):
        home = self.__entryGpsHome.get()
        if (home == ""):
            showerror("Parametre","Impossible d'enregistrer une adresse vide")
        else :
            self.__entryGpsHome.delete(0,END)
            if (self.__gazelle.ajoutGPSAdresse(1,home) == False):
                showerror("Parametre","Impossible d'enregistrer cette adresse")
            else :
                showinfo("Parametre","Adresse enregistré")
        self.__viewGPS()

    def __validateGpsWork(self):
        work = self.__entryGpsWork.get()
        if (work == ""):
            showerror("Parametre","Impossible d'enregistrer une adresse vide")
        else :
            self.__entryGpsHome.delete(0,END)
            if (self.__gazelle.ajoutGPSAdresse(2, work) == False):
                showerror("Parametre","Impossible d'enregistrer cette adresse")
            else :
                showinfo("Parametre","Adresse enregistré")
        self.__viewGPS()
    
    def __validerMoteur(self):
        moteur = self.__varMoteurRecherce.get()
        if (self.__gazelle.changeMoteur(moteur)):
            showinfo("Parametre","Moteur enregistré")
        else :
            showerror("Parametre","Impossible d'enregistrer le moteur")
        self.__backAcceuil()

    
    def __validerTheme(self):
        theme = self.__varChoixTheme.get()
        self.__gazelle.changeTheme(theme)
        showinfo("Parametre","Theme changer")
        self.__backAcceuil()
    
    def __validerSoundMicro(self):
        sortie = self.__varSonsEmis.get()
        if (sortie=="ON"):
            self.__gazelle.changeSoundMicro(True)
        else :
            self.__gazelle.changeSoundMicro(False)
        self.__backAcceuilMicro()

    def __showArreraWorkFolder(self):
        folderExist = self.__gazelle.workFolderExist()
        self.__disableAllFrame()
        self.__btnSupprArreraWork.place_forget()
        self.__btnFolderArreraWork.place_forget()
        self.__arrTK.packRight(self.__cadreArreraWork)
        if folderExist :
            self.__arrTK.placeCenter(self.__btnSupprArreraWork)
        else :
            self.__arrTK.placeCenter(self.__btnFolderArreraWork)

    def __showArreraDownloadFolder(self):
        folderExist = self.__gazelle.downloadFolderExist()
        self.__disableAllFrame()
        self.__btnSupprDownload.place_forget()
        self.__btnFolderDownload.place_forget()
        self.__arrTK.packRight(self.__cadreVideoDownload)
        if folderExist :
            self.__arrTK.placeCenter(self.__btnSupprDownload)
        else :
            self.__arrTK.placeCenter(self.__btnFolderDownload)

    def __validerFolderWork(self,mode : int ):
        """
        1 : add
        2 : suppr
        """
        self.__backAcceuil()

        match mode :
            case 1 :
                self.__gazelle.setWorkFolder()
            case 2 :
                self.__gazelle.supprWorkFolder()

    def __validerFolderDownload(self,mode : int ):
        """
        1 : add
        2 : suppr
        """
        self.__backAcceuil()

        match mode :
            case 1 :
                self.__gazelle.setVideoDownloadFolder()
            case 2 :
                self.__gazelle.supprVideoDownloadFolder()

    def passApropos(self,aproposFNC):
        self.__boutonMenuMain[0].configure(command=aproposFNC)