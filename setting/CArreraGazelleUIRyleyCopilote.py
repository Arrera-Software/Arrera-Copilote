from librairy.arrera_tk import *
from setting.arreraGazelle import*
from tkinter.messagebox import*
from typing import Union

class CArreraGazelleUIRyleyCopilote :
    def __init__(self,atk:CArreraTK,windows:Union[ctk.CTk,ctk.CTkToplevel],emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str,emplacementConfigSetting:str):
        # Ouverture de l'objet

        self.__gazelle = CArreraGazelle(emplacementJsonUser,emplacementJsonNeuronNetwork,emplacementJsonAssistant)
        jsonSetting = jsonWork(emplacementConfigSetting)

        # Mise de la fenetre dans un atribut

        self.__windows = windows
        self.__arrTK = atk

        # Varriable

        tailleTitle = 27
        tailleMain = 23
        self.__varRecherche = StringVar(self.__windows)
        self.__varMoteurRecherce = StringVar(self.__windows)
        self.__varTheme = StringVar(self.__windows)
        self.__varGenre = StringVar(self.__windows)
        self.__varChoixLieu = StringVar(self.__windows)
        self.__varSupprLieu = StringVar(self.__windows)
        self.__varSupprSoft = StringVar(self.__windows)
        self.__varChoixSite =  StringVar(self.__windows)
        self.__varSupprSite =  StringVar(self.__windows)
        self.__varChoixTheme  =  StringVar(self.__windows)
        self.__varChoixMicro =  StringVar(self.__windows)

        # Liste
        listeTheme = jsonSetting.lectureJSONList("listeTheme")
        listMoteur = jsonSetting.lectureJSONList("listMoteurRecherche")
        listGenre = jsonSetting.lectureJSONList("listGenre")
        listChoixLieu = ["Simple","Domicile","Travail"]
        listChoixSite = ["Autre","Cloud"]
        self.__listChoixMicro = ["ON","OFF"]

        # Creation des Frame
        self.__cadreMenu = self.__arrTK.createFrame(self.__windows,width=150,height=630)
        self.__cadreAcceuil = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreUser = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreMeteo = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreGPS = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreRecherche = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreSoft = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreInternet = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreTheme = self.__arrTK.createFrame(self.__windows,width=350,height=630)
        self.__cadreArreraWork = self.__arrTK.createFrame(self.__windows, width=350, height=630)
        self.__cadreVideoDownload = self.__arrTK.createFrame(self.__windows, width=350, height=630)
        self.__cadreMicro = self.__arrTK.createFrame(self.__windows,width=350,height=630)

        #cadre interne a l'acceuil
        cadresPresentations = [
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1),
            self.__arrTK.createFrame(self.__cadreAcceuil,width=175,height=205,wightBoder=1)]
        #Widget
        labelTitreMenu = self.__arrTK.createLabel(self.__cadreMenu, text="Menu", ppolice="arial", ptaille=tailleTitle)
        labelcadresPresentations = [
            self.__arrTK.createLabel(cadresPresentations[0], text="Gestion recherche", ppolice="Arial", ptaille=17),
            self.__arrTK.createLabel(cadresPresentations[1], text="Gestion meteo", ppolice="Arial", ptaille=17),
            self.__arrTK.createLabel(cadresPresentations[2], text="Gestion GPS", ppolice="Arial", ptaille=17),
            self.__arrTK.createLabel(cadresPresentations[3], text="Gestion des logiciel", ppolice="Arial", ptaille=17),
            self.__arrTK.createLabel(cadresPresentations[4], text="Gestion Site internet", ppolice="Arial", ptaille=17)]
        
        boutonMenu = [
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Acceuil",command=self.__backAcceuil,width=20),#0
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Utilisateur",command=self.__showUserFrame,width=20),#1
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Meteo",command=lambda : self.__showMeteoFrame(1),width=20),#2
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="GPS",command=lambda : self.__showGPSFrame(1),width=20),#3
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Recherche",command=self.__showRechercheFrame,width=20),#4
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Logiciel",command=lambda : self.__showSoftFrame(1),width=20),#5
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Site Web",command=lambda :self.__showInternetFrame(1),width=20),#6
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Theme",command=self.__showThemeFrame,width=20),#7
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                                text="Arrera Work", command=self.__showArreraWorkFolder, width=20),#8
                        self.__arrTK.createButton(self.__cadreMenu, ppolice="arial",ptaille=23,
                                      text="Downloader",command=self.__showArreraDownloadFolder, width=20),  # 9
                        self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Micro",command=self.__showMicroFrame,width=20),#10
        ]

        self.__btnQUIT = self.__arrTK.createButton(self.__cadreMenu,ppolice="arial",ptaille=23,
                                                  text="Quitter",width=20)
        imgSoft = self.__arrTK.createImage(jsonSetting.lectureJSON("iconSoft"),
                                           tailleX=150,tailleY=150)

        self.__btnApropos = self.__arrTK.createButton(cadresPresentations[5],image=imgSoft,width=150,height=150)
        #cadresPresentations
        #0
        menuRecherche1 = self.__arrTK.createOptionMenu(cadresPresentations[0],var=self.__varRecherche,value=listMoteur)
        btnValiderMoteur1 = self.__arrTK.createButton(cadresPresentations[0],text="Valider"
                                                             ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda : self.__validerMoteur(2))
        #1
        btnMeteo1 = self.__arrTK.createButton(cadresPresentations[1],text="Ajouter\nune ville"
                                                     ,width=20,ppolice = "arial" , ptaille = tailleMain  ,command = lambda : self.__showMeteoFrame(2))
        #2
        btnGPSHome = self.__arrTK.createButton(cadresPresentations[2],text="Adresse\nde domicile"
                                                      ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda : self.__showGPSFrame(2))
        btnGPSWork = self.__arrTK.createButton(cadresPresentations[2],text="Adresse\nde travail"
                                                      ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda : self.__showGPSFrame(3))
        #3
        btnSoftware1 = self.__arrTK.createButton(cadresPresentations[3],text="Ajouter\nd'un logiciel"
                                                        ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda : self.__showSoftFrame(2))
        #4
        buttonAddSite = self.__arrTK.createButton(cadresPresentations[4],text="Ajouter"
                                                         ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda :self.__showInternetFrame(2))
        buttonSupprSite = self.__arrTK.createButton(cadresPresentations[4],text="Supprimer"
                                                           ,width=20,ppolice = "arial" , ptaille = tailleMain ,command=lambda :self.__showInternetFrame(3))

        # Cadre User 
        self.__labelTitreUser = self.__arrTK.createLabel(self.__cadreUser, ppolice="Arial", ptaille=tailleTitle)
        self.__btnPrenom = self.__arrTK.createButton(self.__cadreUser,ppolice = "arial" , ptaille = tailleMain
                                                     ,text="Nom de l'utilisateur",command=lambda : self.__affichageCadreUser(2))
        self.__btnGenre = self.__arrTK.createButton(self.__cadreUser,ppolice = "arial" , ptaille = tailleMain
                                                    ,text="genre de l'utilisateur",command=lambda : self.__affichageCadreUser(3))
        self.__menuGenre = self.__arrTK.createOptionMenu(self.__cadreUser,var=self.__varGenre,value=listGenre)
        self.__entryNameUser = self.__arrTK.createEntry(self.__cadreUser,ppolice="Arial",ptaille=tailleMain,width=250)
        self.__btnvaliderUser = self.__arrTK.createButton(self.__cadreUser,ppolice = "arial" , ptaille = tailleMain,
                                                          text="Valider",width=20)
        self.__btnAnulerUser = self.__arrTK.createButton(self.__cadreUser,ppolice = "arial" , ptaille = tailleMain,
                                                         text="Annuler",command=lambda : self.__affichageCadreUser(1),width=20)

        # Cadre Meteo 
        self.__labelTitreMeteo = self.__arrTK.createLabel(self.__cadreMeteo, ppolice="Arial", ptaille=tailleTitle)
        self.__btnListMeteo =  self.__arrTK.createButton(self.__cadreMeteo,text="Liste des villes enregistrées"
                                                         ,ppolice = "arial" , ptaille = tailleMain,command= lambda : self.__affichageCadreMeteo(2))
        self.__btnAddVille =   self.__arrTK.createButton(self.__cadreMeteo,text="Ajouter une ville"
                                                         ,ppolice = "arial" , ptaille = tailleMain,command= lambda : self.__affichageCadreMeteo(3))
        self.__btnSupprVille = self.__arrTK.createButton(self.__cadreMeteo,text="Supprimer une ville"
                                                         ,ppolice = "arial" , ptaille = tailleMain,command= lambda : self.__affichageCadreMeteo(4))
        self.__labelListeMeteo = self.__arrTK.createLabel(self.__cadreMeteo, ppolice="Arial", ptaille=tailleTitle)
        self.__menuChoixLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var=self.__varChoixLieu,value=listChoixLieu)
        self.__menuSupprLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var=self.__varSupprLieu,value=listChoixLieu)
        self.__entryVille = self.__arrTK.createEntry(self.__cadreMeteo,ppolice="Arial",ptaille=tailleMain)
        self.__btnvaliderMeteo = self.__arrTK.createButton(self.__cadreMeteo,text="Valider"
                                                           ,ppolice = "arial" , ptaille = tailleMain)
        self.__btnannulerMeteo = self.__arrTK.createButton(self.__cadreMeteo,ppolice = "arial" , ptaille = tailleMain
                                                           ,command= lambda : self.__affichageCadreMeteo(1))
        # Cadre GPS 
        self.__labelTitreGPS = self.__arrTK.createLabel(self.__cadreGPS, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAdresseDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du domicile"
                                                              ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(2))
        self.__btnAdresseWork = self.__arrTK.createButton(self.__cadreGPS,text="Adresse du lieu de travail"
                                                          ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(3))
        self.__btnvaliderGPS = self.__arrTK.createButton(self.__cadreGPS,text="Valider",ppolice = "arial" , ptaille = tailleMain)
        self.__btnretourGPS = self.__arrTK.createButton(self.__cadreGPS,text="Retour",ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(1))
        self.__btnSupprGPSDomicile = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du domicile"
                                                               ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerGPS(2,1))
        self.__btnSupprGPSWork = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer l'adresse du travail"
                                                           ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerGPS(2,2))
        self.__btnsupprGPS = self.__arrTK.createButton(self.__cadreGPS,text="Supprimer une adresse"
                                                       ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreGPS(4))
        self.__btnentryGPS = self.__arrTK.createEntry(self.__cadreGPS,ppolice="Arial",ptaille=tailleMain)
        # Cadre Rechecrhe
        labelTitreRecherche = self.__arrTK.createLabel(self.__cadreRecherche, text="Choisissez votre moteur\nde recherche"
                                                       , ppolice="Arial", ptaille=tailleTitle)
        menuMoteurRecherche = self.__arrTK.createOptionMenu(self.__cadreRecherche,var = self.__varMoteurRecherce,value = listMoteur)
        btnvaliderMoteur = self.__arrTK.createButton(self.__cadreRecherche,text="Valider"
                                                            ,ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerMoteur(1))
        # Cadre Software 
        self.__labelTitreSoftware = self.__arrTK.createLabel(self.__cadreSoft, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAnnulerSoft = self.__arrTK.createButton(self.__cadreSoft,text="Annuler",
                                                          ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(1))

        self.__btnValiderSoftAdd = self.__arrTK.createButton(self.__cadreSoft, text="Valider",
                                                             ppolice = "arial", ptaille = tailleMain,
                                                             command=lambda : self.__addSoftware(1))

        self.__btnValiderSoftSuppr = self.__arrTK.createButton(self.__cadreSoft, text="Valider",
                                                             ppolice="arial", ptaille=tailleMain,
                                                               command=lambda : self.__supprSoft())

        self.__btnAddSoft = self.__arrTK.createButton(self.__cadreSoft,text="Ajouter un logiciel",
                                                      ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(4))

        self.__btnSupprSoft= self.__arrTK.createButton(self.__cadreSoft,text="Supprimer un logiciel",
                                                       ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(3))

        self.__btnListSoft = self.__arrTK.createButton(self.__cadreSoft,text="Liste des logiciels",
                                                         ppolice = "arial" , ptaille = tailleMain,command=lambda:self.__affichageCadreSoft(5))

        self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var = self.__varSupprSoft,value = ["",""])

        self.__entryNameSoft = self.__arrTK.createEntry(self.__cadreSoft,ppolice="Arial",ptaille=15)

        self.__btnTypeSoftNormal = self.__arrTK.createButton(self.__cadreSoft,text="Normal",ppolice="arial",ptaille=tailleMain,
                                                             command=lambda : self.__affichageCadreSoft(2))
        self.__btnTypeSoftPresentation = self.__arrTK.createButton(self.__cadreSoft, text="Presentation", ppolice="arial", ptaille=tailleMain,
                                                                   command=lambda : self.__addSoftware(2))
        self.__btnTypeSoftNavigateur = self.__arrTK.createButton(self.__cadreSoft, text="Navigateur Internet", ppolice="arial", ptaille=tailleMain,
                                                                 command=lambda : self.__addSoftware(3))
        self.__btnTypeSoftNote = self.__arrTK.createButton(self.__cadreSoft, text="Note", ppolice="arial", ptaille=tailleMain,
                                                           command=lambda : self.__addSoftware(4))
        self.__btnTypeSoftMusique = self.__arrTK.createButton(self.__cadreSoft, text="Musique", ppolice="arial", ptaille=tailleMain,
                                                              command=lambda : self.__addSoftware(5))
        self.__btnRetourTypeSoft = self.__arrTK.createButton(self.__cadreSoft,text="Retour",ppolice="arial",ptaille=tailleMain,
                                                             command=lambda:self.__affichageCadreSoft(1))

        self.__textListSoft = ctk.CTkTextbox(self.__cadreSoft, width=300, height=550,wrap="word",
                                             state="normal", font=("Arial", 14))
        self.__btnRetourListeSoft = self.__arrTK.createButton(self.__cadreSoft,text="Retour",ppolice="arial",ptaille=tailleMain
                                                              ,command=lambda:self.__affichageCadreSoft(1))

        # Cadre Internet
        self.__labelTitreInternet = self.__arrTK.createLabel(self.__cadreInternet, ppolice="Arial", ptaille=tailleTitle)
        self.__btnAddSite = self.__arrTK.createButton(self.__cadreInternet,text="Enregister un site",
                                                      ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(2))
        self.__btnSupprSite = self.__arrTK.createButton(self.__cadreInternet,text="Supprimer un site",
                                                        ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(3))
        self.__btnAnnulerInternet = self.__arrTK.createButton(self.__cadreInternet,text="Annuler",
                                                              ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__affichageCadreSite(1))
        self.__btnValiderInternet = self.__arrTK.createButton(self.__cadreInternet,text="Valider",
                                                              ppolice = "arial" , ptaille = tailleMain)
        self.__entryNameSite = self.__arrTK.createEntry(self.__cadreInternet,ppolice="Arial",ptaille=tailleMain)
        self.__entryLinkSite = self.__arrTK.createEntry(self.__cadreInternet,ppolice="Arial",ptaille=tailleMain)
        self.__menuChoixSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varChoixSite,value = listChoixSite)
        self.__menuSupprSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var = self.__varSupprSite,value=listChoixSite)
        # Cardre theme 
        labelTitreTheme = self.__arrTK.createLabel(self.__cadreTheme, text="Choix du thème\nde l'interface"
                                                   , ppolice="Arial", ptaille=tailleTitle)
        menuChoixTheme = self.__arrTK.createOptionMenu(self.__cadreTheme,var = self.__varChoixTheme,value=listeTheme)
        btnValiderTheme = self.__arrTK.createButton (self.__cadreTheme,text="Valider",
                                                            ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerTheme(1))
        # Cadre Micro
        labelTitreMicro = self.__arrTK.createLabel(self.__cadreMicro, text="Sons au déclenchement\ndu micro",
                                                   ppolice="Arial", ptaille=tailleTitle)
        menuChoixMicro = self.__arrTK.createOptionMenu(self.__cadreMicro,
                                                              var = self.__varChoixMicro,value=self.__listChoixMicro)
        btnValiderMicro = self.__arrTK.createButton (self.__cadreMicro,text="Valider"
                                                            ,ppolice = "arial" , ptaille = tailleMain,command=self.__validerMicro)


        # Cader Work folder
        self.__labelTitreArreraWork = self.__arrTK.createLabel(self.__cadreArreraWork,
                                                               text="Choisir le dossier\npour Arrera Work",
                                                               ppolice="Arial", ptaille=tailleTitle)
        self.__btnFolderArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Choisir le dossier",
                                                               ppolice = "arial" , ptaille = tailleMain,command=lambda : self.__validerFolderWork(1))
        self.__btnSupprArreraWork = self.__arrTK.createButton(self.__cadreArreraWork, text="Supprimer le dossier",
                                                              ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderWork(2))
        # Cadre Download folder
        self.__labelTitreDownload = self.__arrTK.createLabel(self.__cadreVideoDownload,
                                                             text="Choisir le dossier pour\nArrera video download",
                                                             ppolice="Arial", ptaille=tailleTitle)
        self.__btnFolderDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Choisir le dossier",
                                                             ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(1))
        self.__btnSupprDownload = self.__arrTK.createButton(self.__cadreVideoDownload, text="Supprimer le dossier",
                                                            ppolice = "arial" , ptaille = tailleMain,command = lambda : self.__validerFolderDownload(2))
        # Placement widget
        self.__arrTK.placeTopCenter(labelTitreMenu)
        # Cadre acceuil
        self.__arrTK.placeCenter(self.__btnApropos)
        self.__arrTK.placeTopLeft(cadresPresentations[5])
        self.__arrTK.placeTopRight(cadresPresentations[0])
        self.__arrTK.placeCenterLeft(cadresPresentations[1])
        self.__arrTK.placeCenterRight(cadresPresentations[2])
        self.__arrTK.placeBottomLeft(cadresPresentations[3])
        self.__arrTK.placeBottomRight(cadresPresentations[4])

        for i in range(0,len(labelcadresPresentations)):
            self.__arrTK.placeTopCenter(labelcadresPresentations[i])
        
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
        if (jsonSetting.lectureJSON("gestionMicro")=="1"):
            boutonMenu[10].place(relx=0.0,y=550)

        self.__arrTK.placeCenter(menuRecherche1)
        self.__arrTK.placeBottomCenter(btnValiderMoteur1)
        self.__arrTK.placeCenter(btnMeteo1)
        self.__arrTK.placeCenter(btnGPSHome)
        self.__arrTK.placeBottomCenter(btnGPSWork)
        self.__arrTK.placeCenter(btnSoftware1)
        self.__arrTK.placeCenter(buttonAddSite)
        self.__arrTK.placeBottomCenter(buttonSupprSite)

        self.__arrTK.placeTopCenter(self.__labelTitreUser)

        self.__arrTK.placeTopCenter(self.__labelTitreMeteo)

        self.__arrTK.placeTopCenter(self.__labelTitreGPS)

        self.__arrTK.placeTopCenter(labelTitreRecherche)
        self.__arrTK.placeCenter(menuMoteurRecherche)
        self.__arrTK.placeBottomCenter(btnvaliderMoteur)

        self.__arrTK.placeTopCenter(self.__labelTitreSoftware)

        self.__arrTK.placeTopCenter(self.__labelTitreInternet)

        self.__arrTK.placeTopCenter(labelTitreTheme)
        self.__arrTK.placeCenter(menuChoixTheme)
        self.__arrTK.placeBottomCenter(btnValiderTheme)

        self.__arrTK.placeTopCenter(labelTitreMicro)
        self.__arrTK.placeCenter(menuChoixMicro)
        self.__arrTK.placeBottomCenter(btnValiderMicro)

        self.__arrTK.placeTopCenter(self.__labelTitreDownload)
        self.__arrTK.placeTopCenter(self.__labelTitreArreraWork)

            
        
    def active(self):
        self.__arrTK.setResizable(False)
        self.__arrTK.setGeometry(500,630)
        self.__arrTK.packRight(self.__cadreAcceuil)
        self.__arrTK.packLeft(self.__cadreMenu)

    def passQUITFNC(self,quitFNC):
        self.__btnQUIT.configure(command=lambda : self.__fncQuit(quitFNC))
        self.__arrTK.placeBottomCenter(self.__btnQUIT)
        self.__windows.protocol("WM_DELETE_WINDOW", lambda  : self.__fncQuit(quitFNC))

    def __fncQuit(self,quitFnc):
        self.__disableAllFrame()
        self.__cadreMenu.pack_forget()
        quitFnc()

    def __backAcceuil(self):
        self.__arrTK.packRight(self.__cadreAcceuil)
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
    
    def __disableAllFrame(self):
        self.__cadreAcceuil.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        self.__cadreMicro.pack_forget()
        self.__cadreArreraWork.pack_forget()
        self.__cadreVideoDownload.pack_forget()
    
    def __showUserFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreUser)
        self.__affichageCadreUser(1)
    
    def __showMeteoFrame(self,mode:int):
        """
        1 : Normal
        2 : add direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreMeteo)
        match mode :
            case 1 :
                self.__affichageCadreMeteo(1)
            case 2 :
                self.__affichageCadreMeteo(3)
    
    def __showGPSFrame(self,mode:int):
        """
        1 : Normal
        2 : Domicile direct
        3 : Work direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreGPS)
        match mode :
            case 1 :
                self.__affichageCadreGPS(1)
            case 2 :
                self.__affichageCadreGPS(2)
            case 3 :
                self.__affichageCadreGPS(3)

    def __showRechercheFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreRecherche)
    
    def __showSoftFrame(self,mode:int):
        """
        1 : Normal
        2 : Add direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreSoft)
        match mode :
            case 1 :
                self.__affichageCadreSoft(1)
            case 2 :
                self.__affichageCadreSoft(2)
    
    def __showInternetFrame(self,mode:int):
        """
        1 : Normal
        2 : Add direct
        3 : Suppr direct
        """
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreInternet)
        match mode :
            case 1 :
                self.__affichageCadreSite(1)
            case 2 :
                self.__affichageCadreSite(2)
            case 3 : 
                self.__affichageCadreSite(3)
    
    def __showThemeFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreTheme)
    
    def __showMicroFrame(self):
        self.__disableAllFrame()
        self.__arrTK.packRight(self.__cadreMicro)
        etatMicro = self.__gazelle.getSoundMicroAsEnable()
        if (etatMicro==True):
            self.__varChoixMicro.set(self.__listChoixMicro[0])
        else :
            self.__varChoixMicro.set(self.__listChoixMicro[1])
       

    def __affichageCadreUser(self,mode:int):
        """
        1 : Acceuil
        2 : Prenom 
        3 : Genre 
        """
        match mode :
            case 1 :
                self.__labelTitreUser.configure(text="Parametre de l'utilisateur")
                self.__btnPrenom.place(relx=0.5, y=200, anchor="n")
                self.__btnGenre.place(relx=0.5, y=275, anchor="n")
                self.__menuGenre.place_forget()
                self.__entryNameUser.place_forget()
                self.__btnvaliderUser.place_forget()
                self.__btnAnulerUser.place_forget()
            case 2 :
                self.__labelTitreUser.configure(text="Prénom de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place_forget()
                self.__entryNameUser.place(relx=0.5, rely=0.5, anchor="center")
                self.__btnvaliderUser.place(relx=1, rely=1, anchor='se')  
                self.__btnAnulerUser.place(relx=0, rely=1, anchor='sw')
                self.__btnvaliderUser.configure(command=lambda : self.__validerUser(1))
            case 3 :
                self.__labelTitreUser.configure(text="Genre de l'utilisateur")
                self.__btnPrenom.place_forget()
                self.__btnGenre.place_forget()
                self.__menuGenre.place(relx=0.5, rely=0.5, anchor="center")
                self.__entryNameUser.place_forget()
                self.__btnvaliderUser.place(relx=1, rely=1, anchor='se')
                self.__btnAnulerUser.place(relx=0, rely=1, anchor='sw')
                self.__btnvaliderUser.configure(command=lambda : self.__validerUser(2))
    
    def __validerUser(self,mode:int):
        """
        1 : User 
        2 : Genre
        """
        match mode :
            case 1 :
                name = self.__entryNameUser.get()
                if (name==""):
                    showerror("Parametre","Vous n'avez pas entré votre prénom")
                else :
                    self.__entryNameUser.delete(0,END)
                    self.__gazelle.changeUserName(name)
                    showinfo("Parametre","Prénom enregistré")
                    self.__affichageCadreUser(1)
            case 2 :
                genre = self.__varGenre.get()
                self.__gazelle.changeUserGenre(genre)
                showinfo("Parametre","genre enregistré")
                self.__affichageCadreUser(1)

    def __affichageCadreMeteo(self,mode:int):
        """
        1 : Acceuil 
        2 : Liste 
        3 : Ajout 
        4 : Suppr
        """
        match mode :
            case 1 :
                self.__labelTitreMeteo.configure(text="Paramètre Météo")
                #place(relx=0.2,y=200)
                self.__arrTK.placeCenterOnWidth(self.__btnListMeteo,y=150)
                self.__arrTK.placeCenterOnWidth(self.__btnAddVille,y=250)
                self.__arrTK.placeCenterOnWidth(self.__btnSupprVille,y=350)
                self.__btnvaliderMeteo.place_forget()
                self.__btnannulerMeteo.place_forget()
                self.__entryVille.place_forget()
                self.__labelListeMeteo.place_forget()
                self.__menuChoixLieu.place_forget()
                self.__menuSupprLieu.place_forget()
            case 2 : 
                self.__labelTitreMeteo.configure(text="Liste des lieux enregistrés")
                self.__btnListMeteo.place_forget()
                self.__btnAddVille.place_forget()
                self.__btnSupprVille.place_forget()
                # Recuperation de la liste des ville 
                self.__btnannulerMeteo.configure(text="Retour")
                self.__arrTK.placeBottomCenter(self.__btnannulerMeteo)
                listeVille = self.__gazelle.getMeteoSave()
                self.__labelListeMeteo.configure(text="")
                nbVille = len(listeVille)
                if (nbVille == 0 ) :
                    self.__labelListeMeteo.configure(text="Aucun lieu enregistré")
                else :
                    for i in range(0,nbVille):
                        texte = self.__labelListeMeteo.cget("text")
                        self.__labelListeMeteo.configure(text=texte+"\n"+listeVille[i])
    
                self.__labelListeMeteo.place(x=0,y=100)
            case 3 :
                self.__labelTitreMeteo.configure(text="Ajouter un lieu")
                self.__btnListMeteo.place_forget()
                self.__btnAddVille.place_forget()
                self.__btnSupprVille.place_forget()
                self.__menuChoixLieu.place(x=0,y=100)
                self.__btnannulerMeteo.configure(text="Annuler")
                self.__arrTK.placeBottomRight(self.__btnvaliderMeteo)
                self.__arrTK.placeBottomLeft(self.__btnannulerMeteo)
                self.__arrTK.placeCenter(self.__entryVille)
                self.__btnvaliderMeteo.configure(command=lambda : self.__validerMeteo(1))
            case 4 : 
                listeVille = self.__gazelle.getMeteoSave()
                self.__labelListeMeteo.configure(text="")
                nbVille = len(listeVille)
                if (nbVille == 0 ) :
                    showerror("Parametre","Aucun lieu enregistré")
                else :
                    self.__menuSupprLieu = self.__arrTK.createOptionMenu(self.__cadreMeteo,var = self.__varSupprLieu,value=listeVille)
                    self.__labelTitreMeteo.configure(text="Supprimer un lieu")
                    self.__btnListMeteo.place_forget()
                    self.__btnAddVille.place_forget()
                    self.__btnSupprVille.place_forget()
                    self.__menuChoixLieu.place_forget()
                    self.__btnannulerMeteo.configure(text="Annuler")
                    self.__btnvaliderMeteo.place(relx=1, rely=1, anchor='se')
                    self.__btnannulerMeteo.place(relx=0, rely=1, anchor='sw')
                    self.__menuSupprLieu.place(relx=0.5, rely=0.5, anchor="center")
                    self.__entryVille.place_forget()
                    self.__btnvaliderMeteo.configure(command=lambda : self.__validerMeteo(2))
    
    def __validerMeteo(self,mode:int):
        """
        1 : add 
        2 : suppr
        """
        match mode :
            case 1 :
                lieu = self.__entryVille.get()
                if (lieu==""):
                    showerror("Parametre","Impossible d'ajouter un lieu sans nom.")
                else :
                    choix = self.__varChoixLieu.get()
                    if (choix == "Simple"):
                        self.__gazelle.ajoutVilleMeteo(3,lieu)
                    else :
                        if (choix=="Domicile"):
                            self.__gazelle.ajoutVilleMeteo(1,lieu)
                        else :
                            if (choix=="Travail") :
                                self.__gazelle.ajoutVilleMeteo(2,lieu) 
                
                self.__entryVille.delete(0,END)    
                self.__affichageCadreMeteo(1)
            case 2 :
                choixSuppr = self.__varSupprLieu.get()
                if (choixSuppr == ""):
                    showerror("Parametre","Sélectionner le lieu à supprimer")
                else :
                    if (choixSuppr=="Lieu d'habitation enregister") :
                        self.__gazelle.supprVilleMeteo(1,"")
                    else :
                        if (choixSuppr=="Lieu de travail enregister") :
                            self.__gazelle.supprVilleMeteo(2,"")
                        else :
                            self.__gazelle.supprVilleMeteo(3,choixSuppr)
                self.__affichageCadreMeteo(1)
    
    def __affichageCadreGPS(self,mode:int):
        """
        1 : Acceuil
        2 : Domicile
        3 : Travail
        """
        match mode :
            case 1 :
                self.__labelTitreGPS.configure(text="Parametre GPS")
                self.__arrTK.placeCenterOnWidth(self.__btnAdresseDomicile,y=200)
                self.__arrTK.placeCenterOnWidth(self.__btnAdresseWork,y=275)
                self.__arrTK.placeCenterOnWidth(self.__btnsupprGPS,y=350)
                self.__btnvaliderGPS.place_forget()
                self.__btnretourGPS.place_forget()
                self.__btnentryGPS.place_forget()
                self.__btnSupprGPSDomicile.place_forget()
                self.__btnSupprGPSWork.place_forget()
            case 2 :
                self.__labelTitreGPS.configure(text="Adresse du domicile")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnsupprGPS.place_forget()
                self.__arrTK.placeBottomRight(self.__btnvaliderGPS)
                self.__arrTK.placeBottomLeft(self.__btnretourGPS)

                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,1))

            case 3 : 
                self.__labelTitreGPS.configure(text="Adresse du lieu de travail")
                self.__btnAdresseDomicile.place_forget()
                self.__btnAdresseWork.place_forget()
                self.__btnsupprGPS.place_forget()
                self.__btnvaliderGPS.place(relx=1, rely=1, anchor='se')
                self.__btnretourGPS.place(relx=0, rely=1, anchor='sw')
                self.__btnentryGPS.place(relx=0.5, rely=0.5, anchor="center") 
                self.__btnvaliderGPS.configure(command=lambda:self.__validerGPS(1,2))

            case 4 :
                if (self.__gazelle.getGPSAdresseIsSet(1) == False) and (self.__gazelle.getGPSAdresseIsSet(2) == False):
                    messagebox.showerror("Parametre","Il n'a aucune adresse enregistrée")
                else :
                    self.__labelTitreGPS.configure(text="Suppression d'adresse")
                    self.__btnAdresseDomicile.place_forget()
                    self.__btnAdresseWork.place_forget()
                    self.__btnsupprGPS.place_forget()
                    self.__arrTK.placeBottomLeft(self.__btnretourGPS)

                    if (self.__gazelle.getGPSAdresseIsSet(1)==True and self.__gazelle.getGPSAdresseIsSet(2) == True):
                        self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSDomicile,y=200)
                        self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSWork, y=275)
                    else :
                        if (self.__gazelle.getGPSAdresseIsSet(1)==True and self.__gazelle.getGPSAdresseIsSet(2) == False):
                            self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSDomicile, y=200)
                        else :
                            if (self.__gazelle.getGPSAdresseIsSet(1) == False and self.__gazelle.getGPSAdresseIsSet(2) == True):
                                self.__arrTK.placeCenterOnWidth(self.__btnSupprGPSWork, y=200)
    
    def __validerGPS(self,mode:int,type:int):
        """
        Mode : 
        1 : Add 
        2 : Suppr \n 
        Type : 
        1 : Domicile 
        2 : Travail
        """
        
        match mode :
            case 1 :
                adresse = self.__btnentryGPS.get()
                if (adresse==""):
                    showerror("Parametre","Entrer une adresse pour l'enregistrer")
                else :
                    self.__gazelle.ajoutGPSAdresse(type,adresse)
                    self.__btnentryGPS.delete(0,END)
                self.__affichageCadreGPS(1)
            case 2 : 
                self.__gazelle.supprGPSAdresse(type)
                self.__affichageCadreGPS(1)
    
    def __validerMoteur(self,mode:int):
        """
        1 : page
        2 : acceuil
        """
        match mode : 
            case 1 :
                moteur = self.__varMoteurRecherce.get()
            case 2 : 
                moteur = self.__varRecherche.get()
            case other :
                return
        self.__gazelle.changeMoteur(moteur)
        showinfo("Parametre","Moteur enregistré")
        self.__backAcceuil()

    def __affichageCadreSoft(self,mode:int):
        """
        1 : Acceuil 
        2 : Add
        3 : Suppr
        """
        self.__btnTypeSoftNormal.place_forget()
        self.__btnTypeSoftPresentation.place_forget()
        self.__btnTypeSoftNavigateur.place_forget()
        self.__btnTypeSoftNote.place_forget()
        self.__btnTypeSoftMusique.place_forget()
        self.__btnRetourTypeSoft.place_forget()
        self.__menuSupprSoft.place_forget()
        self.__entryNameSoft.place_forget()
        self.__btnAddSoft.place_forget()
        self.__btnSupprSoft.place_forget()
        self.__menuSupprSoft.place_forget()
        self.__btnAddSoft.place_forget()
        self.__btnSupprSoft.place_forget()
        self.__entryNameSoft.place_forget()
        self.__btnValiderSoftAdd.place_forget()
        self.__btnValiderSoftSuppr.place_forget()
        self.__textListSoft.place_forget()
        self.__btnRetourListeSoft.place_forget()
        self.__btnListSoft.place_forget()
        match mode : 
            case 1 :
                self.__labelTitreSoftware.configure(text="Gestion des logiciels")
                self.__btnAnnulerSoft.place_forget()
                self.__btnAddSoft.place(relx=0.5, y=200, anchor="n")
                self.__btnSupprSoft.place(relx=0.5, y=275, anchor="n")
                self.__btnListSoft.place(relx=0.5, y=350, anchor="n")

            case 2 :
                self.__labelTitreSoftware.configure(text="Ajout de logiciels")
                self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderSoftAdd.place(relx=1, rely=1, anchor='se')
                self.__entryNameSoft.place(relx=0.5, rely=0.5, anchor="center")

            case 3 :

                listSoft = self.__gazelle.getListSoft()
                if (len(listSoft)==0):
                    showerror("Parametre","Impossible de supprimer des logiciels avant d'en ajoute")
                    return
                del self.__menuSupprSoft
                self.__menuSupprSoft = self.__arrTK.createOptionMenu(self.__cadreSoft,var=self.__varSupprSoft,value=listSoft)
                self.__labelTitreSoftware.configure(text="Suppression de logiciel")
                self.__btnAnnulerSoft.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderSoftSuppr.place(relx=1, rely=1, anchor='se')
                self.__menuSupprSoft.place(relx=0.5, rely=0.5, anchor="center")

            case 4 :
                self.__labelTitreSoftware.configure(text="Type du logiciel ajouter")
                self.__btnTypeSoftNormal.place(relx=0.5, y=100, anchor="n")
                self.__btnTypeSoftPresentation.place(relx=0.5, y=150, anchor="n")
                self.__btnTypeSoftNavigateur.place(relx=0.5, y=200, anchor="n")
                self.__btnTypeSoftNote.place(relx=0.5, y=250, anchor="n")
                self.__btnTypeSoftMusique.place(relx=0.5, y=300, anchor="n")
                self.__arrTK.placeBottomCenter(self.__btnRetourTypeSoft)

            case 5 :
                self.__labelTitreSoftware.configure(text="Liste des logiciels")
                listSoft = self.__gazelle.getListSoft()
                if (len(listSoft)==0):
                    messagebox.showerror("Parametre","Aucun logiciel enregistré")
                else :
                    self.__textListSoft.delete(1.0,END)
                    self.__textListSoft.configure(state="normal")
                    for i in range(0, len(listSoft)):
                        self.__textListSoft.insert(END, listSoft[i] + "\n")
                    self.__textListSoft.configure(state="disabled")

                self.__arrTK.placeCenter(self.__textListSoft)
                self.__arrTK.placeBottomCenter(self.__btnRetourListeSoft)


    def __addSoftware(self, mode:int):
        """
        1 : normal
        2 : Presentation
        3 : Navigateur
        4 : Note
        5 : Musique
        """
        match mode:
            case 1 :
                soft = self.__entryNameSoft.get()
                if (soft==""):
                    showerror("Parametre","Impossible d'ajouter un logiciel sans nom")
                else :
                    self.__gazelle.addSoft(1,soft)
                    showinfo("Parametre","Logiciel ajouté")
                    self.__entryNameSoft.delete(0,END)
            case 2:
                self.__gazelle.addSoft(2, "presentation")
            case 3:
                self.__gazelle.addSoft(3, "navigateur")
            case 4:
                self.__gazelle.addSoft(4, "musique")
            case 5:
                self.__gazelle.addSoft(5, "note")
        self.__affichageCadreSoft(1)

    def __supprSoft(self):
        soft = self.__varSupprSoft.get()
        if (soft == "Presentation"):
            self.__gazelle.supprSoft(2, "")
        else:
            if (soft == "Navigateur internet"):
                self.__gazelle.supprSoft(3, "")
            else:
                if (soft == "Note"):
                    self.__gazelle.supprSoft(5, "")
                else:
                    if (soft == "Musique"):
                        self.__gazelle.supprSoft(4, "")
                    else:
                        self.__gazelle.supprSoft(1, soft)
        self.__affichageCadreSoft(1)

    
    def __affichageCadreSite(self,mode:int):
        """
        1 : Acceuil
        2 : Add
        3 : Suppr
        """
        match mode :
            case 1 :
                self.__labelTitreInternet.configure(text="Gestion des sites\nInternet")
                self.__btnAddSite.place(relx=0.2,y=200)
                self.__btnSupprSite.place(relx=0.2,y=275)
                self.__btnAnnulerInternet.place_forget()
                self.__btnValiderInternet.place_forget()
                self.__entryNameSite.place_forget()
                self.__entryLinkSite.place_forget()
                self.__menuChoixSite.place_forget()
                self.__menuSupprSite.place_forget()
            case 2 : 
                self.__labelTitreInternet.configure(text="Enregistrement d'un site")
                self.__btnAddSite.place_forget()
                self.__btnSupprSite.place_forget()
                self.__btnAnnulerInternet.place(relx=0, rely=1, anchor='sw')
                self.__btnValiderInternet.place(relx=1, rely=1, anchor='se')
                self.__entryNameSite.place(relx=0.2,y=200)
                self.__entryLinkSite.place(relx=0.2,y=275)
                self.__menuChoixSite.place(x=0,y=100)
                self.__menuSupprSite.place_forget()
                self.__btnValiderInternet.configure(command=lambda:self.__validerSite(1))
            case 3 : 
                listSite = self.__gazelle.getListSite()
                if (len(listSite)==0):
                    showerror("Parametre","Aucun site enregistré")
                else :
                    self.__menuSupprSite =  self.__arrTK.createOptionMenu(self.__cadreInternet,var=self.__varSupprSite,value=listSite)
                    self.__labelTitreInternet.configure(text="Enregistrement d'un site")
                    self.__btnAddSite.place_forget()
                    self.__btnSupprSite.place_forget()
                    self.__btnAnnulerInternet.place(relx=0, rely=1, anchor='sw')
                    self.__btnValiderInternet.place(relx=1, rely=1, anchor='se')
                    self.__entryNameSite.place_forget()
                    self.__entryLinkSite.place_forget()
                    self.__menuChoixSite.place_forget()
                    self.__menuSupprSite.place(relx=0.5,rely=0.5,anchor="center")
                    self.__btnValiderInternet.configure(command=lambda:self.__validerSite(2))
                    self.__varSupprSite.set(listSite[0])
                    

    
    def __validerSite(self,mode:int):
        """
        1 : add
        2 : suppr
        """
        match mode :
            case 1 :
                link = self.__entryLinkSite.get()
                if (link!="") :
                    type = self.__varChoixSite.get()
                    if (type == "Cloud"):
                        self.__gazelle.addSite(2,"",link)
                    else :
                        name = self.__entryNameSite.get()
                        if(name=="") :
                            showerror("Parametre","Impossible d'enregistrer un site sans nom")
                        else :
                            self.__gazelle.addSite(1,name,link)
                            showinfo("Parametre","Site enregistré")
                            self.__affichageCadreSite(1)
                else :
                    showerror("Parametre","Impossible d'enregistrer un site sans URL")
                
                self.__entryLinkSite.delete(0,END)
                self.__entryNameSite.delete(0,END)
            case 2 : 
                site = self.__varSupprSite.get()
                if (site == "Cloud") :
                    self.__gazelle.supprSite(2,"")
                else :
                    self.__gazelle.supprSite(1,site)
                showinfo("Parametre","Site supprimer")
                self.__affichageCadreSite(1)  
    
    def __validerTheme(self,mode:int):
        """
        1 : Page 
        2 : Acceuil
        """
        match mode :
            case 1 :
                theme = self.__varChoixTheme.get()
            case 2 :
                theme = self.__varTheme.get()
            case other :
                return
        self.__gazelle.changeTheme(theme)
        showinfo("Parametre","Theme changer")
        self.__backAcceuil()
    
    def __validerMicro(self):
        sortie = self.__varChoixMicro.get()
        if (sortie=="ON"):
            self.__gazelle.changeSoundMicro(True)
        else :
            self.__gazelle.changeSoundMicro(False)
        self.__backAcceuil()

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
        print("test")
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
        self.__btnApropos.configure(command=aproposFNC)