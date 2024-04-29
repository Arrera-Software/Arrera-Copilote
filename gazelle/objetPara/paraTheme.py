from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingTheme :
    def __init__(self,windows:Tk,cadre:Frame,listeTheme:list,configAssistant:jsonWork,textColor:str,color:str):
        #varriable
        self.__varTheme = StringVar(windows)
        self.__configAssistant = configAssistant
        self.__listTheme = listeTheme
        #cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.__acceuilFrame,text="Choix du theme",bg=color,fg=textColor,font=("arial","20"))
        self.menuTheme = OptionMenu(self.__acceuilFrame,self.__varTheme,*self.__listTheme)
        btnValider = Button(self.__acceuilFrame,text="Choix du theme",bg=color,fg=textColor,font=("arial","15"),command=self.setTheme)
        #Calcule affichage
        largeur = self.__acceuilFrame.winfo_reqwidth()
        hauteur = self.__acceuilFrame.winfo_reqheight()
        #affichage
        labelTitre.place(x=((largeur-labelTitre.winfo_reqwidth())//2),y=0)
        self.menuTheme.place(relx=0.5,rely=0.5,anchor="center")
        btnValider.place(x=((largeur-labelTitre.winfo_reqwidth())//2),y=(hauteur-labelTitre.winfo_reqheight()))
        
        
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self.__acceuilFrame.place(x=0,y=0)
        return True
    
    def setTheme(self)->bool:
        valeur = self.__varTheme.get()
        if valeur :
            self.__configAssistant.EcritureJSON("theme",valeur)
        else :
            messagebox.showerror("Erreur","Veuillez selectionner un theme")