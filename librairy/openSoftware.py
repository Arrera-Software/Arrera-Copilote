from ObjetsNetwork.gestion import*
import subprocess
import os

class OpenSoftware :
    def __init__(self,objetGestion:gestionNetwork):
        detecteurOS = OS()
        self.__windowsOS = detecteurOS.osWindows()
        self.__linuxOS = detecteurOS.osLinux()
        self.__macOS = detecteurOS.osMac()
        self.__emplacement = ""
        self.__etat = bool
        self.__objetGestion = objetGestion
    
    def setName(self,name:str) ->bool:
        if name == "":
            self.__etat = False
        elif self.__windowsOS == True and self.__linuxOS == False and self.__macOS == False:
            self.__emplacement = self.__objetGestion.getEmplacementSoftwareWindows()+"/"+name+".lnk"
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
        if not self.__etat:
            return False
        elif self.__windowsOS == False and self.__linuxOS == True :
            subprocess.Popen([self.__emplacement],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        elif self.__windowsOS == True and self.__linuxOS == False :
            os.startfile(self.__emplacement)
            return True
        elif self.__windowsOS == False and self.__linuxOS == False and self.__macOS == True:
            subprocess.Popen(["open", self.__emplacement])
            return True
        else :
            return False