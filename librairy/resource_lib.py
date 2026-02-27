# Objet pour gerer les ressource sur mac os
import sys, os
from librairy.dectectionOS import OS

class resource_lib:
    def __init__(self):
        osDect = OS()
        if osDect.osLinux():
            self.__os = "linux"
        elif osDect.osMac():
            self.__os = "mac"
        elif osDect.osWindows():
            self.__os = "windows"

    def resource_path(self,relative_path:str):
        if self.__os == "mac":
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)
        else :
            return relative_path
    
    def tmp_directory(self):
        if self.__os == "linux" or self.__os == "mac":
            home = os.path.expanduser("~")
            return str(home)+"/.tmp"
        else : 
            home = os.path.expanduser("~")
            return str(home) + "/AppData/Local/tmp"