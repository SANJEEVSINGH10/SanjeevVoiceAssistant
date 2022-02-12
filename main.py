import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import PyPDF2

book = open('javadoc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
      with sr.Microphone() as source:
        print('listening...')
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'babe' in command:
            command = command.replace('babe', '')
            print(command)

    except:
          pass
    return command

def run_babe():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'read pdf' in command:
        page = pdfReader.getPage(0)
        text = page.extractText()
        talk(text)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry I am a virtual assistant , first made me a body')
    elif 'sanjeev singh' in command:
        talk('He made me with writing line of Codes')
    elif 'god' in command:
        talk('God is who creates and Destroy one and everyone if wants to and I dont know who exactly is God ,'
             'but for me as Sanjeev Created me and can Destroy the same so for me '
             'Sanjeev is God')
    elif 'are you single' in command:
        talk('first give me a physical body then talk')
    else:
        talk('Please say the command again.')
run_babe()


