import pyttsx3 as p3
import datetime as dt
import speech_recognition as sr
import webbrowser as wb
import os

Capoo = p3.init()
voice = Capoo.getProperty('voices')
Capoo.setProperty('voice',voice[1].id)

def speak(audio):
    print("Capoo: ", audio)
    Capoo.say(audio)
    Capoo.runAndWait()

def time():
    Time = dt.datetime.now().strftime("%I : %M %p")
    speak(Time)
def welcome():
    hour = dt.datetime.now().hour
    if hour >=0 and hour <=7:
        Capoo = "Good morning. "
    elif hour >=8 and hour <=17:
        Capoo = "Good afternoon. "
    else:
        Capoo = "Good evening. "
    speak(Capoo)
    speak("How can I help you?")
def command():
    cm = sr.Recognizer()
    with sr.Microphone() as source:
        cm.pause_threshold = 2
        audio = cm.listen(source)
    try:
        request = cm.recognize_google(audio,language='en')
        print(f"You: {request}")
    except sr.UnknownValueError:
        print("Please try again or typing the command")
        request = str(input("Your other is: "))
    return request
    
if __name__ =="__main__":
    welcome()
    while True:
        request = command().lower()
        if "google" in request:
            speak("What do you want to search on Google?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Searching {search} on Google')
        if "youtube" in request:
            speak("What do you want to search on Youtube?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Searching {search} on Youtube')
        elif "video" in request:
            vid = r'C:\AI\Vid\Đất nước trọn vẹn niềm vui.mp4'
            os.startfile(vid)
        elif "time" in request:
            time()
        elif "bye" in request:
            speak("Good bye! Have a nice day!")
        else:
            hbo = r'C:\AI\Vid\HBO.mp4'
            os.startfile(hbo)
        