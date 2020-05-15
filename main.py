import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #used to send mail

engine = pyttsx3.init('sapi5') #sapi5 = Microsoft Speech API
voices = engine.getProperty('voices')
# print("voices[0].id",voices[0].id) --> voices[0]=male voice, voices[1]=female voice
# print("voices", voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # speak("I am Jarvis Sir. Please tell me how may I help you")
    speak("Hello El Profesor here. Please tell me how may I help you")       

def takeCommand():
    '''It takes microphone input from the user and returns string output. Inshort it is converting audio input into string.'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 300   --> minimum audio energy to consider for recording. change(increase) if you are in a noisy place
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("\nSay that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@yours.com', 'your_email_account_password')
    server.sendmail('email@yours.com', to, content)
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
            results = wikipedia.summary(query, sentences=2)  # sentences = number of sentences you want fro wikipedia summary
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            webbrowser.open("https://gaana.com/song/aeroplane-112")
            '''music_dir = 'F:\\songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))'''


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   #--> to open visual studio code
            # codePath = "C:\\Sublime Text 3\\sublime_text.exe" # to open sublime text
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "mrr.91097@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email at the moment")    


        elif 'quit' or 'exit' in query:
            exit()
            # sys.exit(1)
