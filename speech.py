import subprocess
import speech_recognition as sr
def speak(text):
    subprocess.run(["say", "-v", "Alex", text])

def listen():

    r = sr.Recognizer()

    try:
            with sr.Microphone() as source:
                print("Listening...")
                
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                print("Audio recorded successfully!")
                text = r.recognize_google(audio, language="en-IN")
                text = text.lower()  
                return text
                
               

    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

    except sr.UnknownValueError:
            print("Could not understand audio")
            return None

   
            

