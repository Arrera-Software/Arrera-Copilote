from playsound3 import playsound as pl
from gestionnaire.gestion import gestionnaire
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from librairy.resource_lib import resource_lib


class CArreraVoice:
    def __init__(self,gestionnaire:gestionnaire):
        self.__gestionnaire = gestionnaire
        self.__emplacementSoundMicro = ""
        self.__soundMicro = True
        self.__listWord = []
        self.__nbWord = 0
        self.__outPutText = ""
        self.__resource_lib = resource_lib()

        if self.__gestionnaire.getNetworkObjet().getEtatInternet():
            self.__tts = None
            if not os.path.exists(self.__resource_lib.tmp_directory()):
                os.makedirs(self.__resource_lib.tmp_directory())
        else:
            self.__tts = pyttsx3.init()
            for voice in self.__tts.getProperty('voices'):
                if "french" in voice.name.lower() or "fr" in voice.id.lower():
                    voice_id = voice.id
                    self.__tts.setProperty('voice', voice_id)
                    break
            self.__tts.setProperty('rate', 150)

    def loadConfig(self):
        self.__emplacementSoundMicro = self.__gestionnaire.getConfigFile().asset+"sound/micro.mp3"
        if self.__gestionnaire.getUserConf().getSoundMicro():
            self.__soundMicro = True
        else:
            self.__soundMicro = False
        self.__listWord = self.__gestionnaire.getUserConf().getListWord()
        self.__nbWord = len(self.__listWord)

    def say(self,text:str):
        if self.__gestionnaire.getNetworkObjet().getEtatInternet():
            try :
                tts = gTTS(text=text, lang='fr', slow=False)
                if os.path.exists(self.__resource_lib.tmp_directory()+"/voice.mp3"):
                    os.remove(self.__resource_lib.tmp_directory()+"/voice.mp3")

                tts.save(self.__resource_lib.tmp_directory()+"/voice.mp3")

                pl(self.__resource_lib.tmp_directory()+"/voice.mp3")

                os.remove(self.__resource_lib.tmp_directory()+"/voice.mp3")
                return True
            except:
                return False
        else:
            try :
                self.__tts.say(text)
                self.__tts.runAndWait()
                return True
            except:
                return False

    def playFile(self,file:str):
        pl(file)

    def listen(self):
        self.loadConfig()
        if self.__soundMicro:
            pl(self.__emplacementSoundMicro)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            self.__outPutText = text
            return 0
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2

    def getTextMicro(self):
        return self.__outPutText

    def getNbWord(self):
        return self.__nbWord

    def trigerWord(self):
        self.loadConfig()
        if self.__nbWord == 0:
            return -3
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            for word in self.__listWord:
                if word in text:
                    return 1
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2
        return 0