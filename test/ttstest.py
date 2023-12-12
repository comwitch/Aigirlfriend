from speech_recognition import *
from pyautogui import *
from gtts import gTTS
import clipboard
import keyboard
import pyaudio
import time
import playsound
import os

def read_voice():
    r = Recognizer()
    mic = Microphone()
    
    with mic as source:
        audio = r.listen(source)
        
    voice_data = r.recognize_google(audio, language='ko-KR')
    return voice_data

def typing(value):
    clipboard.copy(value)
    hotkey('ctrl', 'v')
    hotkey('enter')
    
def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('./voice.mp3')
    
while True:
    if keyboard.is_pressed("ctrl+alt"):
        voice = read_voice()
        time.sleep(0.1)
        speak(voice)
        