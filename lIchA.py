""" https://articulo.mercadolibre.com.ar/MLA-1127613564-microfono-grabacion-condenser-podcast-consola-efectos-placa-_JM?searchVariation=174303228528#searchVariation=174303228528&position=41&search_layout=stack&type=item&tracking_id=1d3cfdeb-58dc-40f4-b874-698a23532fa3 para seguir con licha
"""
import pyttsx3
import pywhatkit
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Escuchando....')
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
except:
    pass

""" engine = pyttsx3.init()
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
 """