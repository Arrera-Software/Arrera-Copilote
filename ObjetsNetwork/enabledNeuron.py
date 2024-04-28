from librairy.travailJSON import*

class GestArreraNeuron :
    def __init__(self,configNeuron:jsonWork) -> None:
        self.__etatService = configNeuron.lectureJSON("etatService")
        self.__etatSoftware = configNeuron.lectureJSON("etatSoftware")
        self.__etatTime = configNeuron.lectureJSON("etatTime")
        self.__etatOpen = configNeuron.lectureJSON("etatOpen")
        self.__etatSearch = configNeuron.lectureJSON("etatSearch")
        self.__etatChatbot = configNeuron.lectureJSON("etatChatbot")
        self.__etatApi = configNeuron.lectureJSON("etatApi")
        
    def getService(self):
        if self.__etatService == "1" :
            return True
        else :
            return False

    def getSoftware(self):
        if self.__etatSoftware == "1" :
            return True
        else :
            return False

    def getTime(self):
        if self.__etatTime == "1" :
            return True
        else :
            return False
    
    def getOpen(self):
        if self.__etatOpen =="1" :
            return True
        else :
            return False
    
    def getSearch(self):
        if self.__etatSearch == "1" :
            return True
        else :
            return False
    
    def getChatbot(self):
        if self.__etatChatbot == "1" :
            return True
        else :
            return False
    
    def getAPI(self):
        if self.__etatApi == "1" :
            return True
        else :
            return False