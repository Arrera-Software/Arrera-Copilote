from tkinter import StringVar

from gui.guibase import GuiBase,gestionnaire

class GUIHorloge(GuiBase):
    def __init__(self, gest: gestionnaire):
        super().__init__(gest, "Horloge")
        self.__fncHorloge = self._gestionnaire.getGestFNC().getFNCHorloge()
        self.__assetDirectory = self._gestionnaire.getConfigFile().asset+"horloge/"
        self.__clockEnable = False
        self.__minuteurEnable = False

    def _mainframe(self):
        # Variables
        self.__varMinute = StringVar(self._screen)
        self.__varSec = StringVar(self._screen)
        # Conf de la fenetre
        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # Frame principal
        self.__frameNav = self._arrtk.createFrame(self._screen)
        self.__frameHorloge = self._arrtk.createFrame(self._screen)
        self.__frameChrono = self._arrtk.createFrame(self._screen)
        self.__frameMinuteur = self._arrtk.createFrame(self._screen)

        # Frame secondaire
        self.__frameSetMinuteur = self._arrtk.createFrame(self.__frameMinuteur)
        self.__frameViewMinuteur = self._arrtk.createFrame(self.__frameMinuteur)

        # Conf frame
        self.__frameNav.grid_columnconfigure(0, weight=1)  # espace à gauche
        self.__frameNav.grid_columnconfigure(1, uniform="btns")
        self.__frameNav.grid_columnconfigure(2, uniform="btns")
        self.__frameNav.grid_columnconfigure(3, uniform="btns")
        self.__frameNav.grid_columnconfigure(4, weight=1)
        self.__frameNav.grid_rowconfigure(0, weight=0)

        self.__frameHorloge.grid_rowconfigure(0, weight=1)
        self.__frameHorloge.grid_columnconfigure(0, weight=1)

        self.__frameMinuteur.grid_rowconfigure(0, weight=1)
        self.__frameMinuteur.grid_columnconfigure(0, weight=1)

        self.__frameSetMinuteur.grid_rowconfigure(0, weight=1)
        self.__frameSetMinuteur.grid_rowconfigure(1, weight=1)
        self.__frameSetMinuteur.grid_rowconfigure(2, weight=1)
        self.__frameSetMinuteur.grid_columnconfigure(0, weight=1, uniform="cols")
        self.__frameSetMinuteur.grid_columnconfigure(1, weight=1, uniform="cols")
        self.__frameSetMinuteur.grid_columnconfigure(2, weight=1, uniform="cols")

        self.__frameViewMinuteur.grid_columnconfigure(0, weight=1)

        self.__frameViewMinuteur.grid_rowconfigure(0, weight=1)
        self.__frameViewMinuteur.grid_rowconfigure(1, weight=0)
        self.__frameViewMinuteur.grid_rowconfigure(2, weight=0)
        self.__frameViewMinuteur.grid_rowconfigure(3, weight=1)

        self.__frameChrono.grid_columnconfigure(0, weight=1, uniform="cols")
        self.__frameChrono.grid_columnconfigure(1, weight=1, uniform="cols")
        self.__frameChrono.grid_columnconfigure(2, weight=1, uniform="cols")
        self.__frameChrono.grid_rowconfigure(0, weight=1)
        self.__frameChrono.grid_rowconfigure(1, weight=0)
        self.__frameChrono.grid_rowconfigure(2, weight=0)
        self.__frameChrono.grid_rowconfigure(3, weight=1)

        # img
        tailleIMG = 30
        imgHorloge = self._arrtk.createImage(pathDark=self.__assetDirectory+"horloge.png",
                                             pathLight=self.__assetDirectory+"horloge.png",
                                             tailleX=tailleIMG,tailleY=tailleIMG)
        imgChrono = self._arrtk.createImage(pathDark=self.__assetDirectory+"chronometre.png",
                                             pathLight=self.__assetDirectory+"chronometre.png",
                                             tailleX=tailleIMG,tailleY=tailleIMG)
        imgMinuteur = self._arrtk.createImage(pathDark=self.__assetDirectory+"minuteur.png",
                                             pathLight=self.__assetDirectory+"minuteur.png",
                                             tailleX=tailleIMG,tailleY=tailleIMG)

        # Widget
        # Nav
        btnHorloge = self._arrtk.createButton(self.__frameNav,text="",image=imgHorloge,
                                              command=self.__viewHorloge,
                                              bg=self._btnColor,fg=self._btnTexteColor,)
        btnMinuteur = self._arrtk.createButton(self.__frameNav,text="",image=imgMinuteur,
                                               command=self.__viewMinuteur,
                                               bg=self._btnColor,fg=self._btnTexteColor,)
        btnChrono = self._arrtk.createButton(self.__frameNav,text="",image=imgChrono,
                                             command=self.__viewChrono,
                                             bg=self._btnColor,fg=self._btnTexteColor,)
        # Horloge
        self.__labelViewClock = self._arrtk.createLabel(self.__frameHorloge,text="00:00:00",
                                                        ppolice="Arial",ptaille=60,pstyle="bold")

        # Minuteur
        # Set Minuteur
        picketMinuteur = self._arrtk.createHourPickert(self.__frameSetMinuteur,
                                                       varHour=self.__varMinute,
                                                       varMinute=self.__varSec)
        btnReset = self._arrtk.createButton(self.__frameSetMinuteur,text="Reset"
                                            ,command=self.__resetMinuteur,
                                            bg=self._btnColor,fg=self._btnTexteColor,
                                            ppolice="Arial",ptaille=25)
        btnStartMinuteur1 = self._arrtk.createButton(self.__frameSetMinuteur,text="Start",
                                                     command=self.__startMinuteur,
                                                     bg=self._btnColor,fg=self._btnTexteColor,
                                                     ppolice="Arial",ptaille=25)
        btnStartMinuteur2 = self._arrtk.createButton(self.__frameSetMinuteur,text="1 Min",
                                                     command=self.__setOneMin,
                                                     bg=self._btnColor,fg=self._btnTexteColor,
                                                     ppolice="Arial",ptaille=25)
        btnStartMinuteur3 = self._arrtk.createButton(self.__frameSetMinuteur, text="3 Min",
                                                     command=self.__setThreeMin,
                                                     bg=self._btnColor,fg=self._btnTexteColor,
                                                     ppolice="Arial",ptaille=25)


        # View Minuteur
        self.__labelViewTimeMinuteur = self._arrtk.createLabel(self.__frameViewMinuteur,text="00:00:00",
                                                        ppolice="Arial",ptaille=60,pstyle="bold")
        btnStopMinuteur = self._arrtk.createButton(self.__frameViewMinuteur,text="Stop",
                                                  command=self.__fncHorloge.stopMinuteur,
                                                   bg=self._btnColor,fg=self._btnTexteColor,
                                                   ppolice="Arial",ptaille=25)

        # Chrono
        self.__labelViewChrono = self._arrtk.createLabel(self.__frameChrono,text="00:00:00",
                                                        ppolice="Arial",ptaille=60,pstyle="bold")

        btnResetChrono = self._arrtk.createButton(self.__frameChrono,text="Reset",
                                                  command=self.__resetChrono,
                                                  bg=self._btnColor,fg=self._btnTexteColor,
                                                  ppolice="Arial",ptaille=25)

        self.__btnStartStopChrono = self._arrtk.createButton(self.__frameChrono,text="Start",
                                                             command=self.__enableOrDisableChrono,
                                                             bg=self._btnColor,fg=self._btnTexteColor,
                                                             ppolice="Arial",ptaille=25)

        # Placement des widget
        btnHorloge.grid( row=0, column=1, padx=(8, 8), pady=10)
        btnMinuteur.grid(row=0, column=2, padx=(8, 8), pady=10)
        btnChrono.grid( row=0, column=3, padx=(8, 8), pady=10)

        self.__labelViewClock.grid(row=0, column=0, padx=10, pady=10)

        picketMinuteur.grid(row=1, column=1, padx=12, pady=12)
        btnStartMinuteur2.grid(row=1, column=0, padx=8, pady=8)
        btnStartMinuteur3.grid(row=1, column=2, padx=8, pady=8)
        btnReset.grid(row=2, column=1, padx=8, pady=(6, 2))
        btnStartMinuteur1.grid(row=3, column=1, padx=8, pady=(2, 12))

        self.__labelViewChrono.grid(row=1, column=1, padx=12, pady=12)
        btnResetChrono.grid(row=2, column=0, padx=10, pady=(6, 12))
        self.__btnStartStopChrono.grid(row=2, column=2, padx=10, pady=(6, 12))

        self.__labelViewTimeMinuteur.grid(row=1, column=0, padx=12, pady=12)
        btnStopMinuteur.grid(row=2, column=0, padx=12, pady=(8, 16))

        self.__frameNav.grid(row=0, column=0, sticky="ew")
        self.__frameHorloge.grid(row=1, column=0, sticky="nsew")

        self.__clockEnable = True
        self.__activeClock()

    def __disableAllFrame(self):
        self.__frameHorloge.grid_forget()
        self.__frameChrono.grid_forget()
        self.__frameMinuteur.grid_forget()

    def __viewHorloge(self):
        self.__disableAllFrame()
        self.__clockEnable = True
        self.__activeClock()
        self.__frameHorloge.grid(row=1, column=0, sticky="nsew")

    def __viewMinuteur(self):
        self.__disableAllFrame()
        self.__clockEnable = False
        self.__frameMinuteur.grid(row=1, column=0, sticky="nsew")
        if self.__minuteurEnable:
            self.__frameSetMinuteur.grid_forget()
            self.__frameViewMinuteur.grid(row=0, column=0, sticky="nsew")
        else :
            self.__frameViewMinuteur.grid_forget()
            self.__frameSetMinuteur.grid(row=0, column=0, sticky="nsew")

    def activeMinuteur(self):
        self.active()
        self.__viewMinuteur()

    def __viewChrono(self):
        self.__disableAllFrame()
        self.__clockEnable = False
        self.__frameChrono.grid(row=1, column=0, sticky="nsew")

    def activeChrono(self):
        self.active()
        self.__viewChrono()

    # Horloge
    def __activeClock(self):
        if self.__clockEnable:
            current_time = self.__fncHorloge.getHorloge()
            self.__labelViewClock.configure(text=current_time)
            self._screen.after(1000, self.__activeClock)

    # Minuteur
    def __setThreeMin(self):
        self.__varMinute.set("03")
        self.__varSec.set("00")

    def __setOneMin(self):
        self.__varMinute.set("01")
        self.__varSec.set("00")

    def __resetMinuteur(self):
        self.__varMinute.set("00")
        self.__varSec.set("00")
        self.__labelViewTimeMinuteur.configure(text="00:00:00")

    def __startMinuteur(self):
        min = self.__varMinute.get()
        sec = self.__varSec.get()
        if min == "" and sec == "":
            return False
        try :
            min = int(min)
            sec = int(sec)

            time = min * 60 + sec
            if time <= 0:
                return False
            else :
                self.__fncHorloge.startMinuteur(time)
                self.__minuteurEnable = True
                self.__frameViewMinuteur.grid(row=0, column=0, sticky="nsew")
                self.__frameSetMinuteur.grid_forget()
                self._screen.after(1, self.__updateMinuteur)
                return True
        except ValueError:
            return False

    def __updateMinuteur(self):
        self.__minuteurEnable = self.__fncHorloge.getStatMinuteur()
        if self.__minuteurEnable:
            time = self.__fncHorloge.getTimeMinuteur()
            if time is None:
                self.__minuteurEnable = False
                self.__labelViewTimeMinuteur.configure(text="00:00:00")
                self.__frameViewMinuteur.grid_forget()
                self.__frameSetMinuteur.grid(row=0, column=0, sticky="nsew")
                return False
            else :
                self.__labelViewTimeMinuteur.configure(text=time)
                self._screen.after(1, self.__updateMinuteur)
                return True
        else:
            self.__minuteurEnable = False
            self.__frameViewMinuteur.grid_forget()
            self.__frameSetMinuteur.grid(row=0, column=0, sticky="nsew")
            return False

    # Chrono

    def __enableOrDisableChrono(self):
        if not self.__fncHorloge.getStatChrono():
            self.__btnStartStopChrono.configure(text="Stop")
            self.__fncHorloge.startChrono()
            self._screen.after(100, self.__updateChrono)
        else :
            self.__btnStartStopChrono.configure(text="Start")
            self.__fncHorloge.stopChrono()

    def __updateChrono(self):
        if self.__fncHorloge.getStatChrono():
            time = self.__fncHorloge.getTimeChrono()

            total_cs = int(round(time * 100))           # 1 s = 100 centièmes
            minutes, rem_cs = divmod(total_cs, 60 * 100)  # 6000 = 60s * 100cs
            seconds, centiseconds = divmod(rem_cs, 100)

            time = f"{minutes:02d}:{seconds:02d}:{centiseconds:02d}"

            self.__labelViewChrono.configure(text=str(time))
            self._screen.after(100, self.__updateChrono)

    def __resetChrono(self):
        self.__fncHorloge.resetChrono()
        self.__fncHorloge.stopChrono()
        self.__btnStartStopChrono.configure(text="Start")
        self.__labelViewChrono.configure(text="00:00:00")

