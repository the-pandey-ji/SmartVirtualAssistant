# Author : Sonu Pandey
# Version : 1.0
# Date : 06 Aug 2020

import pyttsx3  # pip install pyttsx3  // text to speech conversion library
import \
    speech_recognition as sr  # pip install speechRecognition  //support for several engines and APIs, online and offline
# e.g. Google Cloud Speech API, Microsoft Bing Voice Recognition, IBM Speech to Text etc

import webbrowser
import os
import datetime
import subprocess
from gtts import gTTS  # google text to speech
import playsound  # to play saved mp3 file

import functions
from takeCommand import takeCommand as tc

# ****************************************************************************
#     Set voice
#       and its properties
# ****************************************************************************


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


music_file_number = 0


def speaks(output):
    global music_file_number

    # num to rename every audio file
    # with different name to remove ambiguity
    music_file_number += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(music_file_number) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


if __name__ == "__main__":
    # functions.wishMe()
    while True:
        query = tc().lower()
        if 'stop listening' in query:
            speak("thank you sir")
            break
        elif 'hello jarvis' in query or 'hi jarvis' in query:
            functions.hello()

        elif 'open camera' in query:
            speak("starting ....")
            subprocess.run('start microsoft.windows.camera:', shell=True)

        elif 'introduce yourself' in query or 'who are you' in query:
            functions.introduction()

        elif "what are you doing" in query:
            speak("chilling sir , today we do not have more work ")


        elif 'wikipedia' in query:
            functions.fwikipedia(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            functions.music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Pandey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email send' in query or 'send email' in query:
            functions.mail()

        elif 'google' in query:
            functions.google(query)

        elif 'location' in query:
            functions.location(query)

        elif 'cpu' in query:
            functions.cpu()

        elif 'joke' in query:
            functions.joke()

        elif 'screenshot' in query:
            functions.screenshot()
