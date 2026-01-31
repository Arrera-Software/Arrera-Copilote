import subprocess
import os
from librairy.dectectionOS import *

class OpenSoftware :
    def __init__(self):
        detecteurOS = OS()
        self.__windowsOS = detecteurOS.osWindows()
        self.__linuxOS = detecteurOS.osLinux()
        self.__macOS = detecteurOS.osMac()
        self.__emplacement = ""
        self.__etat = bool
    
    def setLocation(self, name:str) ->bool:
        if name == "":
            self.__etat = False
        elif self.__windowsOS == True and self.__linuxOS == False and self.__macOS == False:
            self.__emplacement = name
            self.__etat = True
        elif self.__windowsOS == False and self.__linuxOS == True and self.__macOS == False :
                self.__emplacement = name
                self.__etat = True
        elif self.__windowsOS == False and self.__linuxOS == False and self.__macOS == True:
            self.__emplacement = name
            self.__etat = True
        else :
            self.__etat = False
        return self.__etat
               
    def open(self):
        if not self.__etat and self.__emplacement == "":
            return False

        # LINUX
        elif self.__linuxOS:
            try :
                subprocess.Popen([self.__emplacement],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            except Exception as e:
                # print(f"Error opening software: {e}")
                return False

        # WINDOWS
        elif self.__windowsOS:
            try:
                os.startfile(self.__emplacement)
                return True
            except Exception as e:
                # print(f"Error opening software: {e}")
                return False

        # macOS
        elif self.__macOS:
            try:
                subprocess.Popen(["open", self.__emplacement])
                return True
            except Exception as e:
                # print(f"Error opening software: {e}")
                return False
        else :
            return False