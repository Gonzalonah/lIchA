import speech_recognition as sr
import pyttsx3
import pywhatkit

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

name = "licha"
listener = sr.Recognizer()
engine = pywhatkit.init()

voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc=listener.listen(source)
            rec=listener.recognize_google(pc)
            rec=rec.lower()
            if name in rec:
                rec=rec.replace(name,'')
    except:
        pass
    return rec

def run_licha():
    while True:
        try:
            rec=listen()
        except UnboundLocalError:
            print("No te entendi, me lo repetis?")
            continue
        if 'reproduce' in rec:
            a =rec.replace('reproduce','')
            print("Reproduciendo "+ a)
            talk("Reproduciendo "+ a)
            pywhatkit.playonyt(a)
if __name__ == '__main__':
    run_licha()