import pygame as p
from gtts import gTTS
import os

def paroleSix(texte:str):
    tts = gTTS(texte, lang="fr")
    p.mixer.init()
    tts.save("voc.mp3")
    p.mixer.music.load("voc.mp3")
    p.mixer.music.play()
    while p.mixer.music.get_busy():
        p.time.Clock().tick(10)
    p.mixer.quit()
    os.remove("voc.mp3")

def playsound(file:str):
    p.mixer.init()
    p.mixer.music.load(file)
    p.mixer.music.play()
    while p.mixer.music.get_busy():
        p.time.Clock().tick(10)
    p.mixer.quit()