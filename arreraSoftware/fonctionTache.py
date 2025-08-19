from tkinter import*
from tkinter.messagebox import *
from ObjetsNetwork.gestion import *
from tkcalendar import DateEntry
from arreraSoftware.fonctionDate import*
from librairy.asset_manage import resource_path

class fncArreraTache :
    def __init__(self,fncDate:fncDate,fichierConfig:jsonWork,taskFile:str,projet:bool=False,nameProjet:str=""):
        self.__taskFile = jsonWork(taskFile)
        self.__mainColor = fichierConfig.lectureJSON("interfaceColor")
        self.__textColor = fichierConfig.lectureJSON("interfaceTextColor")
        self.__icon = resource_path(fichierConfig.lectureJSON("iconAssistant"))
        self.__nameAssistant = fichierConfig.lectureJSON("name")
        self.__objDate = fncDate
        if projet == True :
            self.__title = self.__nameAssistant + " : taches de " + nameProjet
        else :
            self.__title = self.__nameAssistant + " : taches personnel"

    def __windows(self):
        screen = Toplevel()
        screen.minsize(500,500)
        screen.maxsize(500,500)
        screen.configure(bg=self.__mainColor)
        screen.title(self.__title)
        screen.iconphoto(False,PhotoImage(file=self.__icon))
        # Varriable 
        self.__choixSuppr = StringVar(screen)
        tomorrow = datetime.today() + timedelta(days=1)
        # Frame
        self.__frameTask = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameAdd = [Frame(screen,width=500,height=450,bg=self.__mainColor),
                           Frame(screen,width=500,height=450,bg=self.__mainColor),
                           Frame(screen,width=500,height=450,bg=self.__mainColor)]
        self.__frameTaskInfo = Frame(screen,width=500,height=500,bg=self.__mainColor)
        self.__frameSuppr = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameCheck = Frame(screen,width=500,height=450,bg=self.__mainColor)
        self.__frameNavigation = Frame(screen,width=500,height=50,bg=self.__mainColor)
        self.__frameShowTache = [Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor),
                               Frame(self.__frameTask,width=165,height=210,borderwidth=2, relief="solid",bg=self.__mainColor)]
        self.__frameChangeDateInfo = Frame(screen,width=500,height=500,bg=self.__mainColor)
        # Widget FrameNavigation
        btnAddNav = Button(self.__frameNavigation,text="Ajouter",font=("arial","15"),
                           fg=self.__textColor,bg=self.__mainColor,command=self.__showAddFrame)
        btnSupprNav = Button(self.__frameNavigation,text="Supprimer",font=("arial","15"),
                             fg=self.__textColor,bg=self.__mainColor,command=self.__showSupprFrame)
        btnCheckNav = Button(self.__frameNavigation,text="Finir un tache",font=("arial","15"),
                             fg=self.__textColor,bg=self.__mainColor,command=self.__showCheckFrame)
        # Widget frameTask
        labelTitreTask = Label(self.__frameTask,text=self.__nameAssistant+" tache",font=("arial","15","bold"),
                               fg=self.__textColor,bg=self.__mainColor)
        
        # Widget framAdd
        labelTitreAdd = [Label(self.__frameAdd[0],text="Ajouter une tache :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                         Label(self.__frameAdd[1],text="Définir la date de fin :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                         Label(self.__frameAdd[2],text="Ajouter une description a la tache :",
                               font=("arial","15"),fg=self.__textColor,bg=self.__mainColor)]
        
        self.__nameTaskEntry =  Entry(self.__frameAdd[0],font=("arial",15),highlightthickness=2, highlightbackground="black")
        
        self.__btnValiderAdd = [Button(self.__frameAdd[0],text="Ajouter",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor,command=self.__addEvent),
                         Button(self.__frameAdd[1],text="Valider",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor),
                         Button(self.__frameAdd[2],text="Valider",font=("arial","15"),
                                fg=self.__textColor,bg=self.__mainColor)]
        
        self.__chooseDate = DateEntry(self.__frameAdd[1], width=15, background=self.__mainColor, 
                               foreground=self.__textColor, borderwidth=2,year=tomorrow.year, 
                               month=tomorrow.month, day=tomorrow.day)
        
        btnAnnulerAdd = Button(self.__frameAdd[0],text="Annuler",font=("arial","15"),
                               fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        
        self.__descriptionEntryTask =  Entry(self.__frameAdd[2],font=("arial",15),highlightthickness=2, highlightbackground="black")
        # Widget frameSuppr
        labelTitreSuppr = Label(self.__frameSuppr,text="Suprimmer une tache :",font=("arial","15","bold"),
                                fg=self.__textColor,bg=self.__mainColor)
        btnValiderSuppr = Button(self.__frameSuppr,text="Supprimer",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__supprEvent)
        btnAnnulerSuppr = Button(self.__frameSuppr,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Widget frameCheck
        labelTitreCheck = Label(self.__frameCheck,text="Finir une tache :",font=("arial","15","bold"),
                                fg=self.__textColor,bg=self.__mainColor)
        btnValiderCheck = Button(self.__frameCheck,text="Finir",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__checkEvent)
        btnAnnulerCheck = Button(self.__frameCheck,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__showTaskFrame)
        # Widget Frame Show Task 
        self.__labelNameShowTask = [Label(self.__frameShowTache[0],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor),
                                    Label(self.__frameShowTache[1],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor),
                                    Label(self.__frameShowTache[2],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor),
                                    Label(self.__frameShowTache[3],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor),
                                    Label(self.__frameShowTache[4],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor),
                                    Label(self.__frameShowTache[5],font=("arial","15"),
                                          fg=self.__textColor,bg=self.__mainColor)]
        self.__btnInfoShowTask = [Button(self.__frameShowTache[0],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                                  Button(self.__frameShowTache[1],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                                  Button(self.__frameShowTache[2],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                                  Button(self.__frameShowTache[3],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                                  Button(self.__frameShowTache[4],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor),
                                  Button(self.__frameShowTache[5],text="Plus d'info",
                                         font=("arial","15"),fg=self.__textColor,bg=self.__mainColor)]
        # Widget frame Task Info
        self.__labelTaskInfoName = Label(self.__frameTaskInfo,font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,justify="left",wraplength=450)
        
        self.__labelTaskInfoDate = Label(self.__frameTaskInfo,font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,justify="left",wraplength=200)
        
        self.__labelTaskInfoDescription = Label(self.__frameTaskInfo,font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,justify="left",wraplength=450)
        
        self.__btnInfochangeDate = Button(self.__frameTaskInfo,text="Changer la date",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__changeDate)

        btnBackInfo = Button(self.__frameTaskInfo,text="Retour",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command=self.__backInfoTache)
        # Widget frame Change Date Info
        labelTitreChangeDateInfo = Label(self.__frameChangeDateInfo,font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,text="Changer la date")
        self.__chooseDateTask = DateEntry(self.__frameChangeDateInfo, width=15, background=self.__mainColor, 
                               foreground=self.__textColor, borderwidth=2,year=tomorrow.year, 
                               month=tomorrow.month, day=tomorrow.day)
        self.__btnValiderChangeDate = Button(self.__frameChangeDateInfo,text="Valider",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor)
        btnAnulerChangeDate = Button(self.__frameChangeDateInfo,text="Annuler",font=("arial","15"),
                                 fg=self.__textColor,bg=self.__mainColor,command = self.__backInfoTache)
        # Affichage Main
        self.__frameNavigation.place(relx=0.5, rely=1.0, anchor="s")
        # Affichage FrameNavigation 
        btnAddNav.place(relx=0.0, rely=0.5, anchor="w")  
        btnSupprNav.place(relx=1.0, rely=0.5, anchor="e") 
        btnCheckNav.place(relx=0.5, rely=0.5, anchor="center")
        # Affichage FrameTask
        labelTitreTask.place(relx=0.5, rely=0.0, anchor="n")
        # Affichage frameAdd 
        for i in range(0,3):
            labelTitreAdd[i].place(x=0,y=0)
        self.__btnValiderAdd[0].place(relx=1, rely=1, anchor='se')
        btnAnnulerAdd.place(relx=0, rely=1, anchor='sw')
        for i in range(1,3):
            self.__btnValiderAdd[i].place(relx=1, rely=1, anchor='se')

        self.__descriptionEntryTask.place(relx=0.5, rely=0.5, anchor="center")
        self.__nameTaskEntry.place(relx=0.5, rely=0.5, anchor="center")
        self.__chooseDateTask.place(relx=0.5, rely=0.5, anchor="center")
        self.__chooseDate.place(relx=0.5, rely=0.5, anchor="center")
        # Affichage frameSuppr
        labelTitreCheck.place(x=0,y=0)
        btnValiderCheck.place(relx=1, rely=1, anchor='se')
        btnAnnulerCheck.place(relx=0, rely=1, anchor='sw')
        # Affichage frameSuppr
        labelTitreSuppr.place(x=0,y=0)
        btnValiderSuppr.place(relx=1, rely=1, anchor='se')
        btnAnnulerSuppr.place(relx=0, rely=1, anchor='sw')
        self.__frameShowTache[0].place(x=0,y=labelTitreTask.winfo_reqheight())
        self.__frameShowTache[1].place(x=self.__frameShowTache[0].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight())
        self.__frameShowTache[2].place(x=self.__frameShowTache[0].winfo_reqwidth()+self.__frameShowTache[1].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight())
        
        self.__frameShowTache[3].place(x=0,y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
        self.__frameShowTache[4].place(x=self.__frameShowTache[3].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
        self.__frameShowTache[5].place(x=self.__frameShowTache[3].winfo_reqwidth()+self.__frameShowTache[4].winfo_reqwidth(),
                                       y=labelTitreTask.winfo_reqheight()+self.__frameShowTache[0].winfo_reqheight())
        
        btnBackInfo.place(relx=1, rely=1, anchor='se')

        self.__labelTaskInfoName.place(x=0,y=0)
        self.__labelTaskInfoDate.place(x=0,y=100)
        self.__labelTaskInfoDescription.place(x=0,y=200)

        labelTitreChangeDateInfo.place(x=0,y=0)
        self.__chooseDateTask.place(relx=0.5, rely=0.5, anchor="center")
        self.__btnValiderChangeDate.place(relx=1, rely=1, anchor='se')
        btnAnulerChangeDate.place(relx=0, rely=1, anchor='sw')
    
    def activeViewTask(self):
        self.__windows()
        self.__showTaskFrame()
    
    def activeViewAdd(self):
        self.__windows()
        self.__showAddFrame()
    
    def activeViewSuppr(self):
        check = self.__checkIsTache()
        if (check == True) :
            self.__windows()
            self.__showSupprFrame()
        return check
    
    def activeViewCheck(self):
        check = self.__checkIsTache()
        if (check == True) :
            self.__windows()
            self.__showCheckFrame()
        return check
        
    def __showAddFrame(self):
        self.__frameTask.place_forget()
        self.__frameCheck.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameAdd[0].place(x=0,y=0)
    
    def __showTaskFrame(self):
        self.__viewTacheFrame()
        self.__frameTask.place(x=0,y=0)
        self.__frameCheck.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameAdd[0].place_forget()
        self.__frameAdd[1].place_forget()
        self.__frameAdd[2].place_forget()

    def __checkIsTache(self):
        if(len(self.__taskFile.getContenuJSON())==0):
            return False
        else :
            return True

    def __showSupprFrame(self):
        if (self.__checkIsTache() == True) :
            dictTache = self.__taskFile.getContenuJSON()
            self.__frameTask.place_forget()
            self.__frameCheck.place_forget()
            self.__frameSuppr.place(x=0,y=0)
            self.__frameAdd[0].place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)]["name"])
            OptionMenu(self.__frameSuppr,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            showwarning("Avertisement","Vous pouvez supprimer une tache avant d'en ajouter")

    def __showCheckFrame(self):
        if(self.__checkIsTache()==True):
            dictTache = self.__taskFile.getContenuJSON()
            self.__frameTask.place_forget()
            self.__frameCheck.place(x=0,y=0)
            self.__frameSuppr.place_forget()
            self.__frameAdd[0].place_forget()
            nbTache = self.__taskFile.compteurFlagJSON()
            listTache = []
            for i in range(0,nbTache):
                listTache.append(dictTache[str(i)]["name"])
            OptionMenu(self.__frameCheck,self.__choixSuppr,*listTache).place(relx=0.5,rely=0.5,anchor="center")
            self.__choixSuppr.set(listTache[0])
        else :
            showwarning("Avertisement","Vous pouvez finir une tache avant d'en ajouter")

    def __addEvent(self):
        name = self.__nameTaskEntry.get()
        if(name==""):
            showwarning("Avertisement","Vous crée une tache sans nom")
        else :
            nb = self.__taskFile.compteurFlagJSON()
            self.__taskFile.creerFlagDictionnaire(str(nb))
            self.__taskFile.ajouterFlagDict(str(nb),"name",name)
            reponseDate = askyesno("Tache", "Voulez-vous mettre un date de fin ?")
            self.__nameTaskEntry.delete(0,END)
            if (reponseDate) :
                self.__addDate(str(nb))
            else :
                self.__taskFile.ajouterFlagDict(str(nb),"date","none")
                reponseDes = askyesno("Tache", "Voulez-vous mettre une description ?")
                if (reponseDes) :
                    self.__addDescription(str(nb))
                else :
                    self.__taskFile.ajouterFlagDict(str(nb),"description","none")
                    showinfo("Tache","Tache ajouter")
                    self.__showTaskFrame()

    def __addDate(self,nb:str):
        self.__frameAdd[0].place_forget()
        self.__frameAdd[2].place_forget()
        self.__frameAdd[1].place(x=0,y=0)
        self.__btnValiderAdd[1].configure(command=lambda:self.__addEventDate(nb))

    def __addDescription(self,nb:str):
        self.__frameAdd[0].place_forget()
        self.__frameAdd[1].place_forget()
        self.__frameAdd[2].place(x=0,y=0)
        self.__btnValiderAdd[2].configure(command=lambda:self.__addEventDescription(nb))
    
    def __addEventDate(self,nb:str):
        self.__taskFile.ajouterFlagDict(nb,"date",self.__formatageDateEntry(self.__chooseDate))
        reponseDes = askyesno("Tache", "Voulez-vous mettre une description ?")
        if (reponseDes) :
            self.__addDescription(nb)
        else :
            self.__taskFile.ajouterFlagDict(nb,"description","none")
            showinfo("Tache","Tache ajouter")
            self.__showTaskFrame()

    def __addEventDescription(self,nb:str):
        description = self.__descriptionEntryTask.get()
        self.__descriptionEntryTask.delete(0,END)
        if (description != ""):
            self.__taskFile.ajouterFlagDict(nb,"description",description)
            showinfo("Tache","Tache ajouter")
            self.__showTaskFrame()
        else :
            showwarning("Tache","Imposible d'ajouter une description vide")
    
    def __supprEvent(self):
        nameTache = self.__choixSuppr.get()       
        self.__taskFile.supprDictByFlag("name",nameTache)
        showinfo("événement","Tache supprimer")  
        self.__showTaskFrame()

    def __checkEvent(self,name="null"):
        if (name == "null") :
            nameTache = self.__choixSuppr.get()
        else :
            nameTache = name
        self.__taskFile.supprDictByFlag("name",nameTache)
        showinfo("événement","Tache fini et supprimer")
        self.__showTaskFrame() 

    def __formatageDateEntry(self,dateEntry:DateEntry):
        date_obj = dateEntry.get_date()  # Obtenir la date sous forme d'objet datetime.date
        formatted_date = f"{date_obj.year}-{date_obj.month}-{date_obj.day}"  # Formatter la date
        return formatted_date 
    
    def __viewTacheFrame(self):
        nb = self.__taskFile.compteurFlagJSON()
        dictTache = self.__taskFile.getContenuJSON()
        for i in range(0,6) :
            self.__labelNameShowTask[i].place(relx=0.5, rely=0.5, anchor="center")
            self.__labelNameShowTask[i].configure(text="Pas de tache",justify="center",wraplength=120)
            self.__btnInfoShowTask[i].place_forget()
        for i in range(0,nb):
            if (i < 6):
                self.__labelNameShowTask[i].place_forget()
                self.__labelNameShowTask[i].place(x=0,y=0)
                self.__labelNameShowTask[i].configure(text= dictTache[str(i)]["name"],wraplength=120,justify="left")
                self.__btnInfoShowTask[i].place(relx=0.5, rely=1.0, anchor="s")
                self.__btnInfoShowTask[i].configure(command=lambda:self.__viewInfoTacheFrame(str(i)))
                checkDate = self.__checkDateTache(str(i))
                if (checkDate == True):
                    self.__frameShowTache[i].configure(bg="red")
                    self.__labelNameShowTask[i].configure(bg="red",fg="white")
                else :
                    self.__frameShowTache[i].configure(bg=self.__mainColor)
                    self.__labelNameShowTask[i].configure(bg=self.__mainColor,fg=self.__textColor)

    def __viewInfoTacheFrame(self,nb:str):
        dictTache = self.__taskFile.getContenuJSON()[nb]
        name = dictTache["name"]
        date = dictTache["date"]
        description = dictTache["description"]
        
        self.__labelTaskInfoName.configure(text="Name : "+name)
        self.__labelTaskInfoDate.configure(text="Date : "+date)
        self.__labelTaskInfoDescription.configure(text="Description : "+description)

        self.__btnValiderChangeDate.configure(command=lambda :self.__changeEventDate(nb))

        self.__btnInfochangeDate.place(relx=1.0, y=100, anchor='ne')

        self.__frameNavigation.place_forget()
        self.__frameTask.place_forget()
        self.__frameTaskInfo.place(x=0,y=0)
    
    def __backInfoTache(self):
        self.__frameTaskInfo.place_forget()
        self.__frameChangeDateInfo.place_forget()
        self.__frameNavigation.place(relx=0.5, rely=1.0, anchor="s")
        self.__frameTask.place(x=0,y=0)
    
    def __changeDate(self):
        self.__frameTaskInfo.place_forget()
        self.__frameChangeDateInfo.place(x=0,y=0)

    def __changeEventDate(self,nb:str):
        date = self.__formatageDateEntry(self.__chooseDateTask)
        self.__taskFile.ajouterFlagDict(nb,"date",date)
        self.__frameTaskInfo.place_forget()
        self.__frameChangeDateInfo.place_forget()
        self.__frameNavigation.place(relx=0.5, rely=1.0, anchor="s")
        self.__showTaskFrame()
        showinfo("Tache","Date changer")
    
    def __checkDateTache(self,nb:str):
        self.__objDate.rafraichisement()
        dateToday = self.__objDate.annes()+"-"+self.__objDate.nbMoisSimple()+"-"+self.__objDate.jourSimple()
        hier = self.__objDate.otherPastDate(1)
        avantHier = self.__objDate.otherPastDate(2)
        dateTask = self.__taskFile.getContenuJSON()[nb]["date"]
        
        if ((dateTask==hier)or(dateTask==avantHier)):
            self.__taskFile.ajouterFlagDict(nb,"date",dateToday)
            dateTask = self.__taskFile.getContenuJSON()[nb]["date"]
            
        if (dateToday==dateTask):
            return True
        else :
            return False
    
    def getNbTache(self):
        return len(self.__taskFile.getContenuJSON())
    
    def getNbTacheToday(self):
        dictTache = self.__taskFile.getContenuJSON()
        dateToday = self.__objDate.annes()+"-"+self.__objDate.nbMoisSimple()+"-"+self.__objDate.jourSimple()
        nbTache = 0
        for i in range(0,len(dictTache)):
            if (dictTache[str(i)]["date"] == dateToday):
                nbTache = nbTache+1
        return nbTache
    
    def getTacheToday(self):
        dictTache = self.__taskFile.getContenuJSON()
        dateToday = self.__objDate.annes()+"-"+self.__objDate.nbMoisSimple()+"-"+self.__objDate.jourSimple()
        listTache = []
        for i in range(0,len(dictTache)):
            if (dictTache[str(i)]["date"] == dateToday) :
                listTache.append(dictTache[str(i)]["name"])
        return listTache

    def getTacheTowmorow(self):
        dictTache = self.__taskFile.getContenuJSON()
        dateTowmorow = self.__objDate.otherAfterDate(1)
        listTache = []
        for i in range(0,len(dictTache)):
            if (dictTache[str(i)]["date"] == dateTowmorow) :
                listTache.append(dictTache[str(i)]["name"])
        return listTache