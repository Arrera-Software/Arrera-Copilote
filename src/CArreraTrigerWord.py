import speech_recognition as sr

class CArreraTrigerWord :
    def __init__(self,word:str):
        self.__word = word
    
    def detectWord(self):
        """
        0  : Mots pas detecter
        1  : Mots detecter
        -1 : Impossible de reconaitre l'audio
        -2 : Erreur de reqette
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            if self.__word in text:
                return 1
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2
        return 0