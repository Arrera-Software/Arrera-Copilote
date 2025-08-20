from librairy.travailJSON import *
from pathlib import Path
from librairy.dectectionOS import *

BASECONF = {
  "theme": "light",
  "soundMicro": "1",
  "listWord": []
}

class CopiloteConf:
    def __init__(self):
        self.__osDect = OS()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = Path.home()
            self.__copiloteSettingPath = str(home) + "/.config/assistant/copilote/copilote-config.json"
        elif self.__osDect.osWindows():
            home = Path.home() / "AppData" / "Roaming"
            self.__copiloteSettingPath = str(home) + "/assistant/copilote/copilote-config.json"
        else :
            self.__copiloteSettingPath = None


        if not Path(self.__copiloteSettingPath).is_file():
            path = Path(self.__copiloteSettingPath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as f:
                json.dump(BASECONF, f, ensure_ascii=False, indent=2)

    def getRyleySettingPath(self):
        return self.__copiloteSettingPath