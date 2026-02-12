import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
import time
from tkinter.messagebox import *
from lib.arrera_tk import *
import threading as th
from brain.brain import ABrain
import random
from src.copilote_widget import back_widget,quick_setting
from src.copilote_setting import copilote_setting
from src.copilote_language import copilote_language

class copilote_gui(aTk):
    def __init__(self,iconFolder:str,iconName:str,
                 six_brain:ABrain,ryley_brain:ABrain,theme_file:str,
                 version:str):
        self.__nameSoft = "Arrera Copilote"
        self.__first_boot = False
        self.__assistant_load = False
        self.__speak_is_enable = False
        self.__assistant_speaking = False
        self.__micro_is_enable = False
        self.__setting_is_enabled = False
        self.__assistant_booting = False
        self.__timer = 0
        self.__L_img_boot_gui = []
        self.__L_img_load_gui = []
        self.__D_img_speak_gui = {}
        self.__dir_gui_dark = "asset/GUI/dark/"
        self.__dir_gui_light = "asset/GUI/light/"
        self.__index_load = 0
        self.__version = version

        # Liste de widget
        self.__L_btn_tableur_normal = []
        self.__L_btn_word_normal = []
        self.__L_btn_project_normal = []

        # Recuperation des cerveau
        self.__six_brain = six_brain
        self.__ryley_brain = ryley_brain

        # Recuperation gestionnaire
        self.__gestionnaire = self.__six_brain.getGestionnaire()

        # Recuperation librairy
        self.__objOS = self.__gestionnaire.getOSObjet()
        self.__arr_voice = self.__gestionnaire.getArrVoice()

        # Init des parametre de copilote
        self.__copilote_setting = copilote_setting(self.__objOS)

        # Init de la langue
        self.__copilote_language = copilote_language("json_conf/langue_copilote.json")

        # Theard
        self.__th_reflect_six = th.Thread()
        self.__th_reflect_ryley = th.Thread()
        self.__th_speak_stop = th.Thread()
        self.__th_speak = th.Thread()
        self.__th_first_boot = th.Thread()

        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))

        self.geometry("500x400+5+30")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

        # Init des parametre
        self.__gazelleUI = arrera_gazelle(self,self.__gestionnaire,"json_conf/conf-setting.json")
        self.__gazelleUI.passFNCQuit(self.__quit_setting)
        self.__gazelleUI.passFNCBTNIcon(self.__about)

        # Init de keyboad manager
        self.__key_manage = keyboad_manager(self)

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

        self.__c_speak = self.__canvas_speak_normal()

        self.__c_maj = self.__canvas_maj()

        self.__c_load = self.__canvas_load_normal()

        self.__quick_setting = quick_setting(self,self.__copilote_setting,
                                             [self.__dir_gui_light,self.__dir_gui_dark],
                                             self.__unview_quick_setting,
                                             self.__active_setting)

        self.__back_widget_normal = back_widget(self,key_gest=self.__key_manage,
                                                dirImg=[self.__dir_gui_light,self.__dir_gui_dark],
                                                img_windows_mode="icon-lttle.png",img_mode="iconRyleyCodehelp.png",
                                                dectOS=self.__objOS,
                                                fonc_speed_setting=self.__view_quick_setting,
                                                fonc_mode=lambda : print("Codehelp"),
                                                fonc_windows_mode= lambda : print("mode little"),
                                                fonc_setting=self.__active_setting,
                                                fonc_send= self.__send_on_assistants)

    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()

        self.mainloop()

    def __boot(self):
        self.__set_state_micro_sound()
        self.__assistant_booting = True
        self.__c_maj.place_forget()

        if self.__first_boot :
            self.__sequence_first_boot(1)
        else :
            self.__sequence_boot()

            if random.randint(0,1) == 0 :
                self.__sequence_speak(self.__six_brain.boot())
            else :
                self.__sequence_speak(self.__ryley_brain.boot())

        self.__update__assistant()

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

    def __canvas_speak_normal(self):
        self.__D_img_speak_gui = {"copilote":(self.__dir_gui_light+"parole_copilote.png",self.__dir_gui_dark+"parole_copilote.png"),
                                  "six":(self.__dir_gui_light+"parole_six.png",self.__dir_gui_dark+"parole_six.png"),
                                  "ryley":(self.__dir_gui_light+"parole_ryley.png",self.__dir_gui_dark+"parole_ryley.png"),
                                  "speak":(self.__dir_gui_light+"during_parole.png",self.__dir_gui_dark+"during_parole.png")}
        tableurIMG = aImage(path_dark="asset/GUI/dark/tableur.png",
                            path_light="asset/GUI/light/tableur.png", width=30, height=30)
        wordIMG = aImage(path_dark="asset/GUI/dark/word.png",
                         path_light="asset/GUI/light/word.png", width=30, height=30)
        projetrIMG = aImage(path_dark="asset/GUI/dark/projet.png",
                            path_light="asset/GUI/light/projet.png", width=30, height=30)
        l_img,d_img = self.__D_img_speak_gui["copilote"]
        c = aBackgroundImage(self,background_light=l_img,background_dark=d_img,
                             fg_color=("#ffffff","#000000"),width=500,height=350)

        self.__l_speak = aLabel(c,text="",justify="left",wraplength=455,
                                police_size=20,corner_radius=0)

        self.__L_btn_tableur_normal.append(aButton(c, width=30, height=30, text="", image=tableurIMG,
                                                   dark_color="#1f1f1f", light_color="#e0e0e0",
                                                   hover_color=("#949494", "#505050")))
        self.__L_btn_word_normal.append(aButton(c, width=30, height=30, text="", image=wordIMG,
                                                dark_color="#1f1f1f", light_color="#e0e0e0",
                                                hover_color=("#949494", "#505050")))
        self.__L_btn_project_normal.append(aButton(c, width=30, height=30, text="", image=projetrIMG,
                                                   dark_color="#1f1f1f", light_color="#e0e0e0",
                                                   hover_color=("#949494", "#505050")))

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

    def __canvas_load_normal(self):
        self.__L_img_load_gui.append((self.__dir_gui_light+"load0.png",self.__dir_gui_dark+"load0.png"))
        self.__L_img_load_gui.append((self.__dir_gui_light+"load1.png",self.__dir_gui_dark+"load1.png"))
        self.__L_img_load_gui.append((self.__dir_gui_light+"load2.png",self.__dir_gui_dark+"load2.png"))
        self.__L_img_load_gui.append((self.__dir_gui_light+"load3.png",self.__dir_gui_dark+"load3.png"))
        self.__L_img_load_gui.append((self.__dir_gui_light+"load4.png",self.__dir_gui_dark+"load4.png"))

        l_img,d_img = self.__L_img_load_gui[0]

        c = aBackgroundImage(self,background_light=l_img,
                             background_dark=d_img,
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

    def __change_img_load(self,index:int):
        if index < len(self.__L_img_load_gui):
            l_img,d_img = self.__L_img_load_gui[index]
        else :
            l_img,d_img = self.__L_img_load_gui[0]

        self.__c_load.change_background(background_light=l_img, background_dark=d_img)
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
        self.update()

    def __set_six_speak(self):
        l_img,d_img = self.__D_img_speak_gui["six"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.__l_speak.place(x=25, y=90)
        self.update()

    def __set_ryley_speak(self):
        l_img,d_img = self.__D_img_speak_gui["ryley"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.__l_speak.place(x=25, y=90)
        self.update()


    def __set_voice_speak(self):
        l_img,d_img = self.__D_img_speak_gui["speak"]

        self.__c_speak.change_background(background_light=l_img, background_dark=d_img)

        self.__l_speak.configure(fg_color=("#3b224a","#3b224a"),text_color=("#ffffff","#ffffff"))
        self.__l_speak.place(x=30, y=100)
        self.update()

    # Partie reflection de l'assistant

    def __send_on_assistants(self):
        self.focus()
        self.__assistant_speaking = True
        text = self.__back_widget_normal.get_text_entry()
        self.__back_widget_normal.clear_entry()

        if text != "":

            if "parametre" in text or "settings" in text:
                self.__active_setting()
                return

            self.__back_widget_normal.place_forget()

            self.__th_reflect_six = th.Thread(target=self.__six_brain.neuron,args=(text,))
            self.__th_reflect_ryley = th.Thread(target=self.__ryley_brain.neuron,args=(text,))
            self.__th_reflect_six.start()
            self.__th_reflect_ryley.start()

            self.__index_load = 0
            self.__change_img_load(0)
            self.__c_speak.place_forget()
            self.__c_load.place(x=0, y=0)

            self.__update_during_reflect()

    def __treatment_out_assistant(self,var_six:int,var_ryley:int,out_six:list,out_ryley:list):
        if var_six == 15 and var_ryley == 15:
            self.__on_close()
        elif var_six == 17 :
            self.__windows_help_assistant(out_six[0])
        elif var_ryley == 17:
            self.__windows_help_assistant(out_ryley[0])
        else :
            if var_ryley != 0 :
                self.__sequence_speak(out_ryley[0])
            elif var_six != 0 :
                self.__sequence_speak(out_six[0])

        self.__manage_btn_open_fnc()

    def __update__assistant(self):
        if not self.__setting_is_enabled and not self.__assistant_speaking and not self.__assistant_booting :
            self.__timer += 1
            if self.__six_brain.updateAssistant():
                varOut = self.__six_brain.getValeurSortie()
                listOut = self.__six_brain.getListSortie()
                self.__treatment_out_assistant(varOut,0,listOut,[])
            """
            elif self.__timer >= 10:
                if self.__timer == 10:
                    self.__c_speak.place_forget()
                    self.__c_emotion.place(x=0, y=0)
                self.__sequence_emotion()
            """

        self.__manage_btn_open_fnc()

        self.after(1000,self.__update__assistant)

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
        self.__assistant_booting = False

    def __sequence_speak(self,text:str):
        for btn in self.__L_btn_tableur_normal:
            btn.place_forget()
        for btn in self.__L_btn_word_normal:
            btn.place_forget()
        for btn in self.__L_btn_project_normal:
            btn.place_forget()

        self.__assistant_speaking = True
        self.__timer = 0
        self.__c_load.place_forget()
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
            self.__back_widget_normal.placeBottomCenter()
            self.__assistant_speaking = False

    def __sequence_stop(self):
        if random.randint(0,1) == 0 :
            texte_stop = self.__six_brain.shutdown()
        else :
            texte_stop = self.__ryley_brain.shutdown()

        self.__l_speak.configure(text=texte_stop)
        self.__back_widget_normal.place_forget()

        if self.__speak_is_enable:
            self.__quick_setting.unview()
            self.__c_speak.place(x=0,y=0)
            self.__th_speak_stop = th.Thread(target=self.__arr_voice.say,args=(texte_stop,))
            self.__th_speak_stop.start()
            self.__set_voice_speak()

        self.__update_during_stop()

    def __sequence_first_boot(self,nb:int):
        self.__assistant_speaking = True
        self.__timer = 0
        self.__c_load.place_forget()
        self.__c_boot.place_forget()
        self.__c_speak.place(x=0, y=0)

        texte = self.__copilote_language.get_first_boot(nb)
        self.__l_speak.configure(text=texte)

        if self.__speak_is_enable:
            self.__set_voice_speak()
            self.__th_first_boot = th.Thread(target=self.__arr_voice.say,args=(texte,))
            self.__th_first_boot.start()
            self.__update_during_first_boot(nb)
        else :
            self.__change_gui_speak()

    # Methode update

    def __update_during_speak(self):
        if self.__th_speak.is_alive():
            self.after(100,self.__update_during_speak)
        else :
            self.__th_speak = th.Thread()
            self.__change_gui_speak()
            self.__back_widget_normal.placeBottomCenter()
            self.__assistant_speaking = False

    def __update_during_reflect(self):
        if self.__th_reflect_ryley.is_alive() or self.__th_reflect_six.is_alive():
            self.after(200,self.__update_during_reflect)
            self.__index_load += 1
            self.__change_img_load(self.__index_load)
            if self.__index_load == 4 :
                self.__index_load = 0
        else :
            self.__th_reflect_ryley = th.Thread()
            self.__th_reflect_six = th.Thread()
            self.__c_load.place_forget()
            var_six = self.__six_brain.getValeurSortie()
            list_six = self.__six_brain.getListSortie()

            var_ryley = self.__ryley_brain.getValeurSortie()
            list_ryley = self.__ryley_brain.getListSortie()

            self.__treatment_out_assistant(var_six,var_ryley,
                                           list_six,list_ryley)

    def __update_during_stop(self):
        if self.__th_speak_stop.is_alive():
            self.after(100,self.__update_during_stop)
        else :
            self.__quick_setting.unview()
            self.__th_speak_stop = th.Thread()
            self.__change_gui_speak()
            time.sleep(0.2)
            self.__c_speak.place_forget()
            self.__change_img_boot(4)
            self.__c_boot.place(x=0, y=0)
            time.sleep(0.2)
            self.__change_img_boot(3)
            time.sleep(0.2)
            self.__change_img_boot(2)
            time.sleep(0.2)
            self.__change_img_boot(1)
            time.sleep(0.2)
            self.__change_img_boot(0)
            time.sleep(0.2)

            if self.__objOS.osWindows():
                os.kill(os.getpid(), signal.SIGINT)
            elif self.__objOS.osLinux() or self.__objOS.osMac():
                os.kill(os.getpid(), signal.SIGKILL)

    def __update_during_first_boot(self,nb:int):
        if self.__th_first_boot.is_alive():
            self.after(100,self.__update_during_first_boot,nb)
        else :
            self.__th_first_boot = th.Thread()
            if nb == 1 :
                time.sleep(0.2)
                self.__sequence_first_boot(2)
            else :
                time.sleep(0.2)
                if random.randint(0, 1) == 0:
                    self.__sequence_speak(self.__six_brain.boot())
                else:
                    self.__sequence_speak(self.__ryley_brain.boot())



    # Methode qui agit sur la fenetre

    def __on_close(self):
        self.__change_img_boot(4)
        self.__c_boot.place(x=0,y=0)
        self.update()
        if askyesno("Atention", "Voulez-vous vraiment fermer Arrera Copilote ?"):
            self.title(self.__nameSoft)
            # self.__gazelleUI.clearAllFrame()
            self.update()
            self.__c_boot.place_forget()
            self.__sequence_stop()
        else :
            self.__l_speak.configure(text="RETOUR") # ToDo : Mettre un petit texte
            self.__c_boot.place_forget()
            self.__change_gui_speak()
            self.__c_speak.place(x=0,y=0)
            self.__back_widget_normal.placeBottomCenter()


    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile="asset/icone/linux/icon.png",
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Arrera-Copilote",
                      linkWeb="https://arrera-software.fr/")

    def __windows_help_assistant(self,texte:str):
        winHelp = aTopLevel(width=500, height=600,title="Arrera Copilote : Aide Assistant",
                            icon=self.__emplacementIcon)
        labelTitleHelp = aLabel(winHelp, police_size=25,text="Copilote - Aide")
        aideView = aText(winHelp, width=475, height=500,wrap="word",police_size=20)

        self.__sequence_speak("Aide") # Todo : Mettre une vrai phrase

        aideView.insert_text(texte)
        labelTitleHelp.placeTopCenter()
        aideView.placeCenter()

    # Methode des parametres

    def __active_setting(self):
        self.__setting_is_enabled = True
        self.__quick_setting.unview()
        self.__c_load.place_forget()
        self.__back_widget_normal.place_forget()
        self.__c_speak.place_forget()
        self.__c_boot.place_forget()
        self.__gazelleUI.active()

    def __quit_setting(self):
        self.__gazelleUI.clearAllFrame()
        self.__sequence_speak(self.__copilote_language.get_ph_setting())
        self.__setting_is_enabled = False
        self.__timer = 0

    # Methode des bouton

    def __view_quick_setting(self):
        self.__timer = 0
        self.__c_load.place_forget()
        self.__c_speak.place_forget()
        self.__c_boot.place_forget()
        self.__back_widget_normal.place_forget()
        self.__quick_setting.view_normal()

    def __unview_quick_setting(self):
        self.__timer = 0
        self.__quick_setting.unview()
        self.__c_load.place_forget()
        self.__c_speak.place(x=0,y=0)
        self.__c_boot.place_forget()
        self.__back_widget_normal.placeBottomCenter()
        self.__set_state_micro_sound()

    def __set_state_micro_sound(self):
        self.__speak_is_enable = self.__copilote_setting.get_sound()
        self.__micro_is_enable = self.__copilote_setting.get_micophone()

    def __manage_btn_open_fnc(self):
        if self.__six_brain.getTableur() :
            for btn in self.__L_btn_tableur_normal:
                btn.placeBottomRight()
        else :
            for btn in self.__L_btn_tableur_normal:
                btn.place_forget()

        if self.__six_brain.getWord():
            for btn in self.__L_btn_word_normal:
                btn.placeBottomLeft()
        else :
            for btn in self.__L_btn_word_normal:
                btn.place_forget()

        if self.__six_brain.getProject():
            for btn in self.__L_btn_project_normal:
                btn.placeBottomCenter()
        else :
            for btn in self.__L_btn_project_normal:
                btn.place_forget()