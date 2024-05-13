import speech_recognition as sr
from unidecode import*
from src.pygamePlaysound import*

class SIXsrc :
    def __init__(self)->None:
        pass
       
    def speak(self,texte:str):
        paroleSix(texte)
        
    
    def micro(self):
        objetReconnaissance = sr.Recognizer()
        with sr.Microphone() as micro:
            entrer = objetReconnaissance.listen(micro)
            try:
                requette = unidecode(objetReconnaissance.recognize_google(entrer, language='fr'))
            except sr.WaitTimeoutError as e:
                requette = "nothing"
            except sr.RequestError as e:
                requette = "nothing"
            except sr.UnknownValueError:
                requette = "nothing"
            return requette