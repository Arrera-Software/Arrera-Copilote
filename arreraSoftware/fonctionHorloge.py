from tkinter import*
from tkinter import messagebox
import time
from playsound import *
from librairy.travailJSON import*

class fncArreraHorloge :
    def __init__(self):
        self.__mainColor = str
        self.__textColor = str
        self.__icon = str
        self.__name = str
        self.__emplacementBIP = str
        
        
    def setAttribut(self,mainColor:str,textColor:str,icon:str,name:str,bip:str):
        self.__mainColor = mainColor
        self.__textColor = textColor
        self.__icon = icon
        self.__name = name
        self.__emplacementBIP = bip
    
    def setAtributJSON(self,fileJSON:jsonWork):
        self.__mainColor = fileJSON.lectureJSON("interfaceColor")
        self.__textColor = fileJSON.lectureJSON("interfaceTextColor")
        self.__icon = fileJSON.lectureJSON("iconAssistant")
        self.__name = fileJSON.lectureJSON("name")
        self.__emplacementBIP = fileJSON.lectureJSON("emplacementAssetHorloge")
          
    def __fenetreTK(self):
        self.__screen = Toplevel()
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        self.__screen.title(self.__name+" : Horloge")
        self.__screen.minsize(500,500)
        self.__screen.maxsize(500,500)
        self.__screen.config(bg=self.__mainColor)
        self.__frameBottom = Frame(self.__screen,bg=self.__mainColor,width=500,height=35)
        self.__frameChrono = Frame(self.__screen,bg=self.__mainColor,height=465,width=500)
        self.__frameMinuteur = Frame(self.__screen,bg=self.__mainColor,height=465,width=500)
        self.__frameHorloge = Frame(self.__screen,bg=self.__mainColor,height=465,width=500)
        self.__btn2 = Button(self.__frameBottom,text="Chronometre",font=("arial","13"),bg=self.__mainColor,fg=self.__textColor,command=self.__affichageChrono)
        self.__btn3 = Button(self.__frameBottom,text="Minuteur",font=("arial","13"),bg=self.__mainColor,fg=self.__textColor,command=self.__affichageMinuteur)
        self.__btn4 = Button(self.__frameBottom,text="Horloge",font=("arial","13"),bg=self.__mainColor,fg=self.__textColor,command=self.__affichageHorloge)
        self.__objetChrono = CHRONOMETRE(self.__frameChrono,self.__mainColor,self.__textColor)
        self.__objetAppMinuteur = AppMinuteur(self.__frameMinuteur,self.__mainColor,self.__textColor,self.__emplacementBIP)
        self.__objetHorloge = Clock(self.__frameHorloge,self.__mainColor,self.__textColor)
        self.__affichageBottom()
    
    def __affichageBottom(self):
        self.__btn2.place(x=0,y=0)
        self.__btn3.place(x=150,y=0)
        self.__btn4.place(x=260,y=0)
        self.__frameBottom.pack(side="bottom")
    
    def resetAffichage(self):
        self.__frameChrono.place_forget()
        self.__frameHorloge.place_forget()
        self.__frameMinuteur.place_forget()
    
    def modeChrono(self):
        self.__fenetreTK()
        self.__objetChrono.bootChrono()
        self.__frameChrono.place(x=0,y=0)
    
    def modeMinuteur(self):
        self.__fenetreTK()
        self.__objetAppMinuteur.bootAppMinuteur()
        self.__frameMinuteur.place(x=0,y=0)
    
    def modeBootMinuteur(self,duration:int) :
        self.__fenetreTK()
        self.__objetAppMinuteur.bootMinuteurInstentaner(duration)
        self.__frameMinuteur.place(x=0,y=0)
    
    def modeHorloge(self):
        self.__fenetreTK()
        self.__objetHorloge.bootClock()
        self.__frameHorloge.place(x=0,y=0)
    
    def __affichageChrono(self):
        self.resetAffichage() 
        self.__objetChrono.bootChrono()
        self.__frameChrono.place(x=0,y=0)
    
    def __affichageMinuteur(self):
        self.resetAffichage()
        self.__objetAppMinuteur.bootAppMinuteur()
        self.__frameMinuteur.place(x=0,y=0)
    
    def __affichageHorloge(self):
        self.resetAffichage()
        self.__objetHorloge.bootClock()
        self.__frameHorloge.place(x=0,y=0)
        
        
