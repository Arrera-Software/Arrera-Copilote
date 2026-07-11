from librairy.arrera_tk import *
from librairy.dectectionOS import OS
from src.copilote_setting import copilote_setting
from gestionnaire.gestion import gestionnaire
from librairy.arrera_voice import CArreraVoice
from src.copilote_micro import copilote_micro

class back_widget(aFrame):
    def __init__(self, master:aTk,assistant_gest:gestionnaire, key_gest:keyboad_manager,
                 dirImg:list, img_windows_mode:str,
                 img_mode:str, dectOS:OS, fonc_speed_setting:Callable,
                 fonc_mode:Callable, fonc_windows_mode:Callable,
                 fonc_send:Callable,arr_voice:CArreraVoice,use_trigger:bool=False):
        super().__init__(master,width=500,height=50)

        self.__l_dir = dirImg[0]
        self.__d_dir = dirImg[1]

        self.__master = master

        self.__assistant_gest = assistant_gest


        user = self.__entry_btn(img_mode,img_windows_mode)

        img_setting = aImage(width=30,height=30,path_light=self.__l_dir+"settings.png",path_dark=self.__d_dir+"settings.png")
        self.__btn_micro = copilote_micro(self,arr_voice=arr_voice,
                                            back_widget=self,
                                            fnc_send=fonc_send,
                                            use_trigger=use_trigger)

        img_speed_setting = aImage(width=30,height=30,path_light=self.__l_dir+"speed_setting.png",path_dark=self.__d_dir+"speed_setting.png")
        self.__btn_speed_setting = aButton(self, text="", image=img_speed_setting, width=30, height=30)

        self.__btn_micro.placeLeftCenter()
        self.__btn_speed_setting.placeRightCenter()

        # Application comportement entry

        self.__entry.bind("<FocusIn>", self.__on_focus)
        self.__entry.bind("<FocusOut>", self.__reset_focus)

        if dectOS.osWindows():
            key_gest.add_key(27,lambda : master.focus())
            key_gest.add_key(13, fonc_send)
        elif dectOS.osLinux():
            key_gest.add_key(9,lambda : master.focus())
            key_gest.add_key(36, fonc_send)
        elif dectOS.osMac():
            key_gest.add_key(889192475,lambda : master.focus())
            key_gest.add_key(603979789, fonc_send)

        # Mise en place fonction dans les BTN

        self.__btn_speed_setting.configure(command=fonc_speed_setting)
        self.__btn_mode.configure(command=fonc_mode)
        self.__btn_windows_mode.configure(command=fonc_windows_mode)

        user.placeCenter()

    def __entry_btn(self,img_mode:str,img_windows_mode:str):
        f = aFrame(self,width=350,height=50)
        self.__entry = aEntry(f,width=200,police_size=20)

        img= aImage(width=30, height=30, path_light=self.__l_dir + img_windows_mode, path_dark=self.__d_dir + img_windows_mode)
        self.__btn_windows_mode = aButton(f, text="", image=img, width=30, height=30)

        img2 = aImage(width=30, height=30, path_light=self.__l_dir + img_mode, path_dark=self.__d_dir + img_mode)
        self.__btn_mode = aButton(f, text="", image=img2, width=30, height=30)

        self.__entry.placeBottomCenterNoStick()
        self.__btn_windows_mode.placeRightBottomNoStick()
        self.__btn_mode.placeLeftBottomNoStick()

        return f

    def __on_focus(self, event):
        # Agrandir l'entry
        self.__entry.configure(width=325)
        self.__entry.placeBottomCenterNoStick()

        # Afficher les boutons
        self.__btn_mode.place_forget()
        self.__btn_windows_mode.place_forget()


    def __reset_focus(self, event=None):
        # Rétrécir l'entry
        self.__entry.configure(width=200)

        # Cacher les boutons
        self.__entry.placeBottomCenterNoStick()
        self.__btn_windows_mode.placeRightBottomNoStick()
        self.__btn_mode.placeLeftBottomNoStick()

        # Retirer le focus de l'entry
        self.__master.focus()

    def get_text_entry(self):
        return self.__assistant_gest.netoyageChaine(self.__entry.get().lower())

    def clear_entry(self):
        self.__entry.delete(0,END)

    def insert_text(self,text:str):
        self.__entry.insert(0,text)

    def get_btn_micro(self):
        return self.__btn_micro

