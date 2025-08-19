from tkinter import*
from librairy.travailJSON import*
from tkinter import colorchooser
from librairy.asset_manage import resource_path

class CCHcolorSelector:
    def __init__(self,ConfigNeuron:jsonWork):
        self.__mainColor = ConfigNeuron.lectureJSON("interfaceColor")
        self.__mainTextColor = ConfigNeuron.lectureJSON("interfaceTextColor")
        self.__iconAssistant = resource_path(ConfigNeuron.lectureJSON("iconAssistant"))
        self.__name = ConfigNeuron.lectureJSON("name")

    def bootSelecteur(self):
        self.__screenColor = Toplevel()
        self.__screenColor.title(self.__name+" : Codehelp color selecteur")
        self.__screenColor.config(bg=self.__mainColor)
        self.__screenColor.iconphoto(False,PhotoImage(file=self.__iconAssistant))
        self.__screenColor.maxsize(800,500)
        self.__screenColor.minsize(800,500)
        #fonction
        #cadre
        cadreNoir = Frame(self.__screenColor,bg="black",width=325,height=325,border=100)
        self.__cadreColor = Frame(cadreNoir,bg="#ffffff",width=310,height=310)
        #label
        self.__labelIndicationCode = Label(self.__screenColor,text="Code HTML : #ffffff \nCode RGB : (255,255,255)",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),justify="left")     
        #declaration des bouton
        buttonSelection = Button(self.__screenColor,text="Selectionner la couleur",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15),command=self.__selecteur)
        self.__buttonCopiHTLM = Button(self.__screenColor,text="Copier le code HTML",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        self.__buttonCopiRGB = Button(self.__screenColor,text="Copier le code RGB",bg=self.__mainColor,fg=self.__mainTextColor,font=("arial",15))
        #affichage
        self.__cadreColor.place(relx=0.5, rely=0.5, anchor=CENTER)
        cadreNoir.pack(side="right")
        self.__labelIndicationCode.place(x=15,y=15)
        buttonSelection.place(x=15,y=135)
        self.__buttonCopiHTLM.place(x=15,y=235)
        self.__buttonCopiRGB.place(x=15,y=335)
        
    def __selecteur(self):
        self.__color = colorchooser.askcolor(title="Ryley : CodeHelp selecteur de couleur",color=self.__mainColor)
        self.__colorHTLM = str(self.__color[1])
        self.__colorRGB = str(self.__color[0])
        self.__cadreColor.config(bg=self.__colorHTLM)
        self.__buttonCopiHTLM.config(command=self.__copieHTLM)
        self.__buttonCopiRGB.config(command=self.__copieRGB)
        self.__labelIndicationCode.config(text="Code HTML : "+self.__colorHTLM+"\nCode RGB : "+self.__colorRGB)
    
    def __copieHTLM(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorHTLM)
    
    def __copieRGB(self):
        self.__screenColor.clipboard_clear()
        self.__screenColor.clipboard_append(self.__colorRGB)