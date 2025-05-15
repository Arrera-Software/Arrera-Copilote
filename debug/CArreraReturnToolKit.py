from tkinter import*
from librairy.travailJSON import *
from librairy.dectectionOS import *
import webbrowser as wb

class CArreraReturnToolKit :
    def __init__(self,debugConf:str):
        configFile = jsonWork(debugConf)
        self.__name = configFile.lectureJSON("NameSoft")
        self.__color = configFile.lectureJSON("color")
        self.__textcolor = configFile.lectureJSON("textColor")
        self.__styleTextTitle = ("Arial",25)
        self.__styleText = ("Arial", 15)
        self.__txtBTN = [configFile.lectureJSON("btn1Text"),configFile.lectureJSON("btn3Text"),
                         configFile.lectureJSON("btn2Text"),configFile.lectureJSON("btn4Text")]
        self.__linkBTN = [configFile.lectureJSON("btn1Link"),configFile.lectureJSON("btn3Link"),
                         configFile.lectureJSON("btn2Link"),configFile.lectureJSON("btn4Link")]
        self.__textAcceuil = configFile.lectureJSON("explication")

    def active(self):
        # Creation de la fenetre
        win = Toplevel()
        win.title(self.__name)
        if (OS().osLinux() == True):
            width = 500
            height = 635
        else:
            width = 500
            height = 610
        win.maxsize(width, height)
        win.minsize(width, height)
        win.configure(bg=self.__color)
        # Frame
        self.__explicationFrame = Frame(win,width=width,height=height,bg=self.__color)
        self.__mainFrame = Frame(win,width=width,height=height,bg=self.__color)
        frameBTN = Frame(self.__mainFrame,width=400,height=400,bg=self.__color)
        # Widget
        # Main
        labelTitle = Label(self.__mainFrame,text=self.__name,
                           bg=self.__color,
                           font=self.__styleTextTitle,fg=self.__textcolor)
        btnQuit = Button(self.__mainFrame,text="Quitter",bg=self.__color,
                         fg=self.__textcolor,font=self.__styleText,
                         command=lambda : win.quit())
        #BTN
        btn1 = Button(frameBTN,text=self.__txtBTN[0],font=self.__styleText,
                      bg=self.__color,fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[0]))
        btn2 = Button(frameBTN, text=self.__txtBTN[1], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[1]))
        btn3 = Button(frameBTN, text=self.__txtBTN[2], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=120,
                      command= lambda : wb.open(self.__linkBTN[2]))
        btn4 = Button(frameBTN, text=self.__txtBTN[3], font=self.__styleText,
                      bg=self.__color, fg=self.__textcolor,wraplength=100,
                      command= lambda : wb.open(self.__linkBTN[3]))
        # Explication Frame
        labelTitleExplication = Label(self.__explicationFrame,text=self.__name,bg=self.__color,
                                      fg=self.__textcolor,font=self.__styleTextTitle)
        labelExplication = Label(self.__explicationFrame,text=self.__textAcceuil,bg=self.__color,
                                 fg=self.__textcolor,font=self.__styleText,wraplength=470,justify="left")
        btnContinuer = Button(self.__explicationFrame,text="Continuer",bg=self.__color,
                              fg=self.__textcolor,font=self.__styleText,command=self.__viewMainFrame)
        # Affichage
        self.__explicationFrame.place(x=0,y=0)
        # BTN
        if self.__txtBTN[0] and self.__linkBTN[0] :
            btn1.place(relx=0.0, rely=0.0, anchor='nw')
        if self.__txtBTN[1] and self.__linkBTN[1]:
            btn2.place(relx=1.0, rely=0.0, anchor='ne')
        if self.__txtBTN[2] and self.__linkBTN[2]:
            btn3.place(relx=0, rely=1, anchor='sw')
        if self.__txtBTN[3] and self.__linkBTN[3]:
            btn4.place(relx=1, rely=1, anchor='se')

        # Mainframe
        frameBTN.place(relx=0.5, rely=0.5, anchor="center")
        labelTitle.place(relx=0.5, rely=0.0, anchor="n")
        btnQuit.place(relx=0.5, rely=1.0, anchor="s")

        # Explication Frame
        labelTitleExplication.place(relx=0.5, rely=0.0, anchor="n")
        labelExplication.place(x=20,y=50)
        btnContinuer.place(relx=0.5, rely=1.0, anchor="s")

    def __viewMainFrame(self):
        self.__explicationFrame.place_forget()
        self.__mainFrame.place(x=0, y=0)