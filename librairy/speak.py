from gtts import gTTS
import os
from playsound import playsound

class Speaking :
    def __init__(self,langue:str) :
        self.lang = langue
    
    def speak(self,texte:str):
        tts = gTTS(texte,lang=self.lang)
        tts.save("voc.mp3")
        playsound("voc.mp3")
        os.remove("voc.mp3")