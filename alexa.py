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

engine.say("hai i am Alexa ,Alex v Ajith's Personal Assistant")
engine.say("What can i do for you?")
engine.runAndWait()
status = True
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif (('who made' in command) or ('your creator' in command)):
    	talk('I was made by Alex v Ajith , second year computer science engineering student')
    	talk("hopefully i am his first and best Project,  ha ha ha ")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'about' in command:
        command = command.replace('tell me about','')
        talk('performing a google search regarding' + command)
        pywhatkit.search(command)
    elif 'message' in command:
        print('recording message')
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            mess = listener.recognize_google(voice)
            pywhatkit.sendwhatmsg('your number',mess,12,2)
    elif 'date' in command:
        date = datetime.date.today()
        talk(date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('ok bye...Have a nice day')
        status = False
    else:
        talk('Please say the command again.')

    

while status:
    run_alexa()
