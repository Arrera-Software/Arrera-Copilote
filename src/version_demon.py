from dataclasses import dataclass
import requests


# Class de conf
@dataclass
class soft_config:
    name_soft : str
    version : str

# Class du demon qui teste la versio
class demon :
    def __init__(self,conf:soft_config,url:str):
        # Teste internet
        try:
            requests.get("https://www.google.com/", timeout=5)
            self.__internet = True
        except requests.RequestException:
            self.__internet = False
        # Variable
        self.__nameSoft = conf.name_soft
        self.__version = conf.version
        self.__url = url
        # load depots
        self.__dictSofts = {}
        self.__state_depots = self.load_depots()


    # Gestion du fichier de depots
    def load_depots(self):
        if self.__internet:
            try :
                response = requests.get(self.__url)
                response.raise_for_status()
                self.__dictSofts = response.json()[self.__nameSoft]
                return True
            except :
                return False
        else :
            return False


    def checkUpdate(self):
        if self.__internet and self.__state_depots:
            if self.__version != "IXXXX-XXX":
                versionOnline = self.__dictSofts["version"]
                if self.__version != versionOnline:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def getVersionSoft(self):
        return self.__version

    def getInternet(self):
        return self.__internet