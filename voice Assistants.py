import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun raha hoon...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Samajh raha hoon...")
        command = r.recognize_google(audio, language='hi-IN')
        print("Aapne kaha:", command)
    except:
        speak("Dobara boliye")
        return ""
    return command.lower()

speak("Namaste, main aapka voice assistant hoon")

while True:
    query = take_command()

    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Abhi samay hai {time}")

    elif "wikipedia" in query:
        speak("Wikipedia se dhoond raha hoon")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "google kholo" in query:
        speak("Google khol raha hoon")
        webbrowser.open("https://google.com")

    elif "youtube kholo" in query:
        speak("YouTube khol raha hoon")
        webbrowser.open("https://youtube.com")

    elif "band ho jao" in query or "exit" in query:
        speak("Dhanyavaad, alvida")
        break
