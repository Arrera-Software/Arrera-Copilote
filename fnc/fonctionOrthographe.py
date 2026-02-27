from fnc.fncBase import fncBase,gestionnaire
from spellchecker import SpellChecker
import pyperclip

class fncOrthographe(fncBase):
    def __init__(self,gestionnaire:gestionnaire,language='fr'):
        super().__init__(gestionnaire)
        self.__toolLaunched = False
        try :
            self.__tool = SpellChecker(language=language)
            self.__toolLaunched = True
        except Exception as e:
            self.__toolLaunched = False
        self.__correctedText = None
        self.__mots = None
        self.__matches = None
    
    def check(self, texte:str):
        if not texte:
            return False
        if not self.__toolLaunched:
            return False

        try :
            self.__mots = texte.split()
            self.__matches = self.__tool.unknown(self.__mots)
            return True
        except Exception as e:
            return False

    def getMotsIncorrects(self):
        if self.__matches is None:
            return None
        if not self.__toolLaunched:
            return None
        return list(self.__matches)
    
    def correctionText(self):
        if self.__matches is None:
            return False
        if not self.__toolLaunched:
            return False

        try:
            self.__correctedText = ' '.join([self.__tool.correction(mot) if mot in self.__matches else mot for mot in self.__mots])
            return True
        except Exception as e:
            return False

    def getCorrections(self):
        return self.__correctedText

    def copyCorrections(self):
        if not self.__toolLaunched:
            return False
        if self.__correctedText is None:
            return False
        try :
            pyperclip.copy(self.__correctedText)
            return True
        except Exception as e:
            return False

    def getToolLaunched(self):
        return self.__toolLaunched