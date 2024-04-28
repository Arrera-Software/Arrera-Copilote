import holidays
from tkinter import *
from tkinter.messagebox import showinfo 
from tkcalendar import DateEntry
from ObjetsNetwork.gestion import *
from arreraSoftware.fonctionDate import *

class fncArreraCalendar :
    def __init__(self,fichierConfig:jsonWork,gestionnaire:gestionNetwork):
        self.__configNeuron = fichierConfig
        self.__gestionnaire = gestionnaire
        self.__objetDate = fncDate()
        self.__fichierEvenement = jsonWork(self.__gestionnaire.getValeurfichierUtilisateur("emplacementEvenenement"))
        name = self.__configNeuron.lectureJSON("name")
        icon = self.__configNeuron.lectureJSON("iconAssistant")
        color = self.__configNeuron.lectureJSON("interfaceColor")
        textColor = self.__configNeuron.lectureJSON("interfaceTextColor")
        self.__interfaceCalendar = ArreraCalendarAddSuppr(color,icon,textColor,name,self.__fichierEvenement,self.__objetDate)
        
    def addEvenemnt(self):
        self.__interfaceCalendar.interfaceAdd()
    
    def supprEvenement(self):
        self.__interfaceCalendar.interfaceSuppr()

    def checkEvenement(self):
        self.__objetDate.rafraichisement()
        listEvent = []
        dictionnaireEvenement = self.__fichierEvenement.dictJson()
        dateJour = str(self.__objetDate.annes() + "-" +  self.__objetDate.nbMois() + "-" + self.__objetDate.jour())
        nbEvent = 0
        nb = self.__fichierEvenement.compteurFlagJSON()
        if nb == 0 :
           return nbEvent , listEvent  
        for i in range(0,nb) :
            if dictionnaireEvenement[str(i)][0] == dateJour :
                nbEvent += 1 
                listEvent.append(dictionnaireEvenement[str(i)][1])
        
        return nbEvent , listEvent
            
            
class ArreraCalendarAddSuppr :
    def __init__(self,color:str,icon:str,textColor:str,name:str,fileEvenement:jsonWork,date:fncDate) :
        self.color = color
        self.icon = icon
        self.textColor = textColor
        self.name = name 
        self.fileEvenement = fileEvenement
        self.__objetDate = date
        
    
    def __fenetreTk(self):
        #fenetre tkinter
        self.__screen = Toplevel()
        self.__screen.title(self.name+" : Calendrier")
        self.__screen.iconphoto(False,PhotoImage(file=self.icon))
        self.__screen.maxsize(500,200)
        self.__screen.minsize(500,200)
        self.__screen.config(bg=self.color)
        #varriable
        self.__event = StringVar(self.__screen)
        #carde
        self.__cadreAdd = Frame(self.__screen,bg=self.color,height=200,width=500)
        self.__cadreSuppr = Frame(self.__screen,bg=self.color,height=200,width=500)
        #diferent widget
        #cadreAdd
        self.__labelAdd = Label(self.__cadreAdd,text="Ajout d'un événement",font=("arial",20),bg=self.color,fg=self.textColor)
        self.__labelDate = Label(self.__cadreAdd,text="Choisir date : ",font=("arial",20),bg=self.color,fg=self.textColor)
        self.__labelName = Label(self.__cadreAdd,text="Nom du rappel : ",font=("arial",20),bg=self.color,fg=self.textColor)
        self.__chooseDate = DateEntry(self.__cadreAdd, width=15, background='darkblue', foreground='white', borderwidth=2)
        self.__entryName = Entry(self.__cadreAdd,font=("arial",12),highlightthickness=2, highlightbackground="black")
        self.__btnValiderAdd = Button(self.__cadreAdd,text="Ajouter",font=("arial",20),bg=self.color,fg=self.textColor,command=self.__addEvent)
        #cadreSuppr
        self.__btnValiderSuppr = Button(self.__cadreSuppr,text="Supprimer",font=("arial",20),bg=self.color,fg=self.textColor,command=self.__supprEvent)
        #affichage
        #cadre add
        self.__labelAdd.place(x=0,y=0)
        self.__labelDate.place(x=0,y=55)
        self.__chooseDate.place(x=190,y=60)
        self.__labelName.place(x=0,y=105)
        self.__entryName.place(x=200,y=110)
        self.__btnValiderAdd.place(x=200,y=150)
        #cadreSuppr
        self.__btnValiderSuppr.place(x=200,y=150)
        

    def interfaceAdd(self):
        self.__fenetreTk()
        self.__cadreAdd.pack()
        
    def interfaceSuppr(self):
        self.__fenetreTk()
        self.__cadreSuppr.pack()
        dictEvenement = self.fileEvenement.dictJson()
        if len(dictEvenement) == 0 :
            showinfo("Avertisement","Vous pouvez supprimer d'evenement avant d'en ajouter")
        else :
            nbEvent = self.fileEvenement.compteurFlagJSON()
            listEvent = []
            for i in range(0,nbEvent) :
                listEvent.append(dictEvenement[str(i)][1])
            listMenu = OptionMenu(self.__cadreSuppr,self.__event,*listEvent)
            listMenu.place(relx=0.5,rely=0.5,anchor=CENTER)
            self.__event.set(listEvent[0])
        
    def __addEvent(self):
        self.__objetDate.rafraichisement()
        dateJour = str(self.__objetDate.annes() + "-" +  self.__objetDate.nbMois() + "-" + self.__objetDate.jour())
        dateIn = str(self.__chooseDate.get_date())
        if dateIn ==  dateJour :
            showinfo("Avertisement","Vous pouvez pas crée un événement a la date du jours")
        else :
            nom = self.__entryName.get()
            if nom == "" :
                showinfo("Avertisement","Vous crée un événement sans nom")
            else :
                nb = self.fileEvenement.compteurFlagJSON()
                self.fileEvenement.EcritureJSON(str(nb),[dateIn,nom])
                self.__entryName.delete(0,END)
                self.__chooseDate.set_date(datetime.date.today())
                showinfo("événement","Evénement enregistrer avec succes")
                
    def __supprEvent(self):
        nameEvent = self.__event.get()
        dictEvenement = self.fileEvenement.dictJson()
        for flag, valeurs in dictEvenement.items():
            deuxieme_valeur = valeurs[1]  # Deuxième valeur de la liste
            if deuxieme_valeur == nameEvent:
                break  
        self.fileEvenement.supprDictReorg(flag)
        showinfo("événement","Evénement supprimer")
        self.__screen.destroy()   