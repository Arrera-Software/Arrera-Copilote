from tkinter import*
from datetime import datetime, timedelta
from librairy.travailJSON import*
import locale

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
    
    def activeAgenda(self):
        self.__windows()
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)
        day1 = today + timedelta(days=2)
        day2 = today + timedelta(days=3)
        day3 = today + timedelta(days=4)
        # Frame
        frameYesterday = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frameToday = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg="green")
        frameTomorrow = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frame1 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frame2 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        frame3 = Frame(self.__screen,width=200,height=175,borderwidth=2, relief="solid",bg=self.__mainColor)
        #Widget 
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
        # Affichage Frame
        frameYesterday.place(x=0,y=0)
        frameToday.place(x=(frameYesterday.winfo_reqwidth()),y=0)
        frameTomorrow.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=0)
        frame1.place(x=(frameYesterday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        frame2.place(x=0,y=(frameYesterday.winfo_reqheight()))
        frame3.place(x=(frameYesterday.winfo_reqwidth()+frameToday.winfo_reqwidth()),y=(frameYesterday.winfo_reqheight()))
        # Affichage Widget
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