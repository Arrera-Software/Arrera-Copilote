import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
import time
from tkinter.messagebox import *
from lib.arrera_tk import *
import threading as th
from brain.brain import ABrain
import random
from src.copilote_widget import *

class copilote_gui(aTk):
    def __init__(self,iconFolder:str,iconName:str,
                 six_brain:ABrain,ryley_brain:ABrain,theme_file:str,
                 version:str):
        self.__nameSoft = "Arrera Copilote"
        self.__first_boot = False
        self.__assistant_load = False
        self.__speak_is_enable = True
        self.__L_img_boot_gui = []
        self.__D_img_speak_gui = {}
        self.__dir_gui_dark = "asset/GUI/dark/"
        self.__dir_gui_light = "asset/GUI/light/"

        # Recuperation des cerveau
        self.__six_brain = six_brain
        self.__ryley_brain = ryley_brain

        # Recuperation gestionnaire
        self.__gestionnaire = self.__six_brain.getGestionnaire()

        # Recuperation librairy
        self.__objOS = self.__gestionnaire.getOSObjet()
        self.__arr_voice = self.__gestionnaire.getArrVoice()

        # Theard
        self.__th_reflect = th.Thread()
        self.__th_speak = th.Thread()

        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))

        self.geometry("500x400+5+30")
        #self.protocol("WM_DELETE_WINDOW", self.__on_close)

        if self.__objOS.osLinux():
            self.__emplacementIcon = iconFolder+"linux/"+iconName+".png"
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))
        elif self.__objOS.osWindows():
            self.__emplacementIcon = iconFolder+"win/"+iconName+".ico"
            self.iconbitmap(self.__emplacementIcon)
        elif self.__objOS.osMac():
            self.__emplacementIcon = resource_path(iconFolder+"mac/"+iconName+".png")
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))

        # Canvas

        self.__c_boot = self.__canvas_boot()

        self.__c_speak = self.__canvas_speak()

        self.__c_maj = self.__canvas_maj()

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()

        self.mainloop()

    def __boot(self):
        # TODO : Gerer le first boot
        self.__c_maj.place_forget()
        self.__sequence_boot()
        self.__sequence_speak(self.__six_brain.boot())


    # Creation des widget

    def __canvas_boot(self):
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b0.png",self.__dir_gui_dark+"b0.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b1.png",self.__dir_gui_dark+"b1.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b2.png",self.__dir_gui_dark+"b2.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b3.png",self.__dir_gui_dark+"b3.png"))
        self.__L_img_boot_gui.append((self.__dir_gui_light+"b4.png",self.__dir_gui_dark+"b4.png"))

        l_img,d_img = self.__L_img_boot_gui[0]

        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,
                             fg_color=("#ffffff","#000000"),width=500,height=350)

        return c

    def __canvas_speak(self):
        self.__D_img_speak_gui = {"copilote":(self.__dir_gui_light+"parole_copilote.png",self.__dir_gui_dark+"parole_copilote.png"),
                                  "six":(self.__dir_gui_light+"parole_six.png",self.__dir_gui_dark+"parole_six.png"),
                                  "ryley":(self.__dir_gui_light+"parole_ryley.png",self.__dir_gui_dark+"parole_ryley.png"),
                                  "speak":(self.__dir_gui_light+"during_parole.png",self.__dir_gui_dark+"during_parole.png")}

        l_img,d_img = self.__D_img_speak_gui["copilote"]
        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,
                             fg_color=("#ffffff","#000000"),width=500,height=350)

        self.__l_speak = aLabel(self,text="",justify="left",wraplength=440,
                                police_size=20,corner_radius=0)

        return c

    def __canvas_maj(self):
        c = aBackgroundImage(self,background_light=self.__dir_gui_light+"MAJ.png",
                             background_dark=self.__dir_gui_dark+"MAJ.png",
                             fg_color=("#ffffff","#000000"),width=500,height=350)

        label_text = aLabel(c,
                            text="La version d’Arrera Copilote la plus récente est disponible. Installez-la pour avoir de nouvelles fonctionnalités et des corrections de bugs.",
                            police_size=20,
                            fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"),
                            wraplength=250, justify="left")

        btn_update = aButton(c, text="Mettre a jour", size=20,
                             command=lambda: wb.open("https://github.com/Arrera-Software/Arrera-Copilote/releases/"))

        btn_continuer = aButton(c, text="Me rappeler plus tart", size=20, command=self.__boot)

        label_text.place(x=190, y=40)
        btn_update.placeBottomLeft()
        btn_continuer.placeBottomRight()
        return c

    # Methode change IMG

    def __change_img_boot(self,index:int):
        if index < len(self.__L_img_boot_gui):
            l_img,d_img = self.__L_img_boot_gui[index]
        else :
            l_img,d_img = self.__L_img_boot_gui[0]

        self.__c_boot.change_background(background_light=l_img, background_dark=d_img)
        self.update()

    def __change_gui_speak(self):
        nb = random.randint(0,2)
        match nb :
            case 0 :
                self.__set_copilote_speak()
            case 1 :
                self.__set_six_speak()
            case 2 :
                self.__set_ryley_speak()


    def __set_copilote_speak(self):
        l_img,d_img = self.__D_img_speak_gui["copilote"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.__l_speak.place(x=25, y=90)

    def __set_six_speak(self):
        l_img,d_img = self.__D_img_speak_gui["six"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.__l_speak.place(x=25, y=90)

    def __set_ryley_speak(self):
        l_img,d_img = self.__D_img_speak_gui["ryley"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.__l_speak.place(x=25, y=90)


    def __set_voice_speak(self):
        l_img,d_img = self.__D_img_speak_gui["speak"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#3b224a","#3b224a"),text_color=("#ffffff","#ffffff"))
        self.__l_speak.place(x=40, y=100)

    # Methode des sequence

    def __sequence_boot(self):
        self.__change_img_boot(0)
        self.__c_boot.place(x=0, y=0)
        time.sleep(0.2)
        self.__change_img_boot(1)
        time.sleep(0.2)
        self.__change_img_boot(2)
        time.sleep(0.2)
        self.__change_img_boot(3)
        time.sleep(0.2)
        self.__change_img_boot(4)
        time.sleep(0.2)


    # Partie parole

    def __sequence_speak(self,text:str):
        self.__c_boot.place_forget()
        self.__c_speak.place(x=0, y=0)

        self.__l_speak.configure(text=text)

        if self.__speak_is_enable:
            self.__set_voice_speak()
            self.__th_speak = th.Thread(target=self.__arr_voice.say,args=(text,))
            self.__th_speak.start()
            self.__update_during_speak()
        else :
            self.__change_gui_speak()

    # Methode update

    def __update_during_speak(self):
        if self.__th_speak.is_alive():
            self.after(100,self.__update_during_speak)
        else :
            self.__th_speak = th.Thread()
            self.__change_gui_speak()