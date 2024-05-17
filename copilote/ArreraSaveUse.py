from librairy.travailJSON import*

class CArreraSaveUse :
    def __init__(self,file:str):
        self.__fileSave = jsonWork(file)
    
    def setTableurOpen(self,open:bool):
        if(open==True):
            self.__fileSave.EcritureJSON("tableurOpen","1")
        else :
            self.__fileSave.EcritureJSON("tableurOpen","0")
    
    def setDocumentOpen(self,open:bool):
        if(open==True):
            self.__fileSave.EcritureJSON("documentOpen","1")
        else :
            self.__fileSave.EcritureJSON("documentOpen","0")
    
    def setDocumentEmplacement(self,emplacement:str):
        self.__fileSave.EcritureJSON("documentEmplacement",emplacement)
    
    def setTableurEmplacement(self,emplacement:str):
        self.__fileSave.EcritureJSON("TableurEmplacement",emplacement)

    def getTableurOpen(self):
        if (self.__fileSave.lectureJSON("tableurOpen")=="1"):
            return True
        else :
            return False
    
    def getDocumentOpen(self):
        if (self.__fileSave.lectureJSON("documentOpen")=="1"):
            return True
        else :
            return False
    
    def getDocumentEmplacement(self):
        return self.__fileSave.lectureJSON("documentEmplacement")
    
    def getTableurEmplacement(self):
        return self.__fileSave.lectureJSON("TableurEmplacement")