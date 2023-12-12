from speech_recognition import *
from pyautogui import *
from gtts import gTTS
import clipboard
import keyboard
import pyaudio
import time
import playsound
import os

# this is version 1
class AIgf:
    
    def __init__(self):
        self.mp3path = ""
    
    def read_voice(self):
        r = Recognizer()
        mic = Microphone()

        with mic as source:
            audio = r.listen(source)

        voice_data = r.recognize_google(audio, language='ko-KR')
        return voice_data

    def typing(self, value):
        clipboard.copy(value)
        hotkey('ctrl', 'v')
        hotkey('enter')

    def speak(self, text):
        tts = gTTS(text=text, lang='ko')
        filename='voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('./voice.mp3')
    
    
# test code
if __name__ == "__main__":
    
    a = AIgf()
    
    while True:
        if keyboard.is_pressed("ctrl+alt"):
            voice = a.read_voice()
            time.sleep(0.1)
            a.speak(voice)
    

