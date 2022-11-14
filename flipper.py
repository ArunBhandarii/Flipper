import datetime
import subprocess
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import requests


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'flipper' in command:
                command = command.replace('flipper', '')
                print(command)
    except:
        pass
    return command


def run_flipper():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('Sorry, but I am in a relationship with your laptop')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hack' in command:
        talk('Sure, Running a penetration testing assessment')
        pro = subprocess.run('/attack.sh')
        print(pro.returncode)
    elif "ip address" in command:
        ip = requests.get('https://api.ipify.org').text
        print(ip)
        talk(f"Your ip address is {ip}")
    elif "shutdown" in command or "offline" in command:
        talk("Alright, going offline. It was nice working with you")
        sys.exit()

    else:
        talk('Can you repeat that again?')


while True:
    run_flipper()
