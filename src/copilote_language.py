from librairy.travailJSON import *

class copilote_language :
    def __init__(self, dir_lang_copilote:str):
        self.__f_copilote = jsonWork(dir_lang_copilote)

    def get_first_boot(self,nb:int):
        return self.__f_copilote.getContentJsonFlag(str(nb))

    def get_ph_setting(self):
        return self.__f_copilote.getContentJsonFlag("setting_close")

    def get_ph_help(self):
        return self.__f_copilote.getContentJsonFlag("aide")

    def get_ph_windows_mode(self,nb:int):
        return self.__f_copilote.getContentJsonFlag("windows"+str(nb))

    def get_ph_cancel_close(self):
        return self.__f_copilote.getContentJsonFlag("cancel_close")

    def get_ph_error(self,nb:int):
        return self.__f_copilote.getContentJsonFlag("error"+str(nb))