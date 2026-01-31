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
        self.__L_img_boot_gui = []
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

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        self.__boot()

        self.mainloop()

    def __boot(self):
        # TODO : Gerer le first boot
        #self.__c_maj.place_forget()
        self.__sequence_boot()
        #self.__sequence_speak(self.__brain.boot())


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

    # Methode change IMG

    def __change_img_boot(self,index:int):
        if index < len(self.__L_img_boot_gui):
            l_img,d_img = self.__L_img_boot_gui[index]
        else :
            l_img,d_img = self.__L_img_boot_gui[0]

        self.__c_boot.change_background(background_light=l_img, background_dark=d_img)
        self.update()

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
