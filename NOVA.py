import os
import pyautogui
import datetime
import time
import webbrowser
import pyttsx3 
import speech_recognition as sr

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')                                #0-male  inside sapi5
    engine.setProperty('voice',voices[1].id)                             #1-female
    
    rate = engine.getProperty('rate')                                    #rate means how fast it talks
    engine.setProperty('rate',rate-50)
    
    volume = engine.getProperty('volume')
    engine.setProperty('volume',volume+0.23)
    return engine

engine = initialize_engine()

def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    
def command():                                                             #giving input as speech from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Listning.....",end="",flush=True)
        r.pause_threshold=1.0
        r.phrase_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
       # r.non_speaking_duration=True
        #r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit = 10
        audio = r.listen(source)
        
    try:
        print("\r",end="",flush=True)
        print("Recognising....",end="",flush=True)
        query = r.recognize_google(audio,language='en-in')
        print("\r",end="",flush=True)
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query



def cal_day():
    day = datetime.datetime.today().weekday()+1
    day_dict = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
        return day_of_week

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    
    if(hour>=0) and (hour<=12) and ('AM' in t):
        speak(f"good morning, it's {day} and the time is {t}")
    elif(hour>=12) and (hour<=16) and ('PM' in t):
        speak(f"good afternoon, it's {day} and the time is {t}")
    else:
        speak(f"good evening, it's {day} and the time is {t}")
        
def social_media(query):
    if'youtube' in query:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com")
    elif'google' in query:
        speak("open google")
        webbrowser.open("https://www.google.com")
    else:
        speak("no result found try again")
        

   
        

if __name__ == "__main__":
    wishMe()
    while True:
        query = command().lower()
        print("->", query)
        
        if query == "none":
            continue
        if any(word in query for word in ["stop", "exit", "quit", "bye", "goodbye", "close"]):
            speak("Okay, have a nice day!")
            print("Assistant stopped.")
            break 
        
        
        if ('youtube' in query) or ('google' in query):
            social_media(query)                   
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("volume increases")
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("volume decreased")
        elif ("volume mute" in query) or ("mute volume" in query):
            pyautogui.press("volumemute")
            speak("volume muted")

    
        
             
            
 
           
        #print(query)
    