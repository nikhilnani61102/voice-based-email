import speech_recognition as sr
import pyttsx3
import smtplib
import tkinter

from Blinde_mans_mail import Speak_Text
r = sr.Recognizer()


def speech_2Text():    
    while(1):
        try:
            with sr.Microphone() as source1:
                r.adjust_for_ambient_noise(source1,duration=0.2)
                audio1 = r.listen(source1)
                Body = r.recognize_google(audio1)
                Body = Body.lower()
                onlyonce = (Body.split(" "))
                if("complete" in onlyonce and "recording" in onlyonce):
                    Speak_Text("Recording succesfully stored")
                    return l
                else:
                    l = list()
                    l = Body.split(" ")
                    print("so the recording is: ",Body)
                    Speak_Text("So the recording is "+Body)
        except sr.RequestError as e:
            print("Could not request results;{0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")
            Speak_Text("Sorry I didnt get you Kindly repeat")

bodymatter = speech_2Text()
print(bodymatter)