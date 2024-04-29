from tkinter import *
from tkinter import messagebox
from librairy.travailJSON import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*

class ArreraLynx :
    def __init__(self,windows:Tk,fichierLynx:jsonWork,fichierUser:jsonWork,fichierNeuron:jsonWork):
        #objet
        self.__fichierLynx = fichierLynx
        self.__fileUser = fichierUser
        self.__fileNeuron = fichierNeuron
        self.__dectOS = OS()
        if self.__dectOS.osWindows()==True:
            self.__softWin = gestionSoftWindows(self.__fileNeuron.lectureJSON("emplacementSoftWindows"))
        #Variable 
        self.__windows = windows
        self.__varGenre = StringVar(windows)
        color = self.__fichierLynx.lectureJSON("color")
        textColor = self.__fichierLynx.lectureJSON("textColor")
        nomSoft = self.__fichierLynx.lectureJSON("nameSoft")
        iconLogiciel = PhotoImage(file=str(self.__fichierLynx.lectureJSON("iconSoft")))
        listGenre = self.__fichierLynx.lectureJSONList("listGenre")
        self.__userIN = False
        self.__genreIN = False
        #modification de la fenetre
        windows.title(nomSoft+": Premier demarage")
        windows.maxsize(700,500)
        windows.iconphoto(False,iconLogiciel)
        #cadre tkinter
        self.__frameAcceuil = Frame(windows,width=700,height=500,bg=color)
        self.__frameUserName = Frame(windows,width=700,height=500,bg=color)
        self.__frameUserGenre = Frame(windows,width=700,height=500,bg=color)
        self.__frameWeather = Frame(windows,width=700,height=500,bg=color)
        self.__frameAddWeather = Frame(windows,width=700,height=500,bg=color)
        self.__frameGPS = Frame(windows,width=700,height=500,bg=color)
        self.__frameAddGPS = Frame(windows,width=700,height=500,bg=color)
        self.__frameSoft = Frame(windows,width=700,height=500,bg=color)
        self.__frameSoftLinux = Frame(windows,width=700,height=500,bg=color)
        self.__frameWeb = Frame(windows,width=700,height=500,bg=color)
        self.__frameAddWeb = Frame(windows,width=700,height=500,bg=color)
        self.__frameEnd =  Frame(windows,width=700,height=500,bg=color)
        #widget 
        labelTitre = [
            Label(self.__frameAcceuil,bg=color,fg=textColor,font=("arial","20"),text="Programme de premier demarage de "+nomSoft),
            Label(self.__frameUserName,bg=color,fg=textColor,font=("arial","20"),text="Nom d'utilisateur"),
            Label(self.__frameUserGenre,bg=color,fg=textColor,font=("arial","20"),text="Genre d'utilisateur"),
            Label(self.__frameWeather,bg=color,fg=textColor,font=("arial","20"),text="Meteo"),
            Label(self.__frameGPS,bg=color,fg=textColor,font=("arial","20"),text="GPS"),
            Label(self.__frameSoft,bg=color,fg=textColor,font=("arial","20"),text="Logiciel"),
            Label(self.__frameWeb,bg=color,fg=textColor,font=("arial","20"),text="Site internet"),
            Label(self.__frameEnd,bg=color,fg=textColor,font=("arial","20"),text="Configuration terminer")
        ]
        btnSuivant = [
            Button(self.__frameAcceuil,bg=color,fg=textColor,font=("arial","15"),text="Commencer",command=self.__passUserName),#0
            Button(self.__frameUserName,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passUserGenre),#1
            Button(self.__frameUserGenre,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passMeteo),#2
            Button(self.__frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passGPS),#3
            Button(self.__frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passSoft),#4
            Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passWeb),#5
            Button(self.__frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self.__passEnd),#6
            Button(self.__frameEnd,bg=color,fg=textColor,font=("arial","15"),text="Commencer à utiliser "+nomSoft,command=self.__end)#7
        ]
        #frameUserName & frameUserGenre
        frameNameUser = Frame(self.__frameUserName,bg=color)
        frameGenreUser = Frame(self.__frameUserGenre,bg=color)
        labelIndicationUser = [
            Label(frameNameUser,bg=color,fg=textColor,font=("arial","15"),text="Nom :"),
            Label(frameGenreUser,bg=color,fg=textColor,font=("arial","15"),text="Genre :")
            ]
        self.entryName = Entry(frameNameUser,font=("arial","15"),borderwidth=2,relief="solid")
        menuGenre = OptionMenu(frameGenreUser,self.__varGenre,*listGenre)
        #frameWeather
        btnDomicile = Button(self.__frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile",command=lambda : self.__viewAddMeteo("domicile"))
        btnTravail = Button(self.__frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Lien de travail",command=lambda : self.__viewAddMeteo("travail"))
        btnVille = Button(self.__frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter une ville",command=lambda : self.__viewAddMeteo("ville"))
        #frameAddWeather
        self.__labelTitreAdd = [Label(self.__frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile"),
                          Label(self.__frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ville"),
                          Label(self.__frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Travail")]
        self.__entryVille = Entry(self.__frameAddWeather,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnAdd = Button(self.__frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameGPS
        btnAdresseDomicile = Button(self.__frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de domicile",command=lambda :self.__viewAddGPS("domicile"))
        btnAdresseTravail = Button(self.__frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de Travail",command=lambda :self.__viewAddGPS("travail"))
        #frameAddGPS
        self.__labelTitreGPSAdd = [
            Label(self.__frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de votre domicile"),
            Label(self.__frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de votre lieu de travail")
        ]
        self.__entryAdresse = Entry(self.__frameAddGPS,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnGPSAdd = Button(self.__frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameSoft
        btnWord = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Traitement de texte",command=lambda:self.__viewAddSoft("Ttexte"))
        btnExel = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Tableur",command=lambda:self.__viewAddSoft("tableur"))
        btnPresentation = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Presentation",command=lambda:self.__viewAddSoft("presentation"))
        btnBrowser = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Navigateur",command=lambda:self.__viewAddSoft("internet"))
        btnNote = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Note",command=lambda:self.__viewAddSoft("note"))
        btnMusic = Button(self.__frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Musique",command=lambda:self.__viewAddSoft("musique"))
        #frameAddSoft
        self.__labelTitreSoft = [
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de traitement de texte"),
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un tableur"),
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de presentation"),
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un navigateur internet"),
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de note"),
            Label(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de musique"),
        ]
        self.__entryCommandLinux = Entry(self.__frameSoftLinux,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnAddSoft = Button(self.__frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameWeb
        btnCloud = Button(self.__frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Stokage cloud ",command=lambda:self.__viewAddWeb("cloud"))
        btnSiteWeb= Button(self.__frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Racourcie site",command=lambda:self.__viewAddWeb("site"))
        #frameAddWeb
        self.__labelIndicationWeb = [Label(self.__frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Lien de votre stokage cloud"),
                              Label(self.__frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Racourcie d'un site")]
        self.__entryNameSite = Entry(self.__frameAddWeb,font=("arial","15"),borderwidth=2,relief="solid")
        self.__entryLienSite = Entry(self.__frameAddWeb,font=("arial","15"),borderwidth=2,relief="solid")
        self.__btnAddSite = Button(self.__frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        
        #calcule affichage
        largeurFrame = self.__frameAcceuil.winfo_reqwidth()
        hauteurFrame = self.__frameAcceuil.winfo_reqheight()
        
        #affichage
        #frameAcceuil
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnSuivant[0].place(relx=0.5,rely=0.5,anchor="center")
        #frameUserName
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        btnSuivant[1].place(x=((largeurFrame-btnSuivant[1].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[1].winfo_reqheight()))
        labelIndicationUser[0].pack(side="left")
        self.entryName.pack(side="left")
        frameNameUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameUserGenre
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        labelIndicationUser[1].pack(side="left")
        menuGenre.pack(side="left")
        btnSuivant[2].place(x=((largeurFrame-btnSuivant[2].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[2].winfo_reqheight()))
        frameGenreUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameWeather
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        btnDomicile.place(x=15,y=((hauteurFrame-btnDomicile.winfo_reqheight())//2))
        btnVille.place(relx=0.5,rely=0.5,anchor="center")
        btnTravail.place(x=((largeurFrame-btnTravail.winfo_reqwidth())-15),y=((hauteurFrame-btnTravail.winfo_reqheight())//2))
        btnSuivant[3].place(x=((largeurFrame-btnSuivant[3].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[3].winfo_reqheight()))
        #frameAddWeather
        self.__entryVille.place(relx=0.5,rely=0.5,anchor="center")
        self.__btnAdd.place(x=((largeurFrame-self.__btnAdd.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnAdd.winfo_reqheight()))
        #frameGPS
        labelTitre[4].place(x=((largeurFrame-labelTitre[4].winfo_reqwidth())//2),y=0)
        btnAdresseDomicile.place(x=15,y=((hauteurFrame-btnAdresseDomicile.winfo_reqheight())//2))
        btnAdresseTravail.place(x=(largeurFrame-btnAdresseTravail.winfo_reqwidth())-15,y=((hauteurFrame-btnAdresseTravail.winfo_reqheight())//2))
        btnSuivant[4].place(x=((largeurFrame-btnSuivant[4].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[4].winfo_reqheight()))
        #frameAddGPS
        self.__entryAdresse.place(relx=0.5,rely=0.5,anchor="center")
        self.__btnGPSAdd.place(x=((largeurFrame-self.__btnGPSAdd.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnGPSAdd.winfo_reqheight()))
        #frameSoft
        labelTitre[5].place(x=((largeurFrame-labelTitre[4].winfo_reqwidth())//2),y=0)
        btnWord.place(x=15,y=100)
        btnExel.place(x=(largeurFrame-btnExel.winfo_reqwidth()-15),y=100)
        btnPresentation.place(x=15,y=200)
        btnBrowser.place(x=(largeurFrame-btnBrowser.winfo_reqwidth()-15),y=200)
        btnNote.place(x=15,y=300)
        btnMusic.place(x=(largeurFrame-btnMusic.winfo_reqwidth()-15),y=300)
        btnSuivant[5].place(x=((largeurFrame-btnSuivant[5].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[4].winfo_reqheight()))
        #frameAddSoft
        if (self.__dectOS.osWindows() == False) and (self.__dectOS.osLinux()==True):
            self.__entryCommandLinux.place(relx=0.5,rely=0.5,anchor="center")
        self.__btnAddSoft.place(x=((largeurFrame-self.__btnAddSoft.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnAddSoft.winfo_reqheight()))
        #frameWeb
        labelTitre[6].place(x=((largeurFrame-labelTitre[6].winfo_reqwidth())//2),y=0)
        btnCloud.place(x=15,y=((hauteurFrame-btnCloud.winfo_reqheight())//2))
        btnSiteWeb.place(x=(largeurFrame-btnSiteWeb.winfo_reqwidth())-15,y=((hauteurFrame-btnSiteWeb.winfo_reqheight())//2))
        btnSuivant[6].place(x=((largeurFrame-btnSuivant[6].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[6].winfo_reqheight()))
        #frameAddWeb
        self.__btnAddSite.place(x=((largeurFrame-self.__btnAddSite.winfo_reqwidth())//2),y=(hauteurFrame-self.__btnAddSite.winfo_reqheight()))
        #frameEnd
        labelTitre[7].place(x=((largeurFrame-labelTitre[7].winfo_reqwidth())//2),y=0)
        btnSuivant[7].place(relx=0.5,rely=0.5,anchor="center")
       

    def confiCreate(self):
        if self.__userIN == True and self.__genreIN == True :
            return True
        else :
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
        self.__frameEnd.pack_forget()

    def active(self):
        self.__frameAcceuil.pack()

    def __passUserName(self):
        self.__clearView()
        self.__frameUserName.pack()
        
    def __passUserGenre(self):
        if self.entryName.get():
            self.__clearView()
            self.__frameUserGenre.pack()
            self.__fileUser.EcritureJSON("user",self.entryName.get())
            self.__userIN = True
        else :
            messagebox.showerror("Erreur","Veuillez entrer un nom d'utilisateur avant de continuer")
        
    
    def __activeFrameWeather(self):
        self.__clearView()
        self.__frameWeather.pack()

    def __passMeteo(self):
        if self.__varGenre.get():
            self.__activeFrameWeather()
            self.__fileUser.EcritureJSON("genre",self.__varGenre.get())
            self.__genreIN = True
        else :
           messagebox.showerror("Erreur","Veuillez entrer selectionner un genre avant de continuer") 
    
    def __viewAddMeteo(self,mode):
        self.__clearView()
        self.__entryVille.delete("0",END)
        self.__frameAddWeather.pack()
        self.__labelTitreAdd[0].place_forget()
        self.__labelTitreAdd[1].place_forget()
        self.__labelTitreAdd[2].place_forget()
        if mode == "domicile" :
            self.__labelTitreAdd[0].place(x=((self.__frameAcceuil.winfo_reqwidth()-self.__labelTitreAdd[0].winfo_reqwidth())//2),y=0)
            self.__btnAdd.configure(command=lambda : self.__addMeteo(mode))
        else :
            if mode == "travail" :
                self.__labelTitreAdd[2].place(x=((self.__frameAcceuil.winfo_reqwidth()-self.__labelTitreAdd[2].winfo_reqwidth())//2),y=0)
                self.__btnAdd.configure(command=lambda : self.__addMeteo(mode))
            else :
                if mode == "ville" :
                    self.__labelTitreAdd[1].place(x=((self.__frameAcceuil.winfo_reqwidth()-self.__labelTitreAdd[1].winfo_reqwidth())//2),y=0)
                    self.__btnAdd.configure(command=lambda : self.__addMeteo(mode))
        
    
    def __addMeteo(self,mode):
        valeur = self.__entryVille.get()
        if valeur:
            if mode == "domicile" :
                self.__fileUser.EcritureJSON("lieuDomicile",valeur)
            else :
                if mode == "travail" :
                    self.__fileUser.EcritureJSON("lieuTravail",valeur)  
                else :
                    if mode == "ville" :
                        self.__fileUser.EcritureJSONList("listVille",valeur) 
            self.__activeFrameWeather()
        else :
            self.__activeFrameWeather()
            messagebox.showerror("Erreur","Aucun ville n'a été marquer dans la zone de texte")
    
    def __passGPS(self):
        self.__clearView()
        self.__frameGPS.pack()
    
    def __viewAddGPS(self,mode:str):
        self.__clearView()
        self.__frameAddGPS.pack()
        self.__entryAdresse.delete("0",END)
        self.__labelTitreGPSAdd[0].place_forget()
        self.__labelTitreGPSAdd[1].place_forget()
        if mode == "domicile":
            self.__labelTitreGPSAdd[0].place(x=((self.__frameAcceuil.winfo_reqwidth()-self.__labelTitreGPSAdd[0].winfo_reqwidth())//2),y=0)
            self.__btnGPSAdd.configure(command=lambda : self.__addGPS(mode))
        else :
            if mode == "travail" :
                self.__labelTitreGPSAdd[1].place(x=((self.__frameAcceuil.winfo_reqwidth()-self.__labelTitreGPSAdd[0].winfo_reqwidth())//2),y=0)
                self.__btnGPSAdd.configure(command=lambda : self.__addGPS(mode))

    def __addGPS(self,mode:str):
        valeur = self.__entryAdresse.get()
        if valeur : 
            if mode == "domicile":
                self.__fileUser.EcritureJSON("adresseDomicile",valeur)
                self.__passGPS()
            else :
                if mode == "travail" :
                    self.__fileUser.EcritureJSON("adresseTravail",valeur)
                    self.__passGPS()
        else :
            self.__passGPS()
            messagebox.showerror("Erreur","Aucun adresse n'a été marquer dans la zone de texte")
   
    def __passSoft(self):
        if (self.__dectOS.osWindows() == True) :
            sortie = ""
            while not sortie :
                messagebox.showinfo("Infomation","Vous devait selectionner un dossier deja crée")
                sortie = self.__softWin.setEmplacementSoft()
                self.__fileNeuron.EcritureJSON("emplacementSoftWindows",sortie)
        self.__clearView()
        self.__frameSoft.pack()
    
    def __viewAddSoft(self,mode:str):
        if (self.__dectOS.osWindows() == True) :
            if mode == "Ttexte":
                self.__softWin.setName("Ttexte")
                self.__softWin.saveSoftware()
                self.__fileUser.EcritureJSON("wordWindows",self.__softWin.getName())
            else :
                if mode == "tableur":
                    self.__softWin.setName("tableur")
                    self.__softWin.saveSoftware()
                    self.__fileUser.EcritureJSON("exelWindows",self.__softWin.getName())
                else :
                    if mode == "presentation" :
                        self.__softWin.setName("presentation")
                        self.__softWin.saveSoftware()
                        self.__fileUser.EcritureJSON("diapoWindows",self.__softWin.getName())
                    else :
                        if mode == "internet" :
                            self.__softWin.setName("internet")
                            self.__softWin.saveSoftware()
                            self.__fileUser.EcritureJSON("browserWindows",self.__softWin.getName())
                        else :
                            if mode == "note" :
                                self.__softWin.setName("note")
                                self.__softWin.saveSoftware()
                                self.__fileUser.EcritureJSON("noteWindows",self.__softWin.getName())
                            else :
                                if mode == "musique" :
                                    self.__softWin.setName("musique")
                                    self.__softWin.saveSoftware()
                                    self.__fileUser.EcritureJSON("musicWindows",self.__softWin.getName())
        else :
            if (self.__dectOS.osLinux() == True) :
                self.__entryCommandLinux.delete("0",END)
                self.__clearView()
                self.__frameSoftLinux.pack()
                largeur = self.__frameAcceuil.winfo_reqwidth()
                for i in range(0,5):
                    self.__labelTitreSoft[i].place_forget()
                if mode == "Ttexte":
                    self.__labelTitreSoft[0].place(x=((largeur-self.__labelTitreSoft[0].winfo_reqwidth())//2),y=0)
                else :
                    if mode == "tableur":
                        self.__labelTitreSoft[1].place(x=((largeur-self.__labelTitreSoft[1].winfo_reqwidth())//2),y=0)
                    else :
                        if mode == "presentation" :
                            self.__labelTitreSoft[2].place(x=((largeur-self.__labelTitreSoft[2].winfo_reqwidth())//2),y=0)
                        else :
                            if mode == "internet" :
                                self.__labelTitreSoft[3].place(x=((largeur-self.__labelTitreSoft[3].winfo_reqwidth())//2),y=0)
                            else :
                                if mode == "note" :
                                    self.__labelTitreSoft[4].place(x=((largeur-self.__labelTitreSoft[4].winfo_reqwidth())//2),y=0)
                                else :
                                    if mode == "musique" :
                                        self.__labelTitreSoft[5].place(x=((largeur-self.__labelTitreSoft[5].winfo_reqwidth())//2),y=0)
                self.__btnAddSoft.configure(command=lambda : self.__addSoft(mode))
    
    def __addSoft(self,mode:str):
        command = self.__entryCommandLinux.get()
        if command :
            if mode == "Ttexte":
                self.__fileUser.EcritureJSON("wordLinux",command)
            else :
                if mode == "tableur":
                    self.__fileUser.EcritureJSON("exelLinux",command)
                else :
                    if mode == "presentation" :
                        self.__fileUser.EcritureJSON("diapoLinux",command)
                    else :
                        if mode == "internet" :
                            self.__fileUser.EcritureJSON("browserLinux",command)
                        else :
                            if mode == "note" :
                                self.__fileUser.EcritureJSON("noteLinux",command)
                            else :
                                if mode == "musique" :
                                    self.__fileUser.EcritureJSON("musicLinux",command)
            messagebox.showinfo("Enregistrement logiciel","Votre logiciel a ete enregister")
        else :
            messagebox.showerror("Erreur","Veuillez marquer une command pour l'enregistrer le logiciel")
        self.__clearView()
        self.__passSoft()
                    
    def __passWeb(self):
        self.__clearView()
        self.__frameWeb.pack()

    def __viewAddWeb(self,mode:str):
        self.__clearView()
        self.__frameAddWeb.pack()
        self.__entryLienSite.delete("0",END)
        self.__entryNameSite.delete("0",END)
        self.__entryLienSite.place_forget()
        self.__entryNameSite.place_forget()
        for i in range(0,1):
            self.__labelIndicationWeb[i].place_forget()
        largeurFrame = self.__frameAcceuil.winfo_reqwidth()
        if mode == "cloud":
            self.__labelIndicationWeb[0].place(x=((largeurFrame-self.__labelIndicationWeb[0].winfo_reqwidth())//2),y=0)
            self.__entryLienSite.place(rely=0.5,relx=0.5,anchor="center")
            self.__btnAddSite.configure(command=lambda:self.__addWeb("cloud"))
        else :
            if mode == "site":
                self.__labelIndicationWeb[1].place(x=((largeurFrame-self.__labelIndicationWeb[0].winfo_reqwidth())//2),y=0)
                self.__entryLienSite.place(x=((largeurFrame-self.__entryLienSite.winfo_reqwidth())//2),y=200)
                self.__entryNameSite.place(x=((largeurFrame-self.__entryNameSite.winfo_reqwidth())//2),y=100)
                self.__btnAddSite.configure(command=lambda:self.__addWeb("site"))
    
    def __addWeb(self,mode:str):
        self.__passWeb()
        if mode == "cloud":
            lien = self.__entryLienSite.get()
            if lien :
                self.__fileUser.EcritureJSON("lienCloud",lien)
                messagebox.showinfo("Lien","Votre lien a ete enregistrer")
            else :
                messagebox.showerror("Erreur","Aucun lien n'a ete marquer dans la zone de texte")
        else :
            if mode == "site":
                name = self.__entryNameSite.get()
                lien = self.__entryLienSite.get()
                if lien and name :
                    self.__fileUser.EcritureJSONDictionnaire("dictSite",name,lien)
                    nbSire = int(self.__fileUser.lectureJSON("nbSite"))
                    self.__fileUser.EcritureJSON("nbSite",str(nbSire+1))
                    messagebox.showinfo("Lien","Votre lien a ete enregistrer")
                else :
                    messagebox.showerror("Erreur","Aucun lien ou nom n'a ete marquer dans les zones de textes")
        

    def __passEnd(self):
        self.__clearView()
        self.__frameEnd.pack()
    
    def __end(self):
        self.__windows.destroy()