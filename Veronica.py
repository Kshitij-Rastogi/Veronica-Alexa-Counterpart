import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
            print('Listening... ')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'veronica' in command:
                command = command.replace('veronica', '')
                print(command)

            elif 'veronika' in command:
                command = command.replace('veronika', '')

            if 'jarvis' in command:
                command = command.replace('jarvis', '')

    except:
        pass
    return command


def run_veronica():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'love' in command or 'like' in command:
        talk("Oh my god, that's so sweet of you")

    elif 'kshitij' in command:
        talk('Mr Shitij is my creator, I love him so much, he was born on 1st September 1996, Currently he is working as a Business Analyst in ETech Global Services')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'tell me about' in command or 'who is ' in command:
        if 'tell me about' in command:
            person = command.replace('tell me about', '')
        else:
            person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'dedicate' in command:
        dedicatedsong = pywhatkit.playonyt('Dekha Hazaron Dafa Aapko')

    elif 'date' in command:
        talk('Sorry, I have a boyfriend')

    else:
        talk("Sorry, I didn't get your point")


run_veronica()

