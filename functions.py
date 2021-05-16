# ****************************************************************************
#     functions
#       defined for work
# ****************************************************************************

import smtplib
import datetime
import os
import random

import psutil
import pyautogui
import pyjokes
import wikipedia  # pip install wikipedia
from mainCode import speak
from takeCommand import takeCommand as tc
import webbrowser


# ****************************************************************************
#     send emails
# ****************************************************************************
def mail():
    try:
        speak("What should I say?")
        content = tc()
        to = "pandey143sonu@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry sir. I am not able to send this email")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


# ****************************************************************************
#   greetings
# ****************************************************************************


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome Back sir ,  how may I help you")


# ****************************************************************************
#   play music
# ****************************************************************************

def music():
    music_dir = 'E:\\Downloads'
    songs = os.listdir(music_dir)
    # print(songs)

    os.startfile(os.path.join(music_dir, random.choice(songs)))


# ****************************************************************************
#   search wikipedia
# ****************************************************************************

def fwikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")  # empty for only word wikipedia
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)


# ****************************************************************************
#   hello sir health feeling
# ****************************************************************************
def hello():
    speak("hello sir, how are you ")
    query = tc()
    if 'not fine' in query or 'sick' in query or 'feeling down' in query or 'not well' in query or 'not good' in query or 'not very good' in query:
        speak(
            "If you are experiencing flu-like symptoms including fever, cough or shortness of breath, please contact your doctor’s office to determine whattype of care you need.")
    elif 'feeling sad' in query or 'headache' in query:
        speak("sorry to know , playing song")
        music()

    else:
        speak("excellent sir")


# ****************************************************************************
#   indtoduction
# ****************************************************************************
def introduction():
    speak("""hii , this is jarvis . I am pandeyji's personal assistant .
    I am here to make your life easier. You can command me to perform various tasks.
     learning every day new things and developing myself. 
     my lovely sir working hard on me.. thank you """)


# ****************************************************************************
# Search on google
# ****************************************************************************
def google(query):
    query = query.replace("google", "")
    url = 'https://google.com/search?q=' + query
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    speak('Here is What I found for' + query)


# ****************************************************************************
# Location
# ****************************************************************************

def location(query):
    query = query.replace("location", "")
    url = 'https://google.nl/maps/place/' + query + '/&amp;'
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    speak('Here is the location ' + query)


# ****************************************************************************
# CPU
# ****************************************************************************
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


# ****************************************************************************
# joke
# ****************************************************************************

def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])
# ****************************************************************************
# Screenshot(not working)
# ****************************************************************************

def screenshot():
    img = pyautogui.screenshot()
    img.save(r'\name.png')


# ****************************************************************************
#
# ****************************************************************************

