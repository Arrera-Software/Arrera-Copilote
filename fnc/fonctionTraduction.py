from fnc.fncBase import fncBase,gestionnaire
from translate import Translator

class fncTraduction(fncBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__traducteur = None

    def getLang(self):
        return ["anglais", "francais", "espagnol", "allemand", "chinois simplifie", "chinois traditionnel",
                     "arabe", "russe", "japonais", "coreen", "italien", "portugais", "neerlandais",
                     "suedois", "danois", "norvegien", "finnois", "grec", "hebreu", "indonesien"]

    def getLangCode(self):
        return ["en", "fr", "es", "de", "zh-CN",
                    "zh-TW","ar","ru","ja",
                   "ko", "it","pt","nl","sv",
                   "da","no","fi","el","he","id"]

    def getLangAndLangCode(self):
        return {"anglais": "en", "francais": "fr", "espagnol": "es", "allemand": "de", "chinois simplifie": "zh-CN",
                    "chinois traditionnel": "zh-TW", "arabe": "ar", "russe": "ru", "japonais": "ja",
                    "coreen": "ko", "italien": "it", "portugais": "pt", "neerlandais": "nl", "suedois": "sv",
                    "danois": "da", "norvegien": "no", "finnois": "fi", "grec": "el", "hebreu": "he",
                    "indonesien": "id"}

    def setTranlator(self,langInt:str,langOut:str):
        try :
            self.__traducteur = None
            self.__traducteur = Translator(to_lang=langInt,from_lang=langOut)
            return True
        except Exception as e:
            return False

    def tranlate(self,texte:str):
        if self.__traducteur is not None:
            try:
                return self.__traducteur.translate(texte)
            except Exception as e:
                return None
        else:
            return None