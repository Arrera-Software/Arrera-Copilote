from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingUser :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,settingConfigFile:jsonWork,textColor:str,color:str):
        #varriable 
        self.__varGenre = StringVar(windows)
        self.__configFile = config
        self.__settingFile = settingConfigFile
        self.__listGenre = list(self.__settingFile.lectureJSONList("listGenre"))
        #declaration cadre
        self.__mainFrame = cadre
        self.__acceuilFrame =  Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__prenomFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        self.__genreFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = [
            Label(self.__acceuilFrame,text="Parametre Utilisateur",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__prenomFrame,text="Prenom",bg=color,fg=textColor,font=("arial","20")),
            Label(self.__genreFrame,text="Genre",bg=color,fg=textColor,font=("arial","20"))
            ]
        btnRetour = [
            Button(self.__prenomFrame,bg=color,fg=textColor,font=("arial","15"),text="Retour",command=self._backAcceuil),
            Button(self.__genreFrame,bg=color,fg=textColor,font=("arial","15"),text="Retour",command=self._backAcceuil)
        ]
        #acceuilFrame
        btnPrenom = Button(self.__acceuilFrame,bg=color,fg=textColor,font=("arial","15"),text="Nom de l'utilisateur",command=self.prenomView)
        btnGenre = Button(self.__acceuilFrame,bg=color,fg=textColor,font=("arial","15"),text="genre de l'utilisateur",command=self.genreView)
        #prenomFrame
        self.entryName = Entry(self.__prenomFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnValiderName = Button(self.__prenomFrame,bg=color,fg=textColor,font=("arial","15"),text="Valider",command=self.changePrenom)  
        #genreFrame
        menuGenre = OptionMenu(self.__genreFrame,self.__varGenre,*self.__listGenre)
        btnValiderGenre = Button(self.__genreFrame,bg=color,fg=textColor,font=("arial","15"),text="Valider",command=self.changeGenre)  
        #calcule affichage
        largeur = self.__acceuilFrame.winfo_reqwidth()
        hauteur = self.__acceuilFrame.winfo_reqheight()
        #affichage
        #acceuilFrame 
        labelTitre[0].place(x=((largeur-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnPrenom.place(x=((largeur-btnPrenom.winfo_reqwidth())//2),y=200)
        btnGenre.place(x=((largeur-btnGenre.winfo_reqwidth())//2),y=275)
        #prenomFrame
        labelTitre[1].place(x=((largeur-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.entryName.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderName.place(x=0,y=(hauteur-btnValiderName.winfo_reqheight()))
        btnRetour[0].place(x=(largeur-btnRetour[0].winfo_reqwidth()),y=(hauteur-btnRetour[0].winfo_reqheight()))
        #genreFrame
        labelTitre[2].place(x=((largeur-labelTitre[2].winfo_reqwidth())//2),y=0)
        menuGenre.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderGenre .place(x=0,y=(hauteur-btnValiderGenre.winfo_reqheight()))
        btnRetour[1].place(x=(largeur-btnRetour[1].winfo_reqwidth()),y=(hauteur-btnRetour[0].winfo_reqheight()))

    def _backAcceuil(self)->bool:
        self.__prenomFrame.place_forget()
        self.__genreFrame.place_forget()
        self.__acceuilFrame.place(x=0,y=0)
        return True

    
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def prenomView(self)->bool:
        self.__acceuilFrame.place_forget()
        self.__prenomFrame.place(x=0,y=0)
        return True
    
    def genreView(self)->bool:
        self.__acceuilFrame.place_forget()
        self.__genreFrame.place(x=0,y=0)
        return True

    def changePrenom(self)->bool:
        name = self.entryName.get()
        if name :
            self.__configFile.EcritureJSON("user",name)
            messagebox.showinfo("Changement de nom","Votre nom a été changer")
            self._backAcceuil()
            self.entryName.delete("0",END)
        else :
            messagebox.showerror("Erreur nom","Vous dever marquer \nun nom pour le changer")
            self._backAcceuil()
        return True
    
    def changeGenre(self)->bool:
        genre = self.__varGenre.get()
        if genre :
            self.__configFile.EcritureJSON("genre",genre)
            messagebox.showinfo("Changement de genre","Votre genre a été modifier")
            self._backAcceuil()
        else :
            messagebox.showerror("Erreur genre","Veuillez selectionner un genre")
            self._backAcceuil()