from tkinter.messagebox import showinfo, showerror
from librairy.arrera_tk import *
from librairy.travailJSON import *
from librairy.dectectionOS import *
from librairy.gestionSoftWindows import *


class ArreraLynx:
    def __init__(self, fichierLynx: str, fichierUser: str, fichierNeuron: str):
        # objet
        self.__fichierLynx = jsonWork(fichierLynx)
        self.__fileUser = jsonWork(fichierUser)
        self.__fileNeuron = jsonWork(fichierNeuron)
        self.__dectOS = OS()
        self.__arrTk = CArreraTK()
        if self.__dectOS.osWindows() == True:
            self.__softWin = gestionSoftWindows(self.__fileNeuron.lectureJSON("emplacementSoftWindows"))

        # Variable
        nomSoft = self.__fichierLynx.lectureJSON("nameSoft")

        if self.__dectOS.osWindows() == True:
            iconLogiciel = os.path.abspath(self.__fichierLynx.lectureJSON("iconSoftWin"))
        else:
            iconLogiciel = os.path.abspath(self.__fichierLynx.lectureJSON("iconSoftLinux"))

        listGenre = self.__fichierLynx.lectureJSONList("listGenre")

        # Gestion du theme
        if self.__arrTk.getTheme() == "Light" :
            windowsColor = "#f0f0f0"
            textColor = "#000000"
        else :
            windowsColor = "#000000"
            textColor = "#FFFFFF"

        # Fenetre
        self.__windows = self.__arrTk.aTK(width=700,
                                          height=500,
                                          title=nomSoft + ": Premier demarage",
                                          resizable=False
                                          ,icon=iconLogiciel,
                                          bg=windowsColor,fg=textColor)
        self.__varGenre = StringVar(self.__windows)

        self.__userIN = False
        self.__genreIN = False
        # cadre tkinter
        self.__frameAcceuil = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameUserName = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameUserGenre = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameWeather = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameAddWeather = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameGPS = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameAddGPS = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameSoft = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameSoftLinux = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameWeb = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameAddWeb = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameWorkFolder = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__framevideoDownloadFolder = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        self.__frameEnd = self.__arrTk.createFrame(self.__windows, width=700, height=500,bg=windowsColor)
        # widget
        labelTitre = [
            self.__arrTk.createLabel(self.__frameAcceuil, text="Bienvenu sur Arrera " + nomSoft,
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 0
            self.__arrTk.createLabel(self.__frameUserName, text="Nom d'utilisateur",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 1
            self.__arrTk.createLabel(self.__frameUserGenre, text="Genre d'utilisateur",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 2
            self.__arrTk.createLabel(self.__frameWeather, text="Meteo",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 3
            self.__arrTk.createLabel(self.__frameGPS, text="GPS",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 4
            self.__arrTk.createLabel(self.__frameSoft, text="Logiciel",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 5
            self.__arrTk.createLabel(self.__frameWeb, text="Site internet",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 6
            self.__arrTk.createLabel(self.__frameWorkFolder, text="Sélectionner le dossier de travail Arrera",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 7
            self.__arrTk.createLabel(self.__framevideoDownloadFolder,
                                     text="Sélectionner le dossier de téléchargement\nde vidéos et de musique",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor),  # 8
            self.__arrTk.createLabel(self.__frameEnd, text="Configuration terminer",
                                     ppolice="Arial", ptaille=35,bg=windowsColor,fg=textColor)  # 9
        ]
        btnSuivant = [
            self.__arrTk.createButton(self.__frameAcceuil, ppolice="Arial", ptaille=25,
                                      text="Commencer", command=self.__passUserName),  # 0
            self.__arrTk.createButton(self.__frameUserName, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passUserGenre),  # 1
            self.__arrTk.createButton(self.__frameUserGenre, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passMeteo),  # 2
            self.__arrTk.createButton(self.__frameWeather, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passGPS),  # 3
            self.__arrTk.createButton(self.__frameGPS, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passSoft),  # 4
            self.__arrTk.createButton(self.__frameSoft, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passWeb),  # 5
            self.__arrTk.createButton(self.__frameWeb, ppolice="Arial", ptaille=25,
                                      text="Suivant", command=self.__passWorkFolder),  # 6
            self.__arrTk.createButton(self.__frameWorkFolder, ppolice="Arial", ptaille=25,
                                      text="Passer", command= lambda : self.__passVideoDownloadFolder()),  # 7
            self.__arrTk.createButton(self.__framevideoDownloadFolder, ppolice="Arial", ptaille=25,
                                      text="Passer", command= lambda  : self.__passEnd()),  # 8
            self.__arrTk.createButton(self.__frameEnd, ppolice="Arial", ptaille=25,
                                      text="Commencer à utiliser " + nomSoft, command=self.__end)  # 9
        ]
        # frameUserName & frameUserGenre

        self.entryName = self.__arrTk.createEntry(self.__frameUserName, ppolice="Arial", ptaille=25,
                                                  placeholderText="Nom d'utilisateur", width=300)
        menuGenre = self.__arrTk.createOptionMenu(self.__frameUserGenre, var=self.__varGenre, value=listGenre,
                                                  police="Arial", taille=25)
        # frameWeather
        btnDomicile = self.__arrTk.createButton(self.__frameWeather, ppolice="Arial", ptaille=25
                                                , text="Domicile",
                                                command=lambda: self.__viewAddMeteo("domicile"))
        btnTravail = self.__arrTk.createButton(self.__frameWeather, ppolice="Arial", ptaille=25
                                               , text="Lien de travail",
                                               command=lambda: self.__viewAddMeteo("travail"))
        btnVille = self.__arrTk.createButton(self.__frameWeather, ppolice="Arial", ptaille=25
                                             , text="Ajouter une ville",
                                             command=lambda: self.__viewAddMeteo("ville"))
        # frameAddWeather
        self.__labelTitreAdd = [
            self.__arrTk.createLabel(self.__frameAddWeather, ppolice="Arial", ptaille=25, text="Domicile"
                                     ,bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameAddWeather, ppolice="Arial", ptaille=25, text="Ville"
                                     ,bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameAddWeather, ppolice="Arial", ptaille=25, text="Travail"
                                     ,bg=windowsColor,fg=textColor)]

        self.__entryVille = self.__arrTk.createEntry(self.__frameAddWeather, ppolice="Arial", ptaille=25
                                                     , width=300)
        self.__btnAdd = self.__arrTk.createButton(self.__frameAddWeather, ppolice="Arial", ptaille=25, text="Ajouter")
        # frameGPS
        btnAdresseDomicile = self.__arrTk.createButton(self.__frameGPS, ppolice="Arial", ptaille=25
                                                       , text="Adresse de domicile"
                                                       , command=lambda: self.__viewAddGPS("domicile"))
        btnAdresseTravail = self.__arrTk.createButton(self.__frameGPS, ppolice="Arial", ptaille=25
                                                      , text="Adresse de Travail"
                                                      , command=lambda: self.__viewAddGPS("travail"))
        # frameAddGPS
        self.__labelTitreGPSAdd = [
            self.__arrTk.createLabel(self.__frameAddGPS, ppolice="Arial", ptaille=25
                                     , text="Adresse de votre domicile",bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameAddGPS, ppolice="Arial", ptaille=25
                                     , text="Adresse de votre lieu de travail",bg=windowsColor,fg=textColor)
        ]
        self.__entryAdresse = self.__arrTk.createEntry(self.__frameAddGPS, width=500, ppolice="Arial", ptaille=25)
        self.__btnGPSAdd = self.__arrTk.createButton(self.__frameAddGPS, ppolice="Arial", ptaille=25, text="Ajouter")
        # frameSoft
        # Frame pour mieux placer le bouton
        frameLeftSoft = self.__arrTk.createFrame(self.__frameSoft, width=300, height=350,
                                     bg=windowsColor)
        frameRightSoft = self.__arrTk.createFrame(self.__frameSoft, width=300, height=350,
                                      bg=windowsColor)

        btnWord = self.__arrTk.createButton(frameLeftSoft, ppolice="Arial", ptaille=25,
                                            text="Traitement de texte", command=lambda: self.__viewAddSoft("Ttexte"))
        btnExel = self.__arrTk.createButton(frameLeftSoft, ppolice="Arial", ptaille=25,
                                            text="Tableur", command=lambda: self.__viewAddSoft("tableur"))
        btnPresentation = self.__arrTk.createButton(frameLeftSoft, ppolice="Arial", ptaille=25,
                                                    text="Presentation",
                                                    command=lambda: self.__viewAddSoft("presentation"))
        btnBrowser = self.__arrTk.createButton(frameRightSoft, ppolice="Arial", ptaille=25,
                                               text="Navigateur", command=lambda: self.__viewAddSoft("internet"))
        btnNote = self.__arrTk.createButton(frameRightSoft, ppolice="Arial", ptaille=25,
                                            text="Note", command=lambda: self.__viewAddSoft("note"))
        btnMusic = self.__arrTk.createButton(frameRightSoft, ppolice="Arial", ptaille=25,
                                             text="Musique", command=lambda: self.__viewAddSoft("musique"))
        # frameAddSoft
        self.__labelTitreSoftLinux = [
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un logiciel de traitement de texte",
                                     bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un tableur",bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un logiciel de presentation",
                                     bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un navigateur internet",
                                     bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un logiciel de note",
                                     bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                     text="Ajouter un logiciel de musique",
                                     bg=windowsColor,fg=textColor),
        ]
        # self.__entryCommandLinux = self.__arrTk.createEntry(self.__frameSoftLinux,width=300,placeholderText="",ppolice="Arial",ptaille=25)
        self.__btnAddSoftLinux = self.__arrTk.createButton(self.__frameSoftLinux, ppolice="Arial", ptaille=25,
                                                           text="Choisir le programme")
        # frameWeb
        btnCloud = self.__arrTk.createButton(self.__frameWeb, ppolice="Arial", ptaille=25,
                                             text="Stokage cloud ", command=lambda: self.__viewAddWeb("cloud"))
        btnSiteWeb = self.__arrTk.createButton(self.__frameWeb, ppolice="Arial", ptaille=25,
                                               text="Racourcie site", command=lambda: self.__viewAddWeb("site"))
        # frameAddWeb
        self.__labelIndicationWeb = [
            self.__arrTk.createLabel(self.__frameAddWeb, ppolice="Arial", ptaille=25,
                                     text="Lien de votre stokage cloud",
                                     bg=windowsColor,fg=textColor),
            self.__arrTk.createLabel(self.__frameAddWeb, ppolice="Arial", ptaille=25, text="Racourcie d'un site")]
        self.__entryNameSite = self.__arrTk.createEntry(self.__frameAddWeb, ppolice="Arial", ptaille=25, width=300)
        self.__entryLienSite = self.__arrTk.createEntry(self.__frameAddWeb, ppolice="Arial", ptaille=25, width=300)
        self.__btnAddSite = self.__arrTk.createButton(self.__frameAddWeb, ppolice="Arial", ptaille=25, text="Ajouter")

        # FrameFolderWork

        btnChooseWorkFolder = self.__arrTk.createButton(self.__frameWorkFolder, ppolice="Arial", ptaille=25,
                                      text="Choisir le dossier de travail", command=self.__addFolderWork)

        # FrameVideoDownloadFolder

        btnChosseVideoFolder = self.__arrTk.createButton(self.__framevideoDownloadFolder, ppolice="Arial", ptaille=25,
                                      text="Choisir le dossier de téléchargement", command= lambda  : self.__addFolderVideo())

        # affichage
        # frameAcceuil
        self.__arrTk.placeTopCenter(labelTitre[0])
        self.__arrTk.placeCenter(btnSuivant[0])
        # frameUserName
        self.__arrTk.placeTopCenter(labelTitre[1])
        self.__arrTk.placeCenter(self.entryName)
        self.__arrTk.placeBottomCenter(btnSuivant[1])
        # frameUserGenre
        self.__arrTk.placeTopCenter(labelTitre[2])
        self.__arrTk.placeCenter(menuGenre)
        self.__arrTk.placeBottomCenter(btnSuivant[2])

        # frameWeather
        self.__arrTk.placeTopCenter(labelTitre[3])
        self.__arrTk.placeLeftCenter(btnDomicile)
        self.__arrTk.placeCenter(btnVille)
        self.__arrTk.placeRightCenter(btnTravail)
        self.__arrTk.placeBottomCenter(btnSuivant[3])
        # frameAddWeather
        self.__arrTk.placeCenter(self.__entryVille)
        self.__arrTk.placeBottomCenter(self.__btnAdd)
        # frameGPS
        self.__arrTk.placeTopCenter(labelTitre[4])
        self.__arrTk.placeLeftCenter(btnAdresseDomicile)
        self.__arrTk.placeRightCenter(btnAdresseTravail)
        self.__arrTk.placeBottomCenter(btnSuivant[4])
        # frameAddGPS
        self.__arrTk.placeCenter(self.__entryAdresse)
        self.__arrTk.placeBottomCenter(self.__btnGPSAdd)
        # frameSoft
        self.__arrTk.placeTopCenter(labelTitre[5])

        self.__arrTk.placeLeftCenter(frameLeftSoft)
        self.__arrTk.placeRightCenter(frameRightSoft)

        self.__arrTk.placeTopCenter(btnWord)
        self.__arrTk.placeCenter(btnExel)
        self.__arrTk.placeBottomCenter(btnPresentation)

        self.__arrTk.placeTopCenter(btnBrowser)
        self.__arrTk.placeCenter(btnNote)
        self.__arrTk.placeBottomCenter(btnMusic)
        self.__arrTk.placeBottomCenter(btnSuivant[5])
        # frameAddSof
        self.__arrTk.placeCenter(self.__btnAddSoftLinux)
        # frameWeb
        self.__arrTk.placeTopCenter(labelTitre[6])
        self.__arrTk.placeLeftCenter(btnCloud)
        self.__arrTk.placeRightCenter(btnSiteWeb)
        self.__arrTk.placeBottomCenter(btnSuivant[6])
        # frameAddWeb
        self.__arrTk.placeBottomCenter(self.__btnAddSite)
        # FrameFolderWork
        self.__arrTk.placeTopCenter(labelTitre[7])
        self.__arrTk.placeCenter(btnChooseWorkFolder)
        self.__arrTk.placeBottomCenter(btnSuivant[7])
        # FrameVideoDownloadFolder
        self.__arrTk.placeTopCenter(labelTitre[8])
        self.__arrTk.placeCenter(btnChosseVideoFolder)
        self.__arrTk.placeBottomCenter(btnSuivant[8])
        # frameEnd
        self.__arrTk.placeTopCenter(labelTitre[9])
        self.__arrTk.placeCenter(btnSuivant[9])

    def confiCreate(self):
        if self.__userIN == True and self.__genreIN == True:
            return True
        else:
            return False

    def __clearView(self):
        self.__frameAcceuil.pack_forget()
        self.__frameUserName.pack_forget()
        self.__frameUserGenre.pack_forget()
        self.__frameWeather.pack_forget()
        self.__frameAddWeather.pack_forget()
        self.__frameGPS.pack_forget()
        self.__frameAddGPS.pack_forget()
        self.__frameSoft.pack_forget()
        self.__frameSoftLinux.pack_forget()
        self.__frameWeb.pack_forget()
        self.__frameAddWeb.pack_forget()
        self.__framevideoDownloadFolder.pack_forget()
        self.__frameWorkFolder.pack_forget()
        self.__frameEnd.pack_forget()

    def active(self):
        self.__frameAcceuil.pack()
        self.__arrTk.view()

    def __passUserName(self):
        self.__clearView()
        self.__frameUserName.pack()

    def __passUserGenre(self):
        if self.entryName.get():
            self.__clearView()
            self.__arrTk.pack(self.__frameUserGenre)
            self.__fileUser.EcritureJSON("user", self.entryName.get())
            self.__userIN = True
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un nom d'utilisateur avant de continuer")

    def __activeFrameWeather(self):
        self.__clearView()
        self.__frameWeather.pack()

    def __passMeteo(self):
        if self.__varGenre.get():
            self.__activeFrameWeather()
            self.__fileUser.EcritureJSON("genre", self.__varGenre.get())
            self.__genreIN = True
        else:
            messagebox.showerror("Erreur", "Veuillez entrer selectionner un genre avant de continuer")

    def __viewAddMeteo(self, mode):
        self.__clearView()
        self.__entryVille.delete("0", END)
        self.__arrTk.pack(self.__frameAddWeather)
        self.__labelTitreAdd[0].place_forget()
        self.__labelTitreAdd[1].place_forget()
        self.__labelTitreAdd[2].place_forget()
        if mode == "domicile":
            self.__arrTk.placeTopCenter(self.__labelTitreAdd[0])
            self.__btnAdd.configure(command=lambda: self.__addMeteo(mode))
        else:
            if mode == "travail":
                self.__arrTk.placeTopCenter(self.__labelTitreAdd[2])
                self.__btnAdd.configure(command=lambda: self.__addMeteo(mode))
            else:
                if mode == "ville":
                    self.__arrTk.placeTopCenter(self.__labelTitreAdd[1])
                    self.__btnAdd.configure(command=lambda: self.__addMeteo(mode))

    def __addMeteo(self, mode):
        valeur = self.__entryVille.get()
        if valeur:
            if mode == "domicile":
                self.__fileUser.EcritureJSON("lieuDomicile", valeur)
            else:
                if mode == "travail":
                    self.__fileUser.EcritureJSON("lieuTravail", valeur)
                else:
                    if mode == "ville":
                        self.__fileUser.EcritureJSONList("listVille", valeur)
            self.__activeFrameWeather()
        else:
            self.__activeFrameWeather()
            messagebox.showerror("Erreur", "Aucun ville n'a été marquer dans la zone de texte")

    def __passGPS(self):
        self.__clearView()
        self.__arrTk.pack(self.__frameGPS)

    def __viewAddGPS(self, mode: str):
        self.__clearView()
        self.__arrTk.pack(self.__frameAddGPS)
        self.__entryAdresse.delete("0", END)
        self.__labelTitreGPSAdd[0].place_forget()
        self.__labelTitreGPSAdd[1].place_forget()
        if mode == "domicile":
            self.__arrTk.placeTopCenter(self.__labelTitreGPSAdd[0])
            self.__btnGPSAdd.configure(command=lambda: self.__addGPS(mode))
        else:
            if mode == "travail":
                self.__arrTk.placeTopCenter(self.__labelTitreGPSAdd[1])
                self.__btnGPSAdd.configure(command=lambda: self.__addGPS(mode))

    def __addGPS(self, mode: str):
        valeur = self.__entryAdresse.get()
        if valeur:
            if mode == "domicile":
                self.__fileUser.EcritureJSON("adresseDomicile", valeur)
                self.__passGPS()
            else:
                if mode == "travail":
                    self.__fileUser.EcritureJSON("adresseTravail", valeur)
                    self.__passGPS()
        else:
            self.__passGPS()
            messagebox.showerror("Erreur", "Aucun adresse n'a été marquer dans la zone de texte")

    def __passSoft(self):
        if (self.__dectOS.osWindows() == True):
            sortie = ""
            while not sortie:
                messagebox.showinfo("Infomation", "Vous devait selectionner un dossier deja crée")
                sortie = self.__softWin.setEmplacementSoft()
                self.__fileNeuron.EcritureJSON("emplacementSoftWindows", sortie)
        self.__clearView()
        self.__frameSoft.pack()

    def __viewAddSoft(self, mode: str):
        if (self.__dectOS.osWindows() == True):
            if mode == "Ttexte":
                self.__softWin.setName("Ttexte")
                self.__softWin.saveSoftware()
                self.__fileUser.EcritureJSON("wordWindows", self.__softWin.getName())
            else:
                if mode == "tableur":
                    self.__softWin.setName("tableur")
                    self.__softWin.saveSoftware()
                    self.__fileUser.EcritureJSON("exelWindows", self.__softWin.getName())
                else:
                    if mode == "presentation":
                        self.__softWin.setName("presentation")
                        self.__softWin.saveSoftware()
                        self.__fileUser.EcritureJSON("diapoWindows", self.__softWin.getName())
                    else:
                        if mode == "internet":
                            self.__softWin.setName("internet")
                            self.__softWin.saveSoftware()
                            self.__fileUser.EcritureJSON("browserWindows", self.__softWin.getName())
                        else:
                            if mode == "note":
                                self.__softWin.setName("note")
                                self.__softWin.saveSoftware()
                                self.__fileUser.EcritureJSON("noteWindows", self.__softWin.getName())
                            else:
                                if mode == "musique":
                                    self.__softWin.setName("musique")
                                    self.__softWin.saveSoftware()
                                    self.__fileUser.EcritureJSON("musicWindows", self.__softWin.getName())
        else:
            if (self.__dectOS.osLinux() == True):
                # self.__entryCommandLinux.delete("0",END)
                self.__clearView()
                self.__arrTk.pack(self.__frameSoftLinux)
                for i in range(0, 5):
                    self.__labelTitreSoftLinux[i].place_forget()
                if mode == "Ttexte":
                    self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[0])
                else:
                    if mode == "tableur":
                        self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[1])
                    else:
                        if mode == "presentation":
                            self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[2])
                        else:
                            if mode == "internet":
                                self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[3])
                            else:
                                if mode == "note":
                                    self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[4])
                                else:
                                    if mode == "musique":
                                        self.__arrTk.placeTopCenter(self.__labelTitreSoftLinux[5])
                self.__btnAddSoftLinux.configure(command=lambda: self.__addSoftLinux(mode))

    def __addSoftLinux(self, mode: str):
        reponse = messagebox.askquestion(
            "Choix repertoire",
            "Le programme se trouve-t-il dans votre répertoire /home ?",
            icon="question"
        )
        if reponse == "yes":
            command = filedialog.askopenfilename(
                title="Sélectionner un programme",
                initialdir=os.path.expanduser("~"),  # Définit le répertoire initial sur le home de l'utilisateur
                filetypes=[("Tous les fichiers", "*")]
            )
        else:
            command = filedialog.askopenfilename(
                title="Selectionner un programme",
                initialdir="/bin",
                filetypes=[("Tous les fichiers", "*")])
        if command:
            if mode == "Ttexte":
                self.__fileUser.EcritureJSON("wordLinux", command)
            else:
                if mode == "tableur":
                    self.__fileUser.EcritureJSON("exelLinux", command)
                else:
                    if mode == "presentation":
                        self.__fileUser.EcritureJSON("diapoLinux", command)
                    else:
                        if mode == "internet":
                            self.__fileUser.EcritureJSON("browserLinux", command)
                        else:
                            if mode == "note":
                                self.__fileUser.EcritureJSON("noteLinux", command)
                            else:
                                if mode == "musique":
                                    self.__fileUser.EcritureJSON("musicLinux", command)
            messagebox.showinfo("Enregistrement logiciel", "Votre logiciel a ete enregister")
        else:
            messagebox.showerror("Erreur", "Veuillez marquer une command pour l'enregistrer le logiciel")
        self.__clearView()
        self.__passSoft()

    def __passWeb(self):
        self.__clearView()
        self.__arrTk.pack(self.__frameWeb)

    def __viewAddWeb(self, mode: str):
        self.__clearView()
        self.__arrTk.pack(self.__frameAddWeb)
        self.__entryLienSite.delete("0", END)
        self.__entryNameSite.delete("0", END)
        self.__entryLienSite.place_forget()
        self.__entryNameSite.place_forget()
        for i in range(0, 1):
            self.__labelIndicationWeb[i].place_forget()
        largeurFrame = self.__frameAcceuil.winfo_reqwidth()
        if mode == "cloud":
            self.__arrTk.placeTopCenter(self.__labelIndicationWeb[0])
            self.__arrTk.placeCenter(self.__entryLienSite)
            self.__btnAddSite.configure(command=lambda: self.__addWeb("cloud"))
        else:
            if mode == "site":
                self.__arrTk.placeTopCenter(self.__labelIndicationWeb[1])
                self.__entryLienSite.place(x=((largeurFrame - self.__entryLienSite.winfo_reqwidth()) // 2), y=200)
                self.__entryNameSite.place(x=((largeurFrame - self.__entryNameSite.winfo_reqwidth()) // 2), y=100)
                self.__btnAddSite.configure(command=lambda: self.__addWeb("site"))

    def __addWeb(self, mode: str):
        self.__passWeb()
        if mode == "cloud":
            lien = self.__entryLienSite.get()
            if lien:
                self.__fileUser.EcritureJSON("lienCloud", lien)
                messagebox.showinfo("Lien", "Votre lien a ete enregistrer")
            else:
                messagebox.showerror("Erreur", "Aucun lien n'a ete marquer dans la zone de texte")
        else:
            if mode == "site":
                name = self.__entryNameSite.get()
                lien = self.__entryLienSite.get()
                if lien and name:
                    self.__fileUser.EcritureJSONDictionnaire("dictSite", name, lien)
                    nbSire = int(self.__fileUser.lectureJSON("nbSite"))
                    self.__fileUser.EcritureJSON("nbSite", str(nbSire + 1))
                    messagebox.showinfo("Lien", "Votre lien a ete enregistrer")
                else:
                    messagebox.showerror("Erreur", "Aucun lien ou nom n'a ete marquer dans les zones de textes")

    def __passEnd(self):
        self.__clearView()
        self.__arrTk.pack(self.__frameEnd)

    def __end(self):
        self.__windows.destroy()

    def __passWorkFolder(self):
        self.__clearView()
        self.__arrTk.pack(self.__frameWorkFolder)

    def __passVideoDownloadFolder(self):
        self.__clearView()
        self.__arrTk.pack(self.__framevideoDownloadFolder)

    def __addFolderWork(self):
        folder = filedialog.askdirectory(title="Choisir le dossier de travail")

        if folder:
            self.__fileUser.EcritureJSON("wordFolder", folder)
            showinfo("Dossier de travail", "Dossier de travail enregistrer")
        else:
            showerror("Dossier de travail", "Dossier de travail n'est enregistrer")

        self.__passVideoDownloadFolder()

    def __addFolderVideo(self):
        folder = filedialog.askdirectory(title="Choisir le dossier pour les video et les musiques")

        if folder:
            self.__fileUser.EcritureJSON("videoDownloadFolder", folder)
            showinfo("Dossier video et musique", "Dossier video et musique enregistrer")
        else:
            showerror("Dossier video et musique", "Dossier video et musique n'est enregistrer")

        self.__passEnd()