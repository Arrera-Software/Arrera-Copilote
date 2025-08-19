from playsound3 import playsound as pl
from pyttslib import TextToSpeech
from ObjetsNetwork.network import *
from librairy.travailJSON import jsonWork
import speech_recognition as sr
import os
import sys
import platform
import subprocess


class CArreraVoice:
    def __init__(self,config:str,microFile:str):
        self.__configFile = jsonWork(self.__resource_path(config))
        self.__emplacementSoundMicro = self.__resource_path(microFile)
        self.__soundMicro = True
        self.__listWord = []
        self.__nbWord = 0
        self.__outPutText = ""
        self.loadConfig()

        if network().getEtatInternet():
            self.__tts = TextToSpeech(engine="google")
            self.__tts.set_voice("fr")
        else:
            self.__tts = TextToSpeech(engine="pyttsx3",engine_config={
                "rate": 150,    # Words per minute
                "volume": 0.8,  # Volume level (0.0 to 1.0)
            })
            self.__tts.set_voice("French (France)")

    def __resource_path(self, relative_path):
        if platform.system() == "Darwin":
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)
        else:
            return relative_path

    def loadConfig(self):
        if (self.__configFile.lectureJSON("soundMicro") == "1" ):
            self.__soundMicro = True
        else:
            self.__soundMicro = False
        self.__listWord = self.__configFile.lectureJSONList("listWord")
        self.__nbWord = len(self.__listWord)

    def say(self,text:str):
        self.__tts.speak(text)

    def playFile(self,file:str):
        if platform.system() == "Darwin":
            try :
                subprocess.run(["afplay", self.__resource_path(file)], check=True)
                return True
            except subprocess.CalledProcessError as e:
                return False
                #print(f"Error playing sound file: {e}")
        else :
            try :
                pl(file)
                return True
            except Exception as e:
                #print(f"Error playing sound file: {e}")
                return False

    def listen(self):
        if self.__soundMicro:
            self.playFile(self.__emplacementSoundMicro)

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