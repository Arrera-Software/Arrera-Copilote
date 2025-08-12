from librairy.travailJSON import *
from pathlib import Path
from librairy.dectectionOS import *


DICTUSER = {
    "user":"",
    "genre":"",
    "listVille":[""],
    "lieuDomicile":"",
    "lieuTravail":"",
    "adresseDomicile" : "",
    "adresseTravail":"",
    "dictSoftWindows" :{},
    "dictSoftLinux" :{},
    "dictSite":{},
    "moteurRecherche":"",
    "tokenGithub":"",
    "wordFolder":"",
    "videoDownloadFolder":""
}

class userConf:
    def __init__(self):
        self.__osDect = OS()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = Path.home()
            self.__userSettingPath = str(home)+"/.config/assistant/user-config.json"
            self.__userTaskPath = str(home)+"/.config/assistant/user-task.json"
            self.__userHistoriquePath = str(home)+"/.config/assistant/user-hist.json"
            self.__userEventPath = str(home)+"/.config/assistant/user-event.json"
        elif self.__osDect.osWindows():
            home = Path.home() / "AppData" / "Roaming"
            self.__userSettingPath = str(home)+"/assistant/user-config.json"
            self.__userTaskPath = str(home)+"/assistant/user-task.json"
            self.__userHistoriquePath = str(home)+"/assistant/user-hist.json"
            self.__userEventPath = str(home)+"/assistant/user-event.json"
        else :
            self.__userSettingPath = None


        # Teste si le fichier de configuration utilisateur existe
        if not Path(self.__userSettingPath).is_file():
            path = Path(self.__userSettingPath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as f:
                json.dump(DICTUSER, f, ensure_ascii=False, indent=2)

            path = Path(self.__userTaskPath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            path = Path(self.__userHistoriquePath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            path = Path(self.__userEventPath)
            with path.open("x", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            self.__firstRun = True

        # Chargement du fichier de configuration utilisateur
        self.__fileUser = jsonWork(self.__userSettingPath)

    def getFirstRun(self):
        return self.__firstRun

    def getUserSettingPath(self):
        return self.__userSettingPath

    def getTaskPath(self):
        return self.__userTaskPath

    def getEventPath(self):
        return self.__userEventPath

    def getHistoriquePath(self):
        return self.__userHistoriquePath