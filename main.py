from src.talkingAI.testclass import AIgf
import clipboard
import keyboard
import pyaudio
import time
'''
AI 를 이용한 AI 여자친구

'''


t = AIgf()
    
print(" Hello, this is AI girlfriend")
while True:
    
    
    voice = t.read_voice()
    time.sleep(0.1)
    t.speak(voice)
    
    if keyboard.is_pressed("q"):
        break        

