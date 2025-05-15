from ObjetsNetwork.gestion import*
import subprocess
import os

class OpenSoftware :
    def __init__(self,objetGestion:gestionNetwork):
        detecteurOS = OS()
        self.__windowsOS = detecteurOS.osWindows()
        self.__linuxOS = detecteurOS.osLinux()
        self.__emplacement = ""
        self.__etat = bool
        self.__objetGestion = objetGestion
    
    def setName(self,name:str) ->bool:
        if name == "":
            self.__etat = False
        else :
            if self.__windowsOS == True and self.__linuxOS == False :
                self.__emplacement = self.__objetGestion.getEmplacementSoftwareWindows()+"/"+name+".lnk"
                self.__etat = True
            else :
                if self.__windowsOS == False and self.__linuxOS == True : 
                        self.__emplacement = name
                        self.__etat = True
                else :
                    self.__etat = False
        return self.__etat
               
    def open(self):
        if self.__etat == False:
            return False
        else :
            if self.__windowsOS == False and self.__linuxOS == True :
                subprocess.Popen([self.__emplacement],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True 
            else :
                if self.__windowsOS == True and self.__linuxOS == False :
                    os.startfile(self.__emplacement)
                    return True
                else :
                    return False