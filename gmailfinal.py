import imaplib
# import mail
import email
import base64
imap_server = "imap.gmail.com"
email_addresss = "20n31a6947@gmail.com"
passwo = "eivjqeojgoarrioz"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_addresss,passwo)
imap.select("Inbox")

_,msgnums = imap.search(None,"10")
for msgnum in msgnums[0].split():
    _,data = imap.fetch(msgnum,"RFC822")
    message = email.message_from_bytes(data[0][1])
    # print(message)
    print(f"Message Number: {msgnum}")
    print(f"From: {message.get('from')}")
    print(f"To: {message.get('to')}")
    print(f"Date: {message.get('date')}")
    print(f"Subject: {message.get('subject')}")
    print("Content\n")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            # print(part.as_string())
            print(part)
            # print(part.decode("ascii"))