class quick_setting(aFrame):
    def __init__(self,master:aTk,setting:copilote_setting,list_dir:list,fonc_close:Callable,fonc_setting:Callable):
        super().__init__(master)

        self.__little_mode = False

        self.__l_dir = list_dir[0]
        self.__d_dir = list_dir[1]
        
        self.__copilote_setting = setting
        
        self.__L_img_sound_normal = []

        img_setting = aImage(width=70, height=70, path_light=self.__l_dir + "settings.png",
                             path_dark=self.__d_dir + "settings.png")

        self.__l_title = aLabel(self,text="Paramètre rapide copilote",justify="center")

        self.__btn_sound = aButton(self,text="",
                                   command=self.__change_sound)

        self.__btn_close = aButton(self,text="Fermer",size=25,command=fonc_close)
        self.__btn_setting = aButton(self,text="",command=fonc_setting)

        self.__create_widget()

    def view(self):
        self.place(x=0,y=0)

    def unview(self):
        self.place_forget()
    
    def __create_widget(self):
        self.configure(width=500,height=400)

        self.__l_title.configure(font=("Roboto",30,"bold"))
        self.__l_title.placeTopCenter()

        self.__L_img_sound_normal = [aImage(width=70,height=70,
                                            path_light=self.__l_dir+"sound_disable.png",
                                            path_dark=self.__d_dir+"sound_disable.png"),
                                     aImage(width=70,height=70,
                                            path_light=self.__l_dir+"sound_enable.png",
                                            path_dark=self.__d_dir+"sound_enable.png")]

        self.__L_img_sound_little = [aImage(width=30,height=30,
                                            path_light=self.__l_dir+"sound_disable.png",
                                            path_dark=self.__d_dir+"sound_disable.png"),
                                     aImage(width=30,height=30,
                                            path_light=self.__l_dir+"sound_enable.png",
                                            path_dark=self.__d_dir+"sound_enable.png")]

        self.__l_img_setting = [aImage(width=70, height=70, path_light=self.__l_dir + "settings.png",
                             path_dark=self.__d_dir + "settings.png"),
                                aImage(width=30, height=30, path_light=self.__l_dir + "settings.png",
                                       path_dark=self.__d_dir + "settings.png")]


        self.__btn_sound.configure(width=70,height=70)
        self.__btn_setting.configure(width=70, height=70)

        self.__btn_setting.placeLeftCenter()
        self.__btn_sound.placeRightCenter()

        self.__btn_close.placeBottomCenter()

        self.__set_state_btn()

    def __set_state_btn(self):
        if not self.__little_mode :
            if self.__copilote_setting.get_sound():
                self.__btn_sound.configure(image=self.__L_img_sound_normal[0])
            else :
                self.__btn_sound.configure(image=self.__L_img_sound_normal[1])
        else :
            if self.__copilote_setting.get_sound():
                self.__btn_sound.configure(image=self.__L_img_sound_little[0])
            else :
                self.__btn_sound.configure(image=self.__L_img_sound_little[1])


    def __change_sound(self):
        if self.__copilote_setting.get_sound():
            self.__copilote_setting.set_sound(False)
        else :
            self.__copilote_setting.set_sound(True)

        self.__set_state_btn()

    def mode_little(self):
        self.__l_title.configure(font=("Roboto",15,"bold"))
        self.configure(width=500,height=120)
        self.__btn_sound.configure(width=30,height=30)
        self.__btn_setting.configure(width=30, height=30,
                                     text="",image=self.__l_img_setting[1])

        self.__btn_setting.placeCenterLeft()
        self.__btn_sound.placeCenterRight()

        self.__btn_close.place_forget()

        self.__btn_close.placeBottomCenter()

        self.__btn_close.configure(font=("Roboto",13,"normal"))

        self.__little_mode = True
        self.__set_state_btn()

    def mode_normal(self):
        self.__l_title.configure(font=("Roboto",30,"bold"))
        self.__l_title.placeTopCenter()
        self.configure(width=500,height=400)
        self.__btn_sound.configure(width=70,height=70)
        self.__btn_setting.configure(width=70, height=70,
                                     text="", image=self.__l_img_setting[0])

        self.__btn_close.configure(font=("Roboto",25,"bold"))

        self.__btn_setting.placeLeftCenter()
        self.__btn_sound.placeRightCenter()
        self.__btn_close.placeBottomCenter()

        self.__little_mode = False
        self.__set_state_btn()