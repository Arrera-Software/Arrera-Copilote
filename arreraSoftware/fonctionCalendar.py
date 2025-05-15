import locale
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from ObjetsNetwork.gestion import *
from arreraSoftware.fonctionDate import *



class fncArreraAgenda :
    def __init__(self,fichierConfig:jsonWork,gest:gestionNetwork):
        self.__agendaFile = jsonWork(gest.getEmplacementFileAgenda())
        self.__mainColor = fichierConfig.lectureJSON("interfaceColor")
        self.__textColor = fichierConfig.lectureJSON("interfaceTextColor")
        self.__icon = fichierConfig.lectureJSON("iconAssistant")
        self.__nameAssistant = fichierConfig.lectureJSON("name")
        self.__objetDate = fncDate()
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    def __windows(self):
        self.__screen = Toplevel()
        self.__screen.title(self.__nameAssistant+" : Agenda")
        self.__screen.maxsize(600,700)
        self.__screen.minsize(600,700)
        self.__screen.configure(bg="white")
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        # Varriable de date
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        day1 = today + timedelta(days=2)
        day2 = today + timedelta(days=3)
        day3 = today + timedelta(days=4)
        # Variable choix event Suppr
        self.__choixSuppr = StringVar(self.__screen)
        # Frame Agenda
        frameYesterday = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frameToday = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg="green")
        frameTomorrow = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frameDay1 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frameDay2 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frameDay3 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        # Frame Management
        self.__frameAdd = Frame(self.__screen,width=600,height=350,bg=self.__mainColor)
        self.__frameSuppr = Frame(self.__screen,width=600,height=350,bg=self.__mainColor)
        self.__frameResumer = Frame(self.__screen,width=600,height=300,bg=self.__mainColor)
        self.__frameNavigation = Frame(self.__screen,width=600,height=50,bg=self.__mainColor)
        #Widget Frame Agenda
        labelYesterday = Label(frameYesterday,text=yesterday.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelToday = Label(frameToday,text=today.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg="green")
        labelTomorrow = Label(frameTomorrow,text=tomorrow.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay1 = Label(frameDay1,text=day1.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay2 =  Label(frameDay2,text=day2.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay3 = Label(frameDay3,text=day3.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        btnAddFrameDay = [Button(frameTomorrow,text="Ajouter",font=("Arial","13"),bg=self.__mainColor,
                         command=lambda:self.__windowsAdd(str(tomorrow.year)+"-"+str(tomorrow.month)+"-"+str(tomorrow.day))),
            Button(frameDay1,text="Ajouter",font=("Arial","13"),bg=self.__mainColor,
                         command=lambda:self.__windowsAdd(str(day1.year)+"-"+str(day1.month)+"-"+str(day1.day))),
            Button(frameDay2,text="Ajouter",font=("Arial","13"),bg=self.__mainColor,
                         command=lambda:self.__windowsAdd(str(day2.year)+"-"+str(day2.month)+"-"+str(day2.day))),
            Button(frameDay3,text="Ajouter",font=("Arial","13"),bg=self.__mainColor,
                         command=lambda:self.__windowsAdd(str(day3.year)+"-"+str(day3.month)+"-"+str(day3.day)))]
        btnResumerDay = [
            Button(frameToday,text="Resumer",font=("Arial","13"),bg=self.__mainColor,
                   command=lambda:self.__affichageResumer(str(today.year)+"-"+str(today.month)+"-"+str(today.day))),
            Button(frameTomorrow,text="Resumer",font=("Arial","13"),bg=self.__mainColor,
                   command=lambda:self.__affichageResumer(str(tomorrow.year)+"-"+str(tomorrow.month)+"-"+str(tomorrow.day))),
            Button(frameDay1,text="Resumer",font=("Arial","13"),bg=self.__mainColor,
                   command=lambda:self.__affichageResumer(str(day1.year)+"-"+str(day1.month)+"-"+str(day1.day))),
            Button(frameDay2,text="Resumer",font=("Arial","13"),bg=self.__mainColor,
                   command=lambda:self.__affichageResumer(str(day2.year)+"-"+str(day2.month)+"-"+str(day2.day))),
            Button(frameDay3,text="Resumer",font=("Arial","13"),bg=self.__mainColor,
                   command=lambda:self.__affichageResumer(str(day3.year)+"-"+str(day3.month)+"-"+str(day3.day)))]
        self.__labelResumerTomorrow = Label(frameTomorrow,text="a",font=("Arial","13"),bg=self.__mainColor)
        self.__labelResumerDay1 = Label(frameDay1,font=("Arial","13"),bg=self.__mainColor)
        self.__labelResumerDay2 = Label(frameDay2,font=("Arial","13"),bg=self.__mainColor)
        self.__labelResumerDay3 = Label(frameDay3,font=("Arial","13"),bg=self.__mainColor)
        # Widget Frame Management 
        # FrameAdd 
        labelAdd = Label(self.__frameAdd,text="Ajout d'un événement",font=("arial","20"),bg=self.__mainColor,fg=self.__textColor)
        labelDate = Label(self.__frameAdd,text="Choisir date : ",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        labelName = Label(self.__frameAdd,text="Nom du rappel : ",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        chooseDate = DateEntry(self.__frameAdd, width=15, background='darkblue', foreground='white', borderwidth=2)
        entryName = Entry(self.__frameAdd,font=("arial",12),highlightthickness=2, highlightbackground="black")
        btnValiderAdd = Button(self.__frameAdd,text="Ajouter",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor,
                               command=lambda:self.__addEvent(self.__formatageDateEntry(chooseDate),entryName))
        btnAnnulerAdd = Button(self.__frameAdd,text="Annuler",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor,
                               command=self.__showFrameResumer)
        # FrameSuppr
        labelSuppr = Label(self.__frameSuppr,text="Supprimer un événement",font=("arial","20"),
                           bg=self.__mainColor,fg=self.__textColor)
        btnValiderSuppr = Button(self.__frameSuppr,text="Supprimer",font=("arial","15"),
                                 bg=self.__mainColor,fg=self.__textColor,command=self.__supprEvent)
        btnAnnulerSuppr = Button(self.__frameSuppr,text="Annuler",font=("arial","15"),
                                 bg=self.__mainColor,fg=self.__textColor,command=self.__showFrameResumer)
        # frameNavigation
        btnNavigationAdd = Button(self.__frameNavigation,text="Ajouter",
                                  bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__showFrameAdd)
        btnNavigationSuppr = Button(self.__frameNavigation,text="Supprimer",
                                    bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__showFrameSuppr)
        # frameResumer
        self.__labelTitreResumer = Label(self.__frameResumer,
                                         bg=self.__mainColor,fg=self.__textColor,font=("arial","15"))
        self.__labelResumer = Label(self.__frameResumer,
                                    bg=self.__mainColor,fg=self.__textColor,font=("arial","15"))
        # Affichage Frame Agenda
        frameYesterday.place(x=0,y=0)
        frameToday.place(x=(frameYesterday.winfo_reqwidth()),y=0)
        frameTomorrow.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=0)
        frameDay1.place(x=0,y=(frameYesterday.winfo_reqheight()))
        frameDay2.place(x=(frameYesterday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        frameDay3.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        # Affichage Widget Frame Agenda
        labelYesterday.place(x=0,y=0)
        labelToday.place(x=0,y=0)
        labelTomorrow.place(x=0,y=0)
        labelDay1.place(x=0,y=0)
        labelDay2.place(x=0,y=0)
        labelDay3.place(x=0,y=0)
        self.__labelResumerTomorrow.place(relx=0.5, rely=0.5, anchor="center")
        self.__labelResumerDay1.place(relx=0.5, rely=0.5, anchor="center")
        self.__labelResumerDay2.place(relx=0.5, rely=0.5, anchor="center")
        self.__labelResumerDay3.place(relx=0.5, rely=0.5, anchor="center")
        btnAddFrameDay[0].place(relx=0, rely=1, anchor='sw')
        btnAddFrameDay[1].place(relx=0, rely=1, anchor='sw')
        btnAddFrameDay[2].place(relx=0, rely=1, anchor='sw')
        btnAddFrameDay[3].place(relx=0, rely=1, anchor='sw')
        btnResumerDay[0].place(relx=0.5, rely=0.5, anchor="center")
        btnResumerDay[1].place(relx=1, rely=1, anchor='se')
        btnResumerDay[2].place(relx=1, rely=1, anchor='se')
        btnResumerDay[3].place(relx=1, rely=1, anchor='se')
        btnResumerDay[4].place(relx=1, rely=1, anchor='se')
        # Affichage Frame Management
        # FrameAdd
        labelAdd.place(x=0,y=0)
        labelDate.place(x=0,y=55)
        chooseDate.place(x=190,y=60)
        labelName.place(x=0,y=105)
        entryName.place(x=200,y=110)
        btnValiderAdd.place(relx=0, rely=1, anchor='sw')
        btnAnnulerAdd.place(relx=1, rely=1, anchor='se')
        # FrameSuppr 
        labelSuppr.place(x=0,y=0)
        btnValiderSuppr.place(relx=0, rely=1, anchor='sw')
        btnAnnulerSuppr.place(relx=1, rely=1, anchor='se')
        # frameNavigation
        btnNavigationAdd.place(relx=0.0, rely=0.5, anchor="w")
        btnNavigationSuppr.place(relx=1.0, rely=0.5, anchor="e")
        # frameResumer
        self.__labelTitreResumer.place(x=0,y=0)
        self.__labelResumer.place(x=0,y=40)
    
    def __showFrameSuppr(self):
        dictEvenement = self.__agendaFile.getContenuJSON()
        if len(dictEvenement) == 0 :
            messagebox.showwarning("Avertisement","Vous pouvez supprimer d'evenement avant d'en ajouter")
        else :
            self.__frameAdd.place_forget()
            self.__frameResumer.place_forget()
            self.__frameNavigation.place_forget()
            nbEvent = self.__agendaFile.compteurFlagJSON()
            listEvent = []
            for i in range(0,nbEvent):
                listEvent.append(dictEvenement[str(i)][1])
            OptionMenu(self.__frameSuppr,self.__choixSuppr,*listEvent).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listEvent[0])
            self.__frameSuppr.place(x=0,y=self.__frameSuppr.winfo_reqheight())
        self.__setLabelResumer()
    
    def __showFrameAdd(self):
        self.__frameSuppr.place_forget()
        self.__frameResumer.place_forget()
        self.__frameNavigation.place_forget()
        self.__frameAdd.place(x=0,y=self.__frameAdd.winfo_reqheight())
        self.__setLabelResumer()
    
    def __showFrameResumer(self):
        today = datetime.now()
        self.__frameAdd.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameResumer.place(x=0,y=self.__frameAdd.winfo_reqheight())
        self.__frameNavigation.place(x=0,
                                     y=(self.__frameAdd.winfo_reqheight()+self.__frameResumer.winfo_reqheight()))
        self.__affichageResumer(str(today.year)+"-"+str(today.month)+"-"+str(today.day))
        self.__setLabelResumer()

    def activeAgenda(self):
        self.__windows()
        self.__showFrameResumer()

    def activeAddWindows(self):
        self.__windows()
        self.__showFrameAdd()
        
    
    def activeSupprWindows(self):
        self.__windows()
        self.__showFrameSuppr()
        
    def __addEvent(self,date:str,entry:Entry): 
        dateJour = str(self.__objetDate.annes() + "-" +  self.__objetDate.nbMois() + "-" + self.__objetDate.jour()) 
        name = entry.get()   
        if (date==dateJour):
            messagebox.showwarning("Avertisement",
                                   "Vous pouvez pas crée un événement a la date du jours. Cree un tache a la place")
        else :
            if(name==""):
                messagebox.showwarning("Avertisement",
                                       "Vous crée un événement sans nom")
            else :
                nb = self.__agendaFile.compteurFlagJSON()
                self.__agendaFile.EcritureJSON(str(nb),[date,name])
                entry.delete(0,END)
                messagebox.showinfo("événement",
                                    "Evénement enregistrer avec succes")
        self.__setLabelResumer()
    
    def __supprEvent(self):
        nameEvent = self.__choixSuppr.get()
        dictEvenement = self.__agendaFile.getContenuJSON()
        for flag, valeurs in dictEvenement.items():
            deuxieme_valeur = valeurs[1]  # Deuxième valeur de la liste
            if deuxieme_valeur == nameEvent:
                break  
        self.__agendaFile.supprDictReorg(flag)
        messagebox.showinfo("événement","Evénement supprimer")
        self.__showFrameResumer()
        self.__setLabelResumer()
    
    def __windowsAdd(self,date:str):
        screen = Toplevel()
        screen.maxsize(500,200)
        screen.minsize(500,200)
        screen.title("Ajout d'evenement")
        screen.iconphoto(False,PhotoImage(file="asset/icon/copilote/icon.png"))
        screen.configure(bg=self.__mainColor)
        Label(screen,text="Ajout d'evenement le "+date,font=("Arial","13"),bg=self.__mainColor).place(x=0,y=0)
        entryName = Entry(screen,font=("arial",12),highlightthickness=2, highlightbackground="black")
        entryName.place(relx=0.5, rely=0.5, anchor="center")
        Button(screen,text="Ajouter",font=("arial","15"),
               bg=self.__mainColor,fg=self.__textColor,
               command=lambda:
               self.__addEvent(date,entryName) and 
               screen.destroy()).place(relx=1, rely=1, anchor='se')
        Button(screen,text="Annuler",font=("arial","15"),
               bg=self.__mainColor,fg=self.__textColor,
               command=lambda:
               screen.destroy()).place(relx=0, rely=1, anchor='sw')
    
    def __formatageDateEntry(self,dateEntry:DateEntry):
        date_obj = dateEntry.get_date()  # Obtenir la date sous forme d'objet datetime.date
        formatted_date = f"{date_obj.year}-{date_obj.month}-{date_obj.day}"  # Formatter la date
        return formatted_date

    def __checkEvent(self,date:str):
        nbEvent = 0
        listEvent = []
        dictEvent = self.__agendaFile.getContenuJSON()
        nb = self.__agendaFile.compteurFlagJSON()
        if (nb==0):
            return 0 , ["",""]
        else :
            for i in range(0,nb):
                if(dictEvent[str(i)][0]==date):
                    nbEvent += 1 
                    listEvent.append(dictEvent[str(i)][1])
        return nbEvent,listEvent
    
    def __affichageResumer(self,date:str):
        self.__labelTitreResumer.configure(text="Resumer du "+date+" :")
        nb , listEvent = self.__checkEvent(date)
        self.__labelResumer.configure(text="")
        if (nb!=0):
            for i in range(0,nb) :
                texte = self.__labelResumer.cget("text")
                self.__labelResumer.configure(text=texte+listEvent[i]+"\n")
        else :
            self.__labelResumer.configure(text="")
    
    def __setLabelResumer(self):
        tomorrow = datetime.now() + timedelta(days=1)
        day1 = datetime.now() + timedelta(days=2)
        day2 = datetime.now() + timedelta(days=3)
        day3 = datetime.now() + timedelta(days=4)
        nbTomorrow,listEvent = self.__checkEvent(str(tomorrow.year)+"-"+str(tomorrow.month)+"-"+str(tomorrow.day))
        nbDay1,listEvent = self.__checkEvent(str(day1.year)+"-"+str(day1.month)+"-"+str(day1.day))
        nbDay2,listEvent = self.__checkEvent(str(day2.year)+"-"+str(day2.month)+"-"+str(day2.day))
        nbDay3,listEvent = self.__checkEvent(str(day3.year)+"-"+str(day3.month)+"-"+str(day3.day))
        if(nbTomorrow==0):
            self.__labelResumerTomorrow.configure(text="Aucun un événement a cette date",wraplength=130)
        else :
            if(nbTomorrow==1):
                self.__labelResumerTomorrow.configure(text="1 seul événement prévu pour cette date",wraplength=130)
            else :
                self.__labelTitreResumer.configure(text=str(nbTomorrow)+" événements prévu pour cette date",wraplength=130)
        
        if(nbDay1==0):
            self.__labelResumerDay1.configure(text="Aucun un événement a cette date",wraplength=130)
        else :
            if(nbDay1==1):
                self.__labelResumerDay1.configure(text="1 seul événement prévu pour cette date",wraplength=130)
            else :
                self.__labelResumerDay1.configure(text=str(nbDay1)+" événements prévu pour cette date",wraplength=130)
        
        if(nbDay2==0):
            self.__labelResumerDay2.configure(text="Aucun un événement a cette date",wraplength=130)
        else :
            if(nbDay2==1):
                self.__labelResumerDay2.configure(text="1 seul événement prévu pour cette date",wraplength=130)
            else :
                self.__labelResumerDay2.configure(text=str()+" événements prévu pour cette date",wraplength=130)
        
        if(nbDay3==0):
            self.__labelResumerDay3.configure(text="Aucun un événement a cette date",wraplength=130)
        else :
            if(nbDay3==1):
                self.__labelResumerDay3.configure(text="1 seul événement prévu pour cette date",wraplength=130)
            else :
                self.__labelResumerDay3.configure(text=str(nbDay3)+" événements prévu pour cette date",wraplength=130)

    def getEventToday(self):
        today = datetime.now()
        nb , listEvent = self.__checkEvent(str(today.year)+"-"+str(today.month)+"-"+str(today.day))
        return listEvent
    
    def getNbEventToday(self):
        today = datetime.now()
        nb , listEvent = self.__checkEvent(str(today.year)+"-"+str(today.month)+"-"+str(today.day))
        return nb