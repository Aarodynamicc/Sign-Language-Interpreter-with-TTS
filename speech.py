from gtts import gTTS
import pygame
import os

pygame.mixer.init()

def speak(text):
    filename = "temp.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait till it finishes playing
    while pygame.mixer.music.get_busy():
        continue

    os.remove(filename)