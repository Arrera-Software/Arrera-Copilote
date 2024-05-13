from tkinter import*
import webbrowser as w

class CHLibrairy:
    def __init__(self,mainColor:str,textColor:str):
        self.__lienLibrairy = "https://github.com/Arrera-Software/Arrera-librairy"
        self.__lienReadme =  "https://github.com/Arrera-Software/Arrera-librairy/blob/main/README.md"
        self.__lienObjetPython = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/python"
        self.__lienObjetCPP = "https://github.com/Arrera-Software/Arrera-librairy/tree/main/C%2B%2B"
        self.__mainColor = mainColor
        self.__textColor = textColor
    
    def librairy(self):
        self.__screenLibrairy = Toplevel()
        self.__screenLibrairy.title("CodeHelp : librairy")
        self.__screenLibrairy.minsize(700,500)
        self.__screenLibrairy.iconphoto(False,PhotoImage(file="asset/icon/codehelp/icon.png"))
        self.__screenLibrairy.configure(bg=self.__mainColor)
        #widget
        btnlib = Button(self.__screenLibrairy,text="Librairy",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openLib)
        btnReadme = Button(self.__screenLibrairy,text="Readme",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openReadme)
        btnObjetPyton = Button(self.__screenLibrairy,text="Objet Python",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openObjPython)
        btnObjetCPP = Button(self.__screenLibrairy,text="Objet C++",bg=self.__mainColor,fg=self.__textColor,font=("arial","15"),command=self.__openObjCPP)
        #affichage
        btnlib.place(relx=0.1, rely=0.1)
        btnObjetPyton.place(relx=0.1, rely=0.8)
        btnObjetCPP.place(relx=0.8, rely=0.1)
        btnReadme.place(relx=0.8, rely=0.8)

    def __destroyWindows(self):
        self.__screenLibrairy.destroy()

    def __openLib(self):
        w.open(self.__lienLibrairy)
        self.__destroyWindows()
    
    def __openReadme(self):
        w.open(self.__lienReadme)
        self.__destroyWindows()
    
    def __openObjPython(self):
        w.open(self.__lienObjetPython)
        self.__destroyWindows()
    
    def __openObjCPP(self):
        w.open(self.__lienObjetCPP)
        self.__destroyWindows()