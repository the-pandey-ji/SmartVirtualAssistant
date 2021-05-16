# ****************************************************************************
# this function willl take command
# It takes microphone input from the user and returns string output
# ****************************************************************************


import \
    speech_recognition as sr  # pip install speechRecognition  //support for several engines and APIs, online and offline


# e.g. Google Cloud Speech API, Microsoft Bing Voice Recognition, IBM Speech to Text etc


# ****************************************************************************
#     Set voice
#       and its properties
# ****************************************************************************
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")
        return "None"
    return query

# takeCommand()