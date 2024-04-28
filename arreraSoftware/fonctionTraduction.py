from translate import Translator
from librairy.speak import*
from librairy.travailJSON import*
from tkinter import messagebox
from tkinter import*

class fncArreraTrad :
    def __init__(self,ConfigNeuron:jsonWork):
        #objet
        self.__configNeuron = ConfigNeuron
        #varriable fenetre Tkinter
        self.__name = self.__configNeuron.lectureJSON("name")
        self.__icon = self.__configNeuron.lectureJSON("iconAssistant")
        self.__color = self.__configNeuron.lectureJSON("interfaceColor")
        self.__textColor = self.__configNeuron.lectureJSON("interfaceTextColor")
    
    def fenetreTrad(self,langInt:str,langOut:str):
        #objet
        self.__traducteur = Translator(to_lang=langInt,from_lang=langOut)
        #Creation fenetre Tkinter
        self.__fenetreTK = Toplevel()
        self.__fenetreTK.title(self.__name+" : Outil de traduction")
        self.__fenetreTK.maxsize(1050,550)
        self.__fenetreTK.minsize(1050,550)
        self.__fenetreTK.iconphoto(False,PhotoImage(file=self.__icon))
        self.__fenetreTK.config(bg=self.__color)
        #cadre
        self.__frameBTN = Frame(self.__fenetreTK,bg=self.__color)
        #widget
        self.__textInt = Text(self.__fenetreTK,width=50,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.__textOut = Text(self.__fenetreTK,width=50,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.__btnTrad = Button(self.__frameBTN,text="Traduire",bg="green",fg="white",font=("arial",15),width=450,command=self.traduire)
        self.__btnQuitter = Button(self.__frameBTN,text="Quitter",bg="red",fg="white",font=("arial",15),width=450,command=self.quitter)
        self.__btnClear = Button(self.__frameBTN,text="Supprimer",bg=self.__color,fg=self.__textColor,font=("arial",15),width=450,command=self.clearText)
        #affichage
        self.__textInt.pack(side="left")
        self.__textOut.pack(side="right")
        self.__frameBTN.place(relx=0.5,rely=0.5,anchor="center")
        self.__btnTrad.pack()
        self.__btnQuitter.pack()
        self.__btnClear.pack()

    def traduire(self):
        texte = self.__textInt.get("1.0",END).strip()
        if len(texte) == 0 :
            messagebox.showwarning("Attention", "Veuillez entrer une phase dans la la zone de texte de gauche")
        else :
            sortieTraducteur = self.__traducteur.translate(texte)
            self.__textOut.delete("1.0",END)
            self.__textOut.insert("1.0",sortieTraducteur)
    
    def clearText(self):
        self.__textOut.delete("1.0",END)
        self.__textInt.delete("1.0",END)
        
    def quitter(self):
        self.__fenetreTK.destroy()      
    
            
            
