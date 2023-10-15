import os
import speech_recognition as sr
import webbrowser
import datetime

def say(text):
    os.system(f"say {text}")

def takevoice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured..Sorry"


if __name__=="__main__":
    print("hello")
    say("hello i am MAYDAY A.I")
    while True:
        print("Listening..")
        query=takevoice()
        #say(query)
        sites=[["youtube","http://youtube.com"],["wikipedia","http://wikipedia.com"],["Google","http://google.com"],["instagram","http://instagram.com"]]
        
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opending {site[0]}")
                webbrowser.open(site[1])

        if "the time" in query:
            #strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            hourr=datetime.datetime.now().strftime("%H")
            minn=datetime.datetime.now().strftime("%M")

            say(f"Sir the time is {hourr} baaj K {minn} minutes")
        
       
