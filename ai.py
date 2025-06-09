import speech_recognition as sr
import pyttsx3
import os
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("\nListening for your command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry")
            return ""
        except sr.RequestError:
            speak("Sorry, speech service is not available.")
            return ""

def run_ai_controller():
    speak("Hello, I am your AI Laptop Controller. How can I help you?")
    while True:
        command = listen_command()

        if 'open notepad' in command:
            speak("Opening Notepad")
            os.system('notepad.exe')

        elif 'open calculator' in command:
            speak("Opening Calculator")
            os.system('calc.exe')

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open('https://www.google.com')

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open('https://www.youtube.com')

        elif 'open github' in command:
            speak("Opening GitHub")
            webbrowser.open('https://www.github.com')

        elif 'open whatsapp' in command :
            speak("Opening Whatsapp")
            webbrowser.open('https://web.whatsapp.com')

        elif 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry")

run_ai_controller()
