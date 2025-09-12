import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import wikipedia
import os

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed
engine.setProperty('volume', 1)  # Volume

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning Tarun!")
    elif hour < 18:
        speak("Good Afternoon Tarun!")
    else:
        speak("Good Evening Tarun!")
    speak("I am Jarvis, how can I assist you Bro ?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""

def run_jarvis():
    greet()
    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)

        elif "play" in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "time" in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "exit" in query or "quit" in query:
            speak("Goodbye Tarun!")
            break

        elif "who are you" in query or "what is your name" in query:
            speak("I am Jarvis, your personal AI assistant.")

        elif query:
            speak("Let me search that for you.")
            pywhatkit.search(query)

# Run Jarvis
run_jarvis()
