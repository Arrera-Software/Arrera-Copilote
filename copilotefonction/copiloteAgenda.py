from tkinter import*
from datetime import datetime, timedelta
from librairy.travailJSON import*
import locale
from tkcalendar import DateEntry

class CArreraCopiloteAgenda :
    def __init__(self,file:str):
        self.__agendaFile = jsonWork(file)
        self.__mainColor = "white"
        self.__textColor = "black"
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        #.strftime("%A %d/%m/%Y")

    def __windows(self):
        self.__screen = Toplevel()
        self.__screen.title("Copilote : Agenda")
        self.__screen.maxsize(600,700)
        self.__screen.minsize(600,700)
        self.__screen.configure(bg="white")
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
        frame1 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frame2 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frame3 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        # Frame Management
        self.__frameAdd = Frame(self.__screen,width=600,height=350,bg=self.__mainColor)
        self.__frameSuppr = Frame(self.__screen,width=600,height=350,bg=self.__mainColor)
        self.__frameResumer = Frame(self.__screen,width=600,height=300,bg="red")
        self.__frameNavigation = Frame(self.__screen,width=600,height=50,bg=self.__mainColor)
        #Widget Frame Agenda
        labelYesterday = Label(frameYesterday,text=yesterday.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelToday = Label(frameToday,text=today.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg="green")
        labelTomorrow = Label(frameTomorrow,text=tomorrow.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay1 = Label(frame1,text=day1.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay2 =  Label(frame2,text=day2.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        labelDay3 = Label(frame3,text=day3.strftime("%A %d/%m/%Y"),font=("Arial","13"),bg=self.__mainColor)
        btnAdd = [Button(frameTomorrow,text="Ajouter",font=("Arial","13"),bg=self.__mainColor),
            Button(frame1,text="Ajouter",font=("Arial","13"),bg=self.__mainColor),
            Button(frame2,text="Ajouter",font=("Arial","13"),bg=self.__mainColor),
            Button(frame3,text="Ajouter",font=("Arial","13"),bg=self.__mainColor),]
        # Widget Frame Management 
        # FrameAdd 
        labelAdd = Label(self.__frameAdd,text="Ajout d'un événement",font=("arial","20"),bg=self.__mainColor,fg=self.__textColor)
        labelDate = Label(self.__frameAdd,text="Choisir date : ",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        labelName = Label(self.__frameAdd,text="Nom du rappel : ",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        chooseDate = DateEntry(self.__frameAdd, width=15, background='darkblue', foreground='white', borderwidth=2)
        entryName = Entry(self.__frameAdd,font=("arial",12),highlightthickness=2, highlightbackground="black")
        btnValiderAdd = Button(self.__frameAdd,text="Ajouter",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        # FrameSuppr
        labelSuppr = Label(self.__frameSuppr,text="Supprimer un événement",font=("arial","20"),bg=self.__mainColor,fg=self.__textColor)
        btnValiderSuppr = Button(self.__frameSuppr,text="Supprimer",font=("arial","15"),bg=self.__mainColor,fg=self.__textColor)
        # frameNavigation
        btnNavigationAdd = Button(self.__frameNavigation,text="Ajouter",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__addWindows)
        btnNavigationSuppr = Button(self.__frameNavigation,text="Supprimer",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__showFrameSuppr)
        # frameResumer
        labelTitreResumer = Label(self.__frameResumer,text="Resumer du jour :",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"))
        labelResumerToday = Label(self.__frameResumer,bg=self.__mainColor,fg=self.__textColor,font=("arial","15"))
        # Affichage Frame Agenda
        frameYesterday.place(x=0,y=0)
        frameToday.place(x=(frameYesterday.winfo_reqwidth()),y=0)
        frameTomorrow.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=0)
        frame1.place(x=(frameYesterday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        frame2.place(x=0,y=(frameYesterday.winfo_reqheight()))
        frame3.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        # Affichage Widget Frame Agenda
        labelYesterday.place(x=0,y=0)
        labelToday.place(x=0,y=0)
        labelTomorrow.place(x=0,y=0)
        labelDay1.place(x=0,y=0)
        labelDay2.place(x=0,y=0)
        labelDay3.place(x=0,y=0)
        btnAdd[0].place(relx=0.5,rely=0.5,anchor="center")
        btnAdd[1].place(relx=0.5,rely=0.5,anchor="center")
        btnAdd[2].place(relx=0.5,rely=0.5,anchor="center")
        btnAdd[3].place(relx=0.5,rely=0.5,anchor="center")
        # Affichage Frame Management
        # FrameAdd
        labelAdd.place(x=0,y=0)
        labelDate.place(x=0,y=55)
        chooseDate.place(x=190,y=60)
        labelName.place(x=0,y=105)
        entryName.place(x=200,y=110)
        btnValiderAdd.place(relx=0.5, rely=1.0, anchor="s")
        # FrameSuppr 
        labelSuppr.place(x=0,y=0)
        btnValiderSuppr.place(relx=0.5, rely=1.0, anchor="s")
        # frameNavigation
        btnNavigationAdd.place(relx=0.0, rely=0.5, anchor="w")
        btnNavigationSuppr.place(relx=1.0, rely=0.5, anchor="e")
        # frameResumer
        labelTitreResumer.place(x=0,y=0)
        labelResumerToday.place(x=0,y=40)
    
    def __showFrameSuppr(self):
        self.__frameAdd.place_forget()
        self.__frameResumer.place_forget()
        self.__frameNavigation.place_forget()
        listEvent = ["1","2","2"]
        OptionMenu(self.__frameSuppr,self.__choixSuppr,*listEvent).place(relx=0.5,rely=0.5,anchor="center")
        self.__choixSuppr.set(listEvent[0])
        self.__frameSuppr.place(x=0,y=self.__frameSuppr.winfo_reqheight())
    
    def __addWindows(self):
        self.__frameSuppr.place_forget()
        self.__frameResumer.place_forget()
        self.__frameNavigation.place_forget()
        self.__frameAdd.place(x=0,y=self.__frameAdd.winfo_reqheight())

    def activeAgenda(self):
        self.__windows()
        self.__frameAdd.place_forget()
        self.__frameSuppr.place_forget()
        self.__frameResumer.place(x=0,y=self.__frameAdd.winfo_reqheight())
        self.__frameNavigation.place(x=0,
                                     y=(self.__frameAdd.winfo_reqheight()+self.__frameResumer.winfo_reqheight()))

    
    def activeAddWindows(self):
        self.__addWindows()
        self.__windows()
        
    
    def activeSupprWindows(self):
        self.__windows()
        self.__showFrameSuppr()
        
        