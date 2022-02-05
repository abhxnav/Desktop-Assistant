import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("How may I help you?")
    print("How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        print("Sorry! Didn't get you....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server. starttls()
    server.login('k.abhinav1000@gmail.com', "pass")
    server.login('k.abhinav1000@gmail.com',to, content)
    server.close()



if __name__ == '__main__':
    assname = "DRAKE"
    wishMe()
    activeRecognition = True
    while activeRecognition == True:
        query = takeCommand().lower()

        if "your name" in query:
            speak("You can call me DRAKE!")
            speak(assname)
            print("You can call me DRAKE")
 
        elif 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening Google....")

        elif 'open github' in query:
            webbrowser.open("github.com")
            print("Opening GitHub....")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            print("Opening LinkedIn....")

        elif 'open portal' in query:
            webbrowser.open("uims.cuchd.in")
            print("Opening CUIMS....")

        elif 'play music' in query:
            music_dir = 'E:\\test_music'
            songs = os.listdir(music_dir)
            print("Playing Music")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"right now it is {strTime}")
            print(f"right now it is {strTime}")
            

        elif 'open browser' in query:
            browserPath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(browserPath)
            
        elif 'open brave' in query:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(browserPath)
            
        elif 'open sublime' in query:
            sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimePath)

        elif 'open code' in query:
            codePath = "C:\\Users\\Abhinav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'email to yash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'yashbochiwal@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, the Email couldn't be sent....")
        
        elif 'weather' in query:
            speak("Please repeat only the name of the place!")
            place = takeCommand()
            weather = wf.forecast(place)
            intro = "Weather forcast for " + weather['place'] + " for " + weather['date'] + " is"

            day = ""
            if weather['day']['phrases']:
                day += "\tWeather: " + weather['day']['phrases'] + "\n"
            if weather['day']['temperature']:
                day += "\tTemperature: " + str(weather['day']['temperature']) + "\n"
            if weather['day']['precipitate']:
                day += "\tPrecipitation: " + str(weather['day']['precipitate']) + "\n"
            if weather['day']['humidity']:
                day += "\tHumidity: " + str(weather['day']['humidity']) + "\n"

            night = ""
            if weather['night']['phrases']:
                night += "\tWeather: " + weather['night']['phrases'] + "\n"
            if weather['night']['temperature']:
                night += "\tTemperature: " + str(weather['night']['temperature']) + "\n"
            if weather['night']['precipitate']:
                night += "\tPrecipitation: " + str(weather['night']['precipitate']) + "\n"
            if weather['night']['humidity']:
                night += "\tHumidity: " + str(weather['night']['humidity']) + "\n"

            speak(intro)
            speak("Day :" + day)
            speak("Night :" + night)

        elif 'stop' in query:
            activeRecognition = False
            speak("Okay")

        elif 'quit' in query:
            speak("Have a nice Day!")
            print("Closing....")
            exit()
            

            
        
            






    