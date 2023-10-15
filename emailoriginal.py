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


def Fetch_inbox(x):
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
        Speak_Text(f"Message {msgnum}, recieved from {message.get('from')} on {message.get('date')} subjecting {message.get('subject')}")
        if(a==2):
            break
        # print("Content\n")
        # for part in message.walk():
        #     if part.get_content_type() == "text/plain":
        #         # print(part.as_string())
        #         print(part)
        #         # print(part.decode("ascii"))
Speak_Text("The recent 10 mails in your inbox are")
Fetch_inbox(10)
