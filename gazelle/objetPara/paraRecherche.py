from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingRecherche :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str,liste:list):
        #varriable
        self.__configFile = config
        self.__listMoteur = liste
        self.__choixVar = StringVar(windows)
        #declaration cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.__acceuilFrame,text="Choisisser\nle moteur de recherche",bg=color,fg=textColor,font=("arial","20"))
        menuMoteur = OptionMenu(self.__acceuilFrame,self.__choixVar,*self.__listMoteur)
        btnValider = Button(self.__acceuilFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self._moteurRecherche)
        #calcule affichage
        largeurAcceuilFrame = self.__acceuilFrame.winfo_reqwidth()
        #Affichage 
        labelTitre.place(x=((largeurAcceuilFrame-labelTitre.winfo_reqwidth())//2),y=0)
        menuMoteur.place(relx=0.5,rely=0.5,anchor="center")
        btnValider.place(x=((largeurAcceuilFrame-btnValider.winfo_reqwidth())//2),y=(self.__acceuilFrame.winfo_reqheight()-btnValider.winfo_reqheight()))
        
    def view(self)->bool:
        self.__mainFrame.pack(side="left")
        self.__acceuilFrame.place(x=0,y=0)
        
    def writeMoteur(self,moteur:StringVar):
        valeur = moteur.get()
        self.__configFile.EcritureJSON("moteurRecherche",valeur)
        messagebox.showinfo("Moteur de recherche","Le moteur de chercheche a ete changer")
    
    def _moteurRecherche(self):
        self.writeMoteur(self.__choixVar)