class CHRONOMETRE:
    def __init__(self,master,mainColor,textColor):
        self.__master = master
        self.__mainColor = mainColor
        self.__textColor = textColor
        self.__label = Label(self.__master, text="00:00", font=("arial", 40),bg=self.__mainColor,fg=self.__textColor)
        self.__startButton = Button(self.__master, text="Start", command=self.start ,font=("arial", 15),bg=self.__mainColor,fg=self.__textColor)
        self.__stopButton = Button(self.__master, text="Stop", command=self.stop ,font=("arial", 15),bg=self.__mainColor,fg=self.__textColor)
        self.__resetButton = Button(self.__master, text="Reset", command=self.reset ,font=("arial", 15),bg=self.__mainColor,fg=self.__textColor)
        self.__isRunning = bool
        self.__currentTime = int
        self.__startTime = int
        self.__elapsedTime = int

    def bootChrono(self):
        self.__label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__startButton.place(x=40,y=215)
        self.__stopButton.place(x=400,y=215)
        self.__resetButton.place(x=215,y=315)
        self.__isRunning = False
        self.__currentTime = 0
        self.__startTime = 0
        self.__elapsedTime = 0

    def start(self):
        if not self.__isRunning:
            self.__startTime = time.time()
            self.__isRunning = True
            self.UpdateTemps()

    def stop(self):
        if self.__isRunning:
            self.__isRunning = False

    def reset(self):
        self.__currentTime = 0
        self.__startTime = 0
        self.__elapsedTime = 0
        self.__label.configure(text="00:00")

    def UpdateTemps(self):
        if self.__isRunning:
            self.__currentTime = time.time()
            self.__elapsedTime = self.__currentTime - self.__startTime
            minutes, seconds = divmod(self.__elapsedTime, 60)
            self.__label.configure(text=f"{int(minutes):02d}:{int(seconds):02d}")
            self.__master.after(10, self.UpdateTemps)

        
