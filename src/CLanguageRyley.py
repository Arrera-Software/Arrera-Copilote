from librairy.travailJSON import *

class CLanguageRyley :
    def __init__(self, fileLanguage:str, fileHelp:str,fileFirstBoot:str):
        self.__language = jsonWork(fileLanguage)
        self.__help = jsonWork(fileHelp)
        self.__firstBoot = jsonWork(fileFirstBoot)

    def getHelpTableur(self):
        return self.__help.lectureJSONList("tableur")

    def getHelpWord(self):
        return self.__help.lectureJSONList("word")

    def getHelpProjet(self):
        return self.__help.lectureJSONList("projet")

    def getPhOpenActu(self):
        return self.__language.lectureJSON("phOpenActu")

    def getPhErreurActu(self):
        return self.__language.lectureJSON("phErreurActu")

    def getPhErreurResumerActu(self):
        return self.__language.lectureJSON("phErreurResumer")

    def getPhResumerActu(self):
        return self.__language.lectureJSON("phResumerActu")

    def getPhResumerAgenda(self):
        return self.__language.lectureJSON("phResumerAgenda")

    def getPhResumerAll(self):
        return self.__language.lectureJSON("phResumerAll")

    def getPhErreurResumerAll(self):
        return self.__language.lectureJSON("phErreurResumerAll")

    def getPhOpenAideTableur(self):
        return self.__language.lectureJSON("phOpenAideTableur")

    def getPhOpenAideWord(self):
        return self.__language.lectureJSON("phOpenAideWord")

    def getPhOpenAideFichier(self):
        return self.__language.lectureJSON("phOpenAideFichier")

    def getPhOpenAideRadio(self):
        return self.__language.lectureJSON("phOpenAideRadio")

    def getPhOpenAideProjet(self):
        return self.__language.lectureJSON("phOpenAideProjet")

    def getPhOpenAideWork(self):
        return self.__language.lectureJSON("phOpenAideWork")

    def getPhReadWord(self):
        return self.__language.lectureJSON("phReadWord")

    def getPhReadTableur(self):
        return self.__language.lectureJSON("phReadTableur")

    def getPhParametre(self):
        return self.__language.lectureJSON("phParametre")

    def getFirstBoot(self,nb:int):
        return self.__firstBoot.lectureJSON(str(nb))

    def getPhActiveCodehelp(self):
        return self.__language.lectureJSON("phActiveCodehelp")

    def getPhActiveModeLitle(self):
        return self.__language.lectureJSON("phActiveModeLitle")

    def getPhActiveModeNormal(self):
        return self.__language.lectureJSON("phActiveModeNormal")

