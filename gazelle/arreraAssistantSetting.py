from tkinter import *
from librairy.travailJSON import *
from gazelle.objetPara.paraUser import*
from gazelle.objetPara.paraMeteo import*
from gazelle.objetPara.paraGPS import*
from gazelle.objetPara.paraRecherche import *
from gazelle.objetPara.paraSoftware import*
from gazelle.objetPara.paraInternet import *
from gazelle.objetPara.paraTheme import*
from gazelle.objetPara.paraMicro import *

class ArreraSettingAssistant :
    def __init__(self,configSettingFile:str,configFile:str,configAssistant:str,fichierConfigUser:str):
        self.__changeColor = bool 
        self.__controleMicro = bool
        self.__icon = bool 
        self.__fileIcon = str
        self.__fnc = None
        #overture des fichier
        self.__settingFile = jsonWork(configSettingFile)
        self.__fileNeuronConfig = jsonWork(configFile)
        self.__assistantFile = jsonWork(configAssistant)
        self.__fileUser = jsonWork(fichierConfigUser)
        #Recuperarton donner
        if self.__settingFile.lectureJSON("colorInterface") == "1" :
            self.__changeColor =  True 
            self.__listTheme = self.__settingFile.lectureJSONList("listeTheme")
        else :
            self.__changeColor = False
        if self.__settingFile.lectureJSON("setIcon") == "1" : 
            self.__icon = True
        else :
            self.__icon = False
        if self.__settingFile.lectureJSON("gestionMicro") == "1" :
            self.__controleMicro = True
        else :
            self.__controleMicro = False
        #fichier fileconfig 
        self.__icon = self.__fileNeuronConfig.lectureJSON("iconAssistant")
        self.__nameAssistant = self.__fileNeuronConfig.lectureJSON("name")
        if self.__icon == True :
            self.__fileIcon = self.__assistantFile.lectureJSON("iconAssistant")
            
    def windows(self,windows:Toplevel,mode:str) ->bool :
        # Recuperation de la couleur
        if (mode == "light" ) :
            self.__colorPrimaire = self.__settingFile.lectureJSON("colorLight1")
            self.__colorSecondaire = self.__settingFile.lectureJSON("colorLight2")
            self.__textColorPrimaire = self.__settingFile.lectureJSON("textColorLight1")
            self.__textColorSecondaire = self.__settingFile.lectureJSON("textColorLight2")
        else :
            self.__colorPrimaire = self.__settingFile.lectureJSON("colorDark1")
            self.__colorSecondaire = self.__settingFile.lectureJSON("colorDark2")
            self.__textColorPrimaire = self.__settingFile.lectureJSON("textColorDark1")
            self.__textColorSecondaire = self.__settingFile.lectureJSON("textColorDark2")
        #variable
        xlabel2 = int 
        yBTNQuitter = int 
        listMoteur = ["Duckduckgo","google","bing","brave","ecosia","qwant"]
        self.__varRecherche = StringVar(windows)
        self.__varTheme = StringVar(windows)
        #widget
        #Cadre
        self.__cadreMenu = Frame(windows,width=150,height=600,bg=self.__colorSecondaire)
        self.__cadreAcceuil = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreUser = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreMeteo = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreGPS = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreRecherche = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreSoft = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreInternet = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreTheme = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        self.__cadreMicro = Frame(windows,width=350,height=600,bg=self.__colorPrimaire)
        #initilisation objet para
        self.__paraUser = SettingUser(windows,self.__cadreUser,self.__fileUser,self.__settingFile,self.__textColorPrimaire,self.__colorPrimaire)
        self.__paraMeteo = SettingMeteo(windows,self.__cadreMeteo,self.__fileUser,self.__textColorPrimaire,self.__colorPrimaire)
        self.__paraGPS = SettingGPS(windows,self.__cadreGPS,self.__fileUser,self.__textColorPrimaire,self.__colorPrimaire)
        self.__paraRecherche = SettingRecherche(windows,self.__cadreRecherche,self.__fileUser,self.__textColorPrimaire,self.__colorPrimaire,listMoteur)
        self.__paraSoftware = SettingSoftware(windows,self.__cadreSoft,self.__fileUser,self.__settingFile, self.__fileNeuronConfig,self.__textColorPrimaire,self.__colorPrimaire)
        self.__paraInternet = SettingInternet(windows,self.__cadreInternet,self.__fileUser,self.__textColorPrimaire,self.__colorPrimaire)
        if self.__changeColor == True:
            self.__paraTheme = SettingTheme(windows,self.__cadreTheme,self.__listTheme,self.__assistantFile,self.__textColorPrimaire,self.__colorPrimaire)
        if self.__controleMicro == True :
            self.__paraMicro = SettingMicro(self.__cadreMicro,self.__assistantFile,self.__textColorPrimaire,self.__colorPrimaire)
        #cadre interne a l'acceuil
        cadresPresentations = [
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.__cadreAcceuil,width=175,height=200,bg=self.__colorPrimaire,borderwidth=1, relief="solid")]
        #Label
        labelTitreMenu = Label(self.__cadreMenu,text="Menu",font=("arial","20"),bg=self.__colorSecondaire,fg=self.__textColorSecondaire)
        labelcadresPresentations = [
            Label(cadresPresentations[0],text="Gestion recherche",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire),
            Label(cadresPresentations[1],text="Gestion meteo",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire),
            Label(cadresPresentations[2],text="Gestion GPS",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire),
            Label(cadresPresentations[3],text="Gestion software",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire),
            Label(cadresPresentations[4],text="Gestion Site internet",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire),
            Label(cadresPresentations[5],text="Gestion theme",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire)]
        if self.__changeColor == False :
            labelcadresPresentations[5].configure(text="Cette fonction\nn'est pas\ndisponible sur\ncette assistant")
        #cadresPresentations
        #0
        menuRecherche1 = OptionMenu(cadresPresentations[0],self.__varRecherche,*listMoteur)
        btnValiderMoteur1 = Button(cadresPresentations[0],text="Valider",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.rechercheChange)
        #1
        btnMeteo1 = Button(cadresPresentations[1],text="Ajouter\nune ville",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.meteoViewAdd)
        #2
        btnGPSHome = Button(cadresPresentations[2],text="Adresse\nde domicile",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.gpsViewDomicile)
        btnGPSWork = Button(cadresPresentations[2],text="Adresse\nde travail",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.gpsViewWork)
        #3
        btnSoftware1 = Button(cadresPresentations[3],text="Ajouter\nun logiciel",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.softwareAddView)
        #4
        buttonAddSite = Button(cadresPresentations[4],text="Ajouter",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.internetViewAdd)
        buttonSupprSite = Button(cadresPresentations[4],text="Supprimer",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.internetViewSuppr)
        #5
        if self.__changeColor == True:
            menuTheme1 = OptionMenu(cadresPresentations[5],self.__varTheme,*self.__listTheme)
            btnValiderTheme1 = Button(cadresPresentations[5],text="Valider",font=("arial","13"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,command=self.setThemeAcceuil)
        #bouton
        #cadre menu
        boutonMenu1 = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Acceuil",command=lambda : self.mainView())
        boutonMenu2 = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Utilisateur",command=lambda :self.userView())
        boutonMenu3 = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Meteo",command=lambda : self.meteoView())
        boutonMenu4=Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="GPS",command=lambda :self.gpsView())
        boutonMenu5=Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Recherche",command=lambda :self.rechercheView())
        boutonMenu6=Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Software",command=lambda :self.softwareView())
        boutonMenu7 = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Internet",command=lambda :self.internetView())
        boutonMenu8=Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Theme",command=lambda :self.themeView())
        boutonMenu9  = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Micro",command=lambda:self.microView())
        boutonQuitter = Button(self.__cadreMenu,font=("arial","15"),bg=self.__colorPrimaire,fg=self.__textColorPrimaire,text="Quitter",command=lambda :self.quittePara())
        #formatage de la fenetre
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.title(self.__nameAssistant+": Parametre")
        if self.__icon == True :
            windows.iconphoto(False,PhotoImage(file=self.__fileIcon))
        #Calcule position
        xlabel2 = int(self.__cadreMenu.winfo_width()/2)
        xBoutonMenu = xlabel2 + 5
        yBTNQuitter = int(self.__cadreMenu.winfo_reqheight()-boutonQuitter.winfo_reqheight())
        #Cadre acceuil
        cadresPresentations[0].place(x=0,y=0)
        cadresPresentations[1].place(x=180,y=0)
        cadresPresentations[2].place(x=0,y=200)
        cadresPresentations[3].place(x=180,y=200)
        cadresPresentations[4].place(x=0,y=400)
        cadresPresentations[5].place(x=180,y=400)
        #Affichage des cadre composant du cadre acceuil
        labelcadresPresentations[0].place(x=0,y=0)
        menuRecherche1.place(relx=0.5,y=(labelcadresPresentations[0].winfo_reqheight()+45), anchor="center")
        btnValiderMoteur1.place(relx=0.5, rely=1.0, anchor="s")
        labelcadresPresentations[1].place(x=0,y=0)
        btnMeteo1.place(relx=0.5, rely=0.5, anchor="center")
        labelcadresPresentations[2].place(x=0,y=0)
        btnGPSHome.place(relx=0.5, rely=1.0, anchor="s")
        btnGPSWork.place(relx=0.5,y=(labelcadresPresentations[2].winfo_reqheight()+45), anchor="center")
        labelcadresPresentations[3].place(x=0,y=0)
        btnSoftware1.place(relx=0.5, rely=0.5, anchor="center")
        labelcadresPresentations[4].place(x=0,y=0)
        buttonSupprSite.place(relx=0.5, rely=0.5, anchor="center")
        buttonAddSite.place(relx=0.5,y=(labelcadresPresentations[4].winfo_reqheight()+45), anchor="s")
        
        if self.__changeColor == True :   
            labelcadresPresentations[5].place(x=0,y=0)
            menuTheme1.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
            btnValiderTheme1.place(relx=0.5, rely=1.0, anchor="s")
        else :
            labelcadresPresentations[5].place(relx=0.5, rely=0.5, anchor="center")
        #Affichage cadre menu 
        labelTitreMenu.place(x=xBoutonMenu,y=0)
        boutonMenu1.place(x=xBoutonMenu,y=50)
        boutonMenu2.place(x=xBoutonMenu,y=100)
        boutonMenu3.place(x=xBoutonMenu,y=150)
        boutonMenu4.place(x=xBoutonMenu,y=200)
        boutonMenu5.place(x=xBoutonMenu,y=250)
        boutonMenu6.place(x=xBoutonMenu,y=300)
        boutonMenu7.place(x=xBoutonMenu,y=350)
        if self.__changeColor == True :
            boutonMenu8.place(x=xBoutonMenu,y=400)
        if self.__controleMicro == True :
            if self.__changeColor == False :
                boutonMenu9.place(x=xBoutonMenu,y=400)
            else :
                boutonMenu9.place(x=xBoutonMenu,y=450)
        boutonQuitter.place(x=xBoutonMenu,y=yBTNQuitter)
        #Affichage cadre principal
        self.__cadreMenu.pack(side="left")
        return True 
    
    def _unView(self):
        self.__cadreAcceuil.pack_forget()
        self.__cadreUser.pack_forget()
        self.__cadreMeteo.pack_forget()  
        self.__cadreGPS.pack_forget()
        self.__cadreRecherche.pack_forget()
        self.__cadreSoft.pack_forget()
        self.__cadreInternet.pack_forget()
        self.__cadreTheme.pack_forget()
        
              
    def mainView(self) -> bool :
        self._unView()
        self.__cadreAcceuil.pack(side="left")
        self.__cadreAcceuil.update()
        return True 
    
    def userView(self)->bool:
        self._unView()
        self.__paraUser.view()
        self.__cadreUser.update()
        return True
    
    def meteoView(self) -> bool : 
        self._unView()
        self.__paraMeteo.view()
        self.__cadreMeteo.update()
        return True 

    def meteoViewAdd(self)->bool:
        self._unView()
        self.__paraMeteo.view()
        self.__paraMeteo.addView()
        self.__cadreMeteo.update()
        return True
    
    def gpsView(self)->bool:
        self._unView()
        self.__paraGPS.view()
        self.__cadreGPS.update()
        return True 
    
    def gpsViewDomicile(self)->bool:
        self._unView()
        self.__paraGPS.view()
        self.__paraGPS.domicileView()
        return True

    def gpsViewWork(self)->bool:
        self._unView()
        self.__paraGPS.view()
        self.__paraGPS.workView()
        return True
    
    def rechercheView(self)->bool  :
        self._unView()
        self.__paraRecherche.view()
        return True 

    def rechercheChange(self)->bool:
        self.__paraRecherche.writeMoteur(self.__varRecherche)
        return True
    
    def softwareView(self)->bool  :
        self._unView()
        self.__paraSoftware.view()
        return True 
    
    def softwareAddView(self)->bool:
        self._unView()
        self.__paraSoftware.view()
        self.__paraSoftware.addView()
        return True
    
    def internetView(self)->bool :
        self._unView()
        self.__paraInternet.view()
        return True
    
    def internetViewAdd(self)->bool  :
        self._unView()
        self.__paraInternet.view()
        self.__paraInternet.addView()
        return True 
    
    def internetViewSuppr(self)->bool  :
        self._unView()
        self.__paraInternet.view()
        self.__paraInternet.supprView()
        return True 
    
    def themeView(self)->bool  :
        if self.__changeColor == True :
            self._unView()
            self.__paraTheme.view()
            return True 
        else :
            return False
    
    def microView(self)->bool:
        if self.__controleMicro == True :
            self._unView()
            self.__paraMicro.view()
            return True
        else :
            return False
        
    def setThemeAcceuil(self):
        valeur = self.__varTheme.get()
        if valeur :
            self.__assistantFile.EcritureJSON("theme",valeur)
        else :
            messagebox.showerror("Erreur","Veuillez selectionner un theme")

    def passageFonctionQuitter(self,fonctionQuitter):
        self.__fnc = fonctionQuitter
    
    def quittePara(self)->bool :
        self.__cadreAcceuil.destroy()
        self.__cadreUser.destroy()
        self.__cadreMeteo.destroy()
        self.__cadreMenu.destroy()
        self.__cadreGPS.destroy()
        self.__cadreRecherche.destroy()
        self.__cadreSoft.destroy()
        self.__cadreTheme.destroy()
        self.__fnc()    
        return True 