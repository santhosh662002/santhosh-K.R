import datetime
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 24 <= hour < 12:
        speak("Good Morning" "Sir!")
    elif 12 <= hour < 16:
        speak("Good Afternoon" "Sir!")
    else:
        speak("Good Evening" "Sir!")
    speak("Emma reporting!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        q = r.recognize_google(audio, language='en-in')
        print("user said: ", q)
    except Exception as e:
        print(e)
        speak("sorry Sir, Can you repeat that again?")
        return "None"
    return q


if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can I" "help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:

            speak("Searching in wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open Youtube' in query:
            webbrowser.open("Youtube.com")
            speak("Youtube is opened for you Sir")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened for you Sir")
        elif 'open gmail' in query:
            webbrowser.open("gamil.com")
            speak("gmail is opened for you Sir")
        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played sir")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'stop' in query:
            speak("See you soon Sir")
            exit()
        else:
            webbrowser.open(query)