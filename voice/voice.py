import speech_recognition as sr
import pyttsx3
from backend.ai_engine import ask_ai
r=sr.Recognizer()
e=pyttsx3.init()
with sr.Microphone() as s:
    while True:
        a=r.listen(s)
        t=r.recognize_google(a)
        if t=="exit":
            break
        e.say(ask_ai(t))
        e.runAndWait()
