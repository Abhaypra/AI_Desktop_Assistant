import sys
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import cv2
import pyaudio
import os
import random
import requests
from requests import get  # for ip address
import wikipedia  # for getting content from wikipedia
import webbrowser  # open website
import pywhatkit as kit  # for search specific task
import pyjokes
import time
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import scrolledtext
import threading

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


# Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To Convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning Sir, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good Afternoon sir, its {tt}")
    else:
        speak(f"Good Evening sir, its {tt}")
    speak("I am Jarvis sir. Please tell me how can I help you")


# for news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=07a8ecac1b044bbe8c8d1b4340634f97'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # Logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')

        elif 'Jarvis' in query:
            speak("Yes, Sir")

        elif 'thank you' in query:
            speak('No problem sir')

        elif "open msword" in query:
            wordpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordpath)

        elif "close msword" in query:
            speak("okay sir, closing msword")
            os.system("taskkill /f /im msword.exe")

        elif "open powerpoint" in query:
            pptpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(pptpath)

        elif "close powerpoint" in query:
            speak("okay sir, closing powerpoint")
            os.system("taskkill /f /im npowerpoint.exe")

        elif "open excel" in query:
            excelpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excelpath)

        elif "close excel" in query:
            speak("okay sir, closing excel")
            os.system("taskkill /f /im excel.exe")

        elif "open google chrome" in query:
            chromepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(chromepath)

        elif "open microsoft edge" in query:
            edgepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(edgepath)

        elif "open adobe reader" in query:
            adobepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader 9.lnk"
            os.startfile(adobepath)

        elif "open vs code" in query:
            vscodepath = "C:\\Users\\Bairagi ji\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(vscodepath)

        elif "open command prompt" in query:
            cmdpath = "C:\\Users\\Bairagi ji\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(cmdpath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(1)
                if k == 10:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia... ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open youtube search" in query:
            speak("Sir, What Should I search on Youtube")
            ycm = takecommand().lower()
            webbrowser.open(f"{ycm}")

        elif "open google" in query:
            speak("Sir, What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play song on youtube" in query:
            kit.playonyt("perfect")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me a news" in query:
            speak("please wait sir , fetching the latest news")
            news()

        elif "take a screenshot" in query:
            speak("Sir, Please tell me the name for this Screenshot file")
            name = takecommand().lower()
            speak("Sir, please hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, The Screen Shot Saved in our main folder")

        elif "exit" in query:
            speak("Thanks for using me sir, Have a Good Day.")
            sys.exit()

        elif "no" in query:
            speak("Thanks for using me sir, Have a Good Day.")
            sys.exit()
