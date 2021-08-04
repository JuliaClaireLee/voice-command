print("HELLO WORLD")
import os
os.system("echo 'hello world'")
os.system("say 'hello world'")

import speech_recognition as sr

with sr.Microphone() as source:
    r = sr.Recognizer()
    os.system("echo 'say something!'")
    os.system("say 'say something!'")
    print("say something!")
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    os.system(text)
    os.system(text)
