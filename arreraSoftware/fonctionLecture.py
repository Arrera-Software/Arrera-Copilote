from tkinter import *
from librairy.travailJSON import *
from librairy.speak import*
from librairy.dectectionOS import*
import threading as th

class fncLecture :
    def __init__(self,ConfigNeuron:jsonWork,detecteurSys:OS):
        #initilation objet
        self.__configNeuron = ConfigNeuron
        self.__name = self.__configNeuron.lectureJSON("name")
        self.__icon = self.__configNeuron.lectureJSON("iconAssistant")
        self.__lang = ""
        self.__langSet = 0
        self.__thSpeak = None
        self.__color = self.__configNeuron.lectureJSON("interfaceColor")
        self.__windowsOS = detecteurSys.osWindows()
        self.__linuxOS = detecteurSys.osLinux()
        
    def fenetreLecture(self):
        #initilisation et configuration fenetre tkinter 
        self.__screen = Toplevel()
        self.__screen.title(self.__name+" : lecture ")
        if self.__windowsOS == True :
            self.__screen.minsize(600,500)
            self.__screen.maxsize(600,500)
        else :
            if self.__linuxOS == True:
                self.__screen.minsize(600,550)
                self.__screen.maxsize(600,550)
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        self.__screen.config(bg=self.__color)
        #varriable
        listeLang = ["en","fr","zh-CN","zh-TW","pt","es"]
        self.__varLang = StringVar(self.__screen)
        #Creation et configuration d'un menu
        self.__menuTop = Menu(self.__screen)
        self.__menuTop.add_command(label="Langue de lecture",command=self.changementLang)
        #creation widget
        self.__entryLect = Text(self.__screen,width=70,highlightthickness=2, highlightbackground="black",font=("Arial", 12))
        self.__boutonValider  = Button(self.__screen,text="Valider",bg="green",fg="white",font=("arial",15),width=70,command=self.lecture)
        self.__menuDeroulant = OptionMenu(self.__screen,self.__varLang,*listeLang)
        #Affichage
        self.__entryLect.pack()
        self.__boutonValider.pack(side="bottom")
        #fin de la fenetre
        self.__screen.config(menu=self.__menuTop)
    
    def retourAcceuil(self):
        self.__menuTop.entryconfigure("Retour Acceuil",label="Langue de lecture",command=self.changementLang)
        self.__menuDeroulant.place_forget()
        self.__boutonValider.configure(command=self.lecture)
        self.__entryLect.pack()

    def changementLang(self):
        self.__menuTop.entryconfigure("Langue de lecture",label="Retour Acceuil",command=self.retourAcceuil)
        self.__entryLect.pack_forget()
        self.__boutonValider.configure(command=self.setlang)
        self.__menuDeroulant.place(relx=0.5,rely=0.5,anchor="center")
    
    def setlang(self):
        self.__lang = self.__varLang.get()
        self.__langSet =  1
        self.retourAcceuil()
    
    def lecture(self):
        texte = self.__entryLect.get("1.0",END)
        if self.__langSet == 0 :
            objSpeak = Speaking(self.__configNeuron.lectureJSON("lang"))

        else :
            objSpeak = Speaking(self.__lang)
        self.__thSpeak = th.Thread(target=objSpeak.speak,args=(texte,))
        self.__thSpeak.start()
        self.__screen.after(1000,self.__actualiser)

    def __actualiser(self):
        if (self.__thSpeak.is_alive()==True):
            self.__entryLect.config(state="disabled")
            self.__screen.after(1000,self.__actualiser)
            self.__boutonValider.pack_forget()
        else :
            self.__entryLect.config(state="normal")
            self.__boutonValider.pack(side="bottom")
            self.__entryLect.delete("1.0",END)
            del self.__thSpeak
            self.__thSpeak = None