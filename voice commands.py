print("HELLO WORLD")
import os
import webbrowser
os.system("echo 'hello world'")
os.system("say 'hello world'")
spot = "https://open.spotify.com"
cap = "https://youtu.be/pc0mxOXbWIU"
lat = "https://www.latimes.com/"
ted = "https://tv.apple.com/us/show/ted-lasso/umc.cmc.vtoh0mn0xn7t3c643xqonfzy?ctx_brand=tvs.sbd.4000"
url = "https://www.google.com/search?q=weather+&client=safari&rls=en&ei=uIYgYbf-IZPO0PEPnc-FuAM&oq=weather+&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyEQguEIAEELEDEIMBEMcBENEDMgsIABCABBCxAxCDATILCAAQgAQQsQMQyQMyBQgAEJIDMgUIABCSAzIECAAQQzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzoHCAAQRxCwAzoHCAAQsAMQQ0oECEEYAFC6ZFi6ZGDZamgBcAJ4AIABnQGIAesBkgEDMS4xmAEAoAEByAEKwAEB&sclient=gws-wiz&ved=0ahUKEwi3urb9qMHyAhUTJzQIHZ1nATcQ4dUDCA0&uact=5"




import speech_recognition as sr

with sr.Microphone() as source:
    r = sr.Recognizer()
    os.system("echo 'say something!'")
    os.system("say 'say something!'")
    print("say something!")
    # read the audio data from the default microphone
    try:
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        if text == "what is the weather":
            os.system("echo   'opening weather in your browser'")
            os.system("say  'opening weather in your browser'")
            webbrowser.open(url)
        elif text == "play music":
            os.system("echo   'opening spotify'")
            os.system("say  'opening spotify'")
            webbrowser.open(spot)
        elif text == "news":
            os.system("echo   'opening the L.A. Times'")
            os.system("say  'opening the L.A. Times'")
            webbrowser.open(lat)
        elif text == "f*** you":
            webbrowser.open(cap)
        elif text == "ted lasso":
            webbrowser.open(ted)
            os.system("echo   'opening Ted Lasso'")
            os.system("say  'opening Ted Lasso'")            
        print(text)
        os.system(text)
        os.system(text)
    except sr.UnknownValueError as e:
          os.system("echo  'I don't understand'")
          os.system("say  'I don't understand'")
          print("I  don't  understand")
         
   
