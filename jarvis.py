import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import subprocess 
import smtplib 

engine = pyttsx3.init()
voices = engine.getProperty('voices') 

selected_voice_id = "com.apple.voice.compact.en-GB.Daniel" 
engine.setProperty('voice', selected_voice_id)     

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()  

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Nova. How can I help you?") 

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e) 
        print("Say that again please...")
        return "None" 
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    server.login('shreyashkande191911@gmail.com', 'Archana123@#$')  
    server.sendmail('shreyashkande191911@gmail.com', to, content)
    server.close()  

if __name__ == "__main__":
    wishMe() 
    while True:
    # if 1: 
        query = takeCommand().lower() 


        # Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results) 
            print(results)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com") 

        elif 'open google' in query:
            speak("Opening google...") 
            webbrowser.open("https://www.google.com") 

        elif 'open StackOverflow' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.stackoverflow.com") 

        elif 'play music' in query:
            speak("Opening YouTube Music...")
            webbrowser.open("https://music.youtube.com/")  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}") 

        elif 'open maps' in query:
            mapsPath = "/System/Applications/Maps.app" 
            subprocess.run(["open", mapsPath]) 

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shreyashkande191911@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e) 
                speak("Sorry, I am not able to send this email")  

        elif 'quit' in query:
            speak("Quitting the program...")
            exit() 