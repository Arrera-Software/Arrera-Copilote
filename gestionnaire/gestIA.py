from gestionnaire.gestion import gestionnaire
from librairy.ArreraIALoad import ArreraIALoad
from librairy.model_downloader import *

class gestIA :
    def __init__(self,gestionnaire:gestionnaire):

        self.__gestionnaire =  gestionnaire

        self.__ia_mode_enabled = False
        self.__ia_loader = None

        self.__reponse_ia = ""

        self.__model_reponse_ok = False

        self.__downloader_model = model_downloader()

    def loadIA(self):
        user_conf = self.__gestionnaire.getUserConf()
        model_name = user_conf.get_ia_model()

        if user_conf.get_use_ia() == 1 and model_name !="":
            try :
                if model_name in self.get_list_model_download():
                    self.__ia_loader= ArreraIALoad()
                    self.__ia_loader.load_model_gguf(model_path=self.__downloader_model.get_path_model(model_name)
                                                     ,n_ctx=8192)
                    if self.__ia_loader.load_help_file("config/ia_instruction.txt"):
                        self.__ia_mode_enabled = True
                        return True
                    else :
                        return False
                else :
                    self.__ia_mode_enabled = False
                    return False
            except Exception as e :
                # print(e)
                self.__ia_mode_enabled = False
                return False
        else :
            self.__ia_mode_enabled = False
            return False

    def send_request_ia(self,requette:str):
        if self.__ia_mode_enabled:
            try :
                self.__reponse_ia = self.__ia_loader.send_request(requette)
                self.__model_reponse_ok = True
                return True
            except Exception as e :
                self.__model_reponse_ok = False
                print(e)
                return False
        else :
            self.__model_reponse_ok = False
            return False

    def get_state_ia_reponse(self):
        return self.__model_reponse_ok

    def get_reponse_ia(self):
        return self.__reponse_ia

    def get_ia_is_enable(self):
        return self.__ia_mode_enabled

    def get_list_model_available(self):
        return self.__downloader_model.get_model_list()

    def gest_data_model(self,model:str):
        if model in self.get_list_model_available():
            return self.__downloader_model.get_data_model(model)
        else :
            return None,None,None

    def get_list_model_download(self):
        return self.__downloader_model.get_model_download()

    def download_model(self,model:str):
        return self.__downloader_model.download_model(model)