from librairy.travailJSON import *

class CLanguageCopilote :
    def __init__(self, languageCopilote:str,languageSix:str,fileHelp:str, fileFirstBoot:str, fileUser:str):
        self.__languageCopilote = jsonWork(languageCopilote)
        self.__languageSix = jsonWork(languageSix)
        self.__help = jsonWork(fileHelp)
        self.__firstBoot = jsonWork(fileFirstBoot)
        self.__jsonUser = jsonWork(fileUser)

    def getHelpTableur(self):
        return self.__help.lectureJSONList("tableur")

    def getHelpWord(self):
        return self.__help.lectureJSONList("word")

    def getHelpProjet(self):
        return self.__help.lectureJSONList("projet")

    def getPhOpenActu(self):
        return self.__languageCopilote.lectureJSON("phOpenActu")

    def getPhErreurActu(self):
        return self.__languageCopilote.lectureJSON("phErreurActu")

    def getPhErreurResumerActu(self):
        return self.__languageCopilote.lectureJSON("phErreurResumer")

    def getPhResumerActu(self):
        return self.__languageCopilote.lectureJSON("phResumerActu")

    def getPhResumerAgenda(self):
        return self.__languageCopilote.lectureJSON("phResumerAgenda")

    def getPhResumerAll(self):
        return self.__languageCopilote.lectureJSON("phResumerAll")

    def getPhErreurResumerAll(self):
        return self.__languageCopilote.lectureJSON("phErreurResumerAll")

    def getPhOpenAideTableur(self):
        return self.__languageCopilote.lectureJSON("phOpenAideTableur")

    def getPhOpenAideWord(self):
        return self.__languageCopilote.lectureJSON("phOpenAideWord")

    def getPhOpenAideFichier(self):
        return self.__languageCopilote.lectureJSON("phOpenAideFichier")

    def getPhOpenAideRadio(self):
        return self.__languageCopilote.lectureJSON("phOpenAideRadio")

    def getPhOpenAideProjet(self):
        return self.__languageCopilote.lectureJSON("phOpenAideProjet")

    def getPhOpenAideWork(self):
        return self.__languageCopilote.lectureJSON("phOpenAideWork")

    def getPhReadWord(self):
        return self.__languageCopilote.lectureJSON("phReadWord")

    def getPhReadTableur(self):
        return self.__languageCopilote.lectureJSON("phReadTableur")

    def getPhParametre(self):
        return self.__languageCopilote.lectureJSON("phParametre")

    def getFirstBoot(self,nb:int):
        return self.__firstBoot.lectureJSON(str(nb))

    def getPhActiveCodehelp(self):
        return self.__languageCopilote.lectureJSON("phActiveCodehelp")

    def getPhActiveModeLitleRyley(self):
        return self.__languageCopilote.lectureJSON("phActiveModeLittleRyley")

    def getPhActiveModelitleSix(self):
        return self.__languageCopilote.lectureJSON("phActiveModeLittleSix").format(genre=self.__jsonUser.lectureJSON("genre"))

    def getPhActiveModeNormalRyley(self):
        return self.__languageCopilote.lectureJSON("phActiveModeNormalRyley")

    def getPhActiveModeNormalSix(self):
        return self.__languageCopilote.lectureJSON("phActiveModeNormalSix").format(genre=self.__jsonUser.lectureJSON("genre"))

    def getPhActiveSound(self):
        return  self.__languageSix.lectureJSON("phActiveSound").format(genre=self.__jsonUser.lectureJSON("genre"))

    def getPhActiveSoundLitle(self):
        return  self.__languageSix.lectureJSON("phActiveSoundLitle").format(genre=self.__jsonUser.lectureJSON("genre"))

    def getPhDesactiveSound(self,nb:int):
        return  self.__languageSix.lectureJSON("phDisableSound" + str(nb)).format(genre=self.__jsonUser.lectureJSON("genre"), nb=nb)