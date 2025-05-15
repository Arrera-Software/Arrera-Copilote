import platform

class OS :
    def __init__(self) :
        self.__os = platform.system()
        
    def osWindows(self):
        if self.__os == "Windows":
           return True
        else :
            return False
    
    def osLinux(self):
        if self.__os == "Linux":
            return True
        else :
            return False
                