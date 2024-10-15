#Before Running The Code, Make Sure To Download These Libraries First
#pip install requests gtts pygame

import requests
from gtts import gTTS
import pygame
import os

class Speaking:
    def __init__(self):
        pygame.mixer.init()

    def speak(self, audio):
        tts = gTTS(text=audio, lang='en')
        tts.save("output.mp3")
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        os.remove("output.mp3")

class GFG:
    def __init__(self):
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        
    def get_word_meaning(self, word):
        try:
            response = requests.get(self.api_url + word)
            if response.status_code == 200:
                data = response.json()
                meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
                return meaning
            else:
                return None
        except Exception as e:
            print(f"Error fetching the word meaning: {e}")
            return None

    def Dictionary(self):
        speak = Speaking()
        speak.speak("Which word do you want to find the meaning of?")

        query = input("Enter the word: ").strip()
        
        word_meaning = self.get_word_meaning(query)        
        if word_meaning:
            print(f"Meaning of {query}: {word_meaning}")
            speak.speak(f"The meaning of {query} is: {word_meaning}")
        else:
            speak.speak(f"Sorry, I could not find the meaning of {query}.")

if __name__ == '__main__':
    gfg = GFG()
    gfg.Dictionary()