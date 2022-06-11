import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import sys
import smtplib

print("Initialising Jay")

MASTER = "V"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak function will pronounce the strin which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#This function will wish you according to the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning, " + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon, " + MASTER)
    else:
        speak("Good Evening, " + MASTER)

    #speak("J here. How can I help you?")


#This function will take commands from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en_in")
        print(f"You said: {query}\n")

    except Exception as e:
        print("Could you please say that again?")
        speak("Could you please say that again?")
        query = takeCommand()

    return query



#Main Program starts here

speak("Initialising Jay ,")
wishMe()
query = takeCommand()
query = query.lower()

#Logic for executing basic tasks as per the query
chrome_path = 'C://Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 5)
    print(results)
    speak(results)

elif 'open youtube' in query:
    speak('Searching Youtube...')
    url = 'youtube.com'
    chrome_path = 'C://Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query:
    speak('Opening Google...')
    url = 'google.com'
    chrome_path = 'C://Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open reddit' in query:
    speak('Opening Reddit...')
    url = 'reddit.com'
    webbrowser.get(chrome_path).open(url)

elif 'open spotify' in query:
    speak('Opening Spotify...')
    url = 'https://open.spotify.com'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query:
    songs_dir = "E:\\vaishnav\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    n = len(songs)
    for i in range (0,n):
        os.startfile(os.path.join(songs_dir, songs[i]))
        i = i+1

elif 'open discord' in query:
    speak('Launching Discord...')
    os.startfile(r"C:\Users\DR\AppData\Local\Discord\app-1.0.9002\Discord.exe") #r"File name" so it gets converted to raw string!!!

elif 'open vs code' in query:
    speak('Launching VS Code...')
    os.startfile(r"C:\Users\DR\AppData\Local\Programs\Microsoft VS Code\Code.exe")

elif 'open cortex':
    speak ('Launching Razer Cortex...')
    os.startfile(r"C:\Program Files (x86)\Razer\Razer Cortex\CortexLauncher.exe")

elif 'play the song' in query:
    query = query.replace("play the song ","")
    song_name = query #file to be searched
    print(song_name)
    songs_dir = "E:\\vaishnav\\Music"
    songs = os.listdir(songs_dir)
    search_list = []
    for i in range (len(songs)):
        x = songs[i].lower() 
        x = x.replace(".mp3","")
        if song_name == x:
            print("Found")
            song_name = song_name + ".mp3"
            print(song_name)
            os.startfile(os.path.join(songs_dir, song_name))
            
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("The time is", strTime)
    speak(f"{MASTER}, the time is {strTime}")
    

