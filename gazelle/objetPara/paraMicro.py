from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingMicro :
    def __init__(self,cadre:Frame,SixConfig:jsonWork,textColor:str,color:str):
        #variable
        self.__config = SixConfig
        #declaration cadre
        self.__mainFrame = cadre
        self.__acceuilFrame = Frame(self.__mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.__acceuilFrame,text="Sons au declanchement du micro",bg=color,fg=textColor,font=("arial","15"))
        self.__btnOnOff = Button(self.__acceuilFrame,bg=color,fg=textColor,font=("arial","15"))
        #calcule Affichage
        largeur = self.__acceuilFrame.winfo_reqwidth()
        hauteur = self.__acceuilFrame.winfo_reqheight()
        self.setTextButton()
        #affichage
        labelTitre.place(x=((largeur-labelTitre.winfo_reqwidth())//2),y=0)
        self.__btnOnOff.place(relx=0.5,rely=0.5,anchor="center")

    def view(self):
        self.__mainFrame.pack(side="left")
        self.__acceuilFrame.place(x=0,y=0)

    def setTextButton(self):
        valeur = int(self.__config.lectureJSON("soundMicro"))
        if valeur == 1 :
            self.__btnOnOff.configure(text="OFF",command=self.commandOff)
        else :
            if valeur == 0 :
                self.__btnOnOff.configure(text="ON",command=self.commandOn)

    def commandOff(self):
        self.__config.EcritureJSON("soundMicro","0")
        self.setTextButton()
    
    def commandOn(self):
        self.__config.EcritureJSON("soundMicro","1")
        self.setTextButton()