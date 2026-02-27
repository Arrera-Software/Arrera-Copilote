from librairy.travailJSON import *
from librairy.dectectionOS import OS
import os

DICTBASE = {"sound":1,
            "microphone":0}

class copilote_setting:
    def __init__(self,objOs:OS):
        self.__osDect = objOs

        if self.__osDect.osLinux() or self.__osDect.osMac():
            self.__copiloteSettingFile = str(os.path.expanduser("~")) + "/.config/arrera-assistant/copilote-config.json"
        elif self.__osDect.osWindows():
            self.__copiloteSettingFile = (str(os.path.join(os.path.expanduser("~"), "AppData", "Roaming")) +
                                          "/arrera-assistant/copilote-config.json")
        else :
            self.__copiloteSettingFile = None

        if not os.path.isfile(self.__copiloteSettingFile):
            os.makedirs(os.path.dirname(self.__copiloteSettingFile), exist_ok=True)
            with open(self.__copiloteSettingFile, "x", encoding="utf-8") as f:
                json.dump(DICTBASE, f, ensure_ascii=False, indent=2)

        self.__file_setting = jsonWork(self.__copiloteSettingFile)

    def get_sound(self):
        return int(self.__file_setting.getContentJsonFlag("sound"))

    def get_micophone(self):
        return int(self.__file_setting.getContentJsonFlag("microphone"))

    def set_sound(self,value:bool):
        if value:
            return self.__file_setting.setValeurJson("sound",1)
        else:
            return self.__file_setting.setValeurJson("sound",0)

    def set_microphone(self,value:bool):
        if value:
            return self.__file_setting.setValeurJson("microphone",1)
        else:
            return self.__file_setting.setValeurJson("microphone",0)