class MINUTEUR:
    def __init__(self, master,mainColor,textColor,emplacementBIP:str):
        self.__master = master
        self.__mainColor = mainColor
        self.__textColor =  textColor
        self.__emplacementBIP =  emplacementBIP
        self.__duration = int
        self.__label = Label(master, font=("arial", 40),bg=self.__mainColor,fg=self.__textColor)
        self.__stopBTN = Button(master, text="Stop", command=self.stop,font=("arial", 15),bg=self.__mainColor,fg=self.__textColor)
        self.__running = False
        self.__currentTime = 0
        self.__startTime = 0
        self.__elapsedTime = 0

        
    def bootMinuteur(self,duration:int):
        self.__duration = duration
        self.__objetAPP = AppMinuteur(self.__master,self.__mainColor,self.__textColor,self.__emplacementBIP)
        self.__label.configure(text=self.FormatTemps(self.__duration))
        self.__label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__stopBTN.place(x=215,y=315)
        self.__currentTime = 0
        self.__startTime = 0
        self.__elapsedTime = 0
        self.__objetAPP.setOlminuteur(duration)
        if not self.__running:
            self.__startTime = time.time()
            self.__running = True
            self.UpdateHorloge()

    def stop(self):
        self.__label.place_forget()
        self.__stopBTN.place_forget()
        self.__objetAPP.bootAppMinuteur()
        if self.__running:
            self.__running = False


    def UpdateHorloge(self):
        if self.__running:
            self.__currentTime = time.time()
            self.__elapsedTime = self.__currentTime - self.__startTime
            remaining_time = self.__duration - self.__elapsedTime
            if remaining_time <= 0:
                playsound(self.__emplacementBIP)
                time.sleep(0.5)
                self.stop()
                self.__label.place_forget()
                self.__stopBTN.place_forget()
                self.__objetAPP.bootAppMinuteur()
            self.__label.configure(text=self.FormatTemps(remaining_time))
            self.__master.after(10, self.UpdateHorloge)

    def FormatTemps(self, time):
        minutes, seconds = divmod(time, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"


class AppMinuteur :
    def __init__(self,master,mainColor:str,textColor:str,emplacementBIP:str):
        self.__master = master
        self.__mainColor = mainColor
        self.__textColor = textColor
        self.__emplacementBIP = emplacementBIP
        self.__oldMinuteur = 0
        self.__zoneEntrer = Frame(master,bg=mainColor)
        self.__entryMin = Entry(self.__zoneEntrer,width=5,font=("arial","15"))
        self.__entrySec = Entry(self.__zoneEntrer,width=5,font=("arial","15"))
        self.__labelMin = Label(self.__zoneEntrer,text="min",font=("arial","15"),bg=mainColor,fg=textColor)
        self.__labelSec = Label(self.__zoneEntrer,text="s",font=("arial","15"),bg=mainColor,fg=textColor)
        self.__btnBoot = Button(master,text="Demarrer",bg=mainColor,fg=textColor,font=("arial","15"),command=self._boot)
        self.__btnPrereglage1 = Button(master,text="15 minutes",bg=mainColor,fg=textColor,command=self._prereglage1,font=("arial","15"))
        self.__btnPrereglage2 = Button(master,text="30 minutes",bg=mainColor,fg=textColor,command=self._prereglage2,font=("arial","15"))
        self.__btnOldMinuteur = Button(master,text="Relancer minuteur",bg=mainColor,fg=textColor,font=("arial","15"),command=self._bootOldMinuteur)
        self.__objetMinuteur = MINUTEUR(self.__master,self.__mainColor,self.__textColor,self.__emplacementBIP)
    
    def bootAppMinuteur(self):    
        self.__zoneEntrer.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__entryMin.pack(side="left")
        self.__labelMin.pack(side="left")
        self.__entrySec.pack(side="left")
        self.__labelSec.pack(side="left")
        self.__btnBoot.place(x=185,y=315)
        self.__btnPrereglage1.place(x=15,y=315)
        self.__btnPrereglage2.place(x=370,y=315)
        if self.__oldMinuteur != 0 :
            self.__btnOldMinuteur.place(x=205,y=415)
            
    def bootMinuteurInstentaner(self,duration:int):
        self.__objetMinuteur.bootMinuteur(duration)
        
    def setOlminuteur(self,nb:int):
        self.__oldMinuteur =  nb
    
    def _noAffichage(self):
        self.__zoneEntrer.place_forget()
        self.__btnBoot.place_forget()
        self.__btnPrereglage1.place_forget()
        self.__btnPrereglage2.place_forget()
    
    def _prereglage1(self):
        self._noAffichage()
        self.__objetMinuteur.bootMinuteur(900)
    
    def _prereglage2(self):
        self._noAffichage()
        self.__objetMinuteur.bootMinuteur(1800)
        
    def _bootOldMinuteur(self):
        self._noAffichage() 
        self.__objetMinuteur.bootMinuteur(self.__oldMinuteur)
    
    def _boot(self):
        valMin = self.__entryMin.get()
        valSec = self.__entrySec.get()
        if valMin == "" :
            min = 0
        else :       
            min = int(valMin)*60
        if valSec == "" :
            sec = 0
        else :
            sec = int(valSec) 
        if sec == 0 and min == 0 :
            messagebox.showinfo("Minuteur imposible", "Imposible de lancer un minuteur de 0 minute et 0 second")
        else :
            self._noAffichage()      
            temps = min + sec
            self.__objetMinuteur.bootMinuteur(temps)
            
        
class Clock() :
    def __init__(self,master,mainColor,textColor):
        self.__master = master
        self.__clock = Label(master, font = ("arial", 60, "bold"),bg=mainColor,fg=textColor)

    def bootClock(self):
        self.__clock.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.time()
    
    def time(self): 
        self.running = True
        current_time = time.strftime("%H:%M:%S")
        self.__clock.config(text=current_time)
        self.__master.after(10,self.time)