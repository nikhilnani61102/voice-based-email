import speech_recognition as sr
import pyttsx3
import smtplib
import imaplib
import email
r = sr.Recognizer()



def Speak_Text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

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


def select_mail():    
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

def speech_2option():    
    while(1):
        try:
            with sr.Microphone() as source1:
                r.adjust_for_ambient_noise(source1,duration=0.2)
                audio1 = r.listen(source1)
                Body = r.recognize_google(audio1)
                Body = Body.lower()
                l1= Body.split()
                print(l1)
                if(("compose" in l1) and "mail" in l1):
                    return 1
                elif("inbox" in l1):
                    return 2
                else:
                    Speak_Text("Sorry I didnt get you Kindly repeat")
        except sr.RequestError as e:
            print("Could not request results;{0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occured")
            Speak_Text("Sorry I didnt get you Kindly repeat")


def listToString(s):
    str1 = ""
    for i in s:
        str1 = str1 +""+ i
    return str1
def listToStringg(s):
    str1 = ""
    for i in s:
        str1 = str1 +" "+ i
    return str1

def send_email(message,recievermail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("20n31a6947@gmail.com", "eivjqeojgoarrioz" )
    messagee = message
    # sending the mail
    server.sendmail("20n31a6947@gmail.com", recievermail+"@gmail.com", messagee)
    # terminating the session
    server.quit()
    print(recievermail,"Succesfully sent")


def Fetch_inboxx(x):
    imap_server = "imap.gmail.com"
    email_addresss = "20n31a6947@gmail.com"
    passwo = "eivjqeojgoarrioz"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_addresss,passwo)
    imap.select("Inbox")
    x = "2"
    _,msgnums = imap.search(None,x)
    a = 0
    for msgnum in msgnums[0].split():
        a = a +1
        _,data = imap.fetch(msgnum,"RFC822")
        message = email.message_from_bytes(data[0][1])
        # print(message)
        print(f"Message Number: {msgnum}")
        
        print(f"From: {message.get('from')}")
        print(f"To: {message.get('to')}")
        print(f"Date: {message.get('date')}")
        print(f"Subject: {message.get('subject')}")
        Speak_Text(f"Message {a}, recieved from {message.get('from')} on {message.get('date')} subjecting {message.get('subject')}")
        if(a==2):
            break


def Fetch_inbox():
    imap_server = "imap.gmail.com"
    email_addresss = "20n31a6947@gmail.com"
    passwo = "eivjqeojgoarrioz"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_addresss,passwo)
    imap.select("Inbox")
    x = "all"
    _,msgnums = imap.search(None,x)
    a = 0
    for msgnum in msgnums[0].split():
        a = a +1
        _,data = imap.fetch(msgnum,"RFC822")
        message = email.message_from_bytes(data[0][1])
        # print(message)
        print(f"Message Number: {msgnum}")
        
        print(f"From: {message.get('from')}")
        print(f"To: {message.get('to')}")
        print(f"Date: {message.get('date')}")
        print(f"Subject: {message.get('subject')}")
        Speak_Text(f"Message {a}, recieved from {message.get('from')} on {message.get('date')} subjecting {message.get('subject')}")
        if(a==5):
            break

        # print("Content\n")
        # for part in message.walk():
        #     if part.get_content_type() == "text/plain":
        #         # print(part.as_string())
        #         print(part)
        #         # print(part.decode("ascii"))



Speak_Text("what would you like to do ?")
Speak_Text("Compose Mail")
Speak_Text("or Check Inbox")
choosed = speech_2option()
if(choosed == 1):
    Speak_Text("what would you like to write as the body of the mail, mention complete recording at the end")
    bodymatter = speech_2Text()
    bodymatter = listToStringg(bodymatter)
    print(bodymatter)
    Speak_Text("To whom do you want to send the mail, mention complete recording at the end")
    Recieveremail = speech_2Text()
    Recieveremail = listToString(Recieveremail)
    print(Recieveremail,"@gmail.com")
    # Recieveremail = "nikhilsairampalli"
    send_email(bodymatter,Recieveremail)
elif(choosed == 2):
    Speak_Text("The recent 5 mails in your inbox are")
    Fetch_inbox()
    Speak_Text("Which mail would you like to hear")
    y = select_mail()
    Fetch_inboxx(x=y)

