import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt
import random as rn
import pandas as pd

birth = pd.read_csv("birthdays")


with open("letter_1.txt") as let1:
    let1 = let1.read()
with open("letter_2.txt") as let2:
    let2 = let2.read()
with open("letter_3.txt") as let3:
    let3 = let3.read()

lista_lett = [let1, let2, let3]

now = dt.datetime.now()
year = now.year
com = dt.datetime(year=1991, month=6, day=16)


index = "a"

for i in birth.iterrows():
    if i[1]["day"] == now.day and i[1]["month"] == now.month:
        index = i[0]


if index != "a":
    mail_content = rn.choice(lista_lett).replace("[NAME]", birth.name[index])
    receiver_address = birth.email[index]

# The mail addresses and password
sender_address = 'provaprovone222@hotmail.com'
sender_pass = ''

# Setup the MIME
message = MIMEMultipart("alternative")
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Happy Birthday'  # The subject line

# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
# Create SMTP session for sending the mail
with smtplib.SMTP('smtp-mail.outlook.com', 587) as session:  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    print('Mail Sent')
    session.quit()
