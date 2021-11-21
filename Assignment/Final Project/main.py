#import libraries
import smtplib
import getpass
import os
import time

def animation():
    for i in range(3):
        print('loading.')
        time.sleep(0.3)
        os.system('cls')
        print('loading..')
        time.sleep(0.3)
        os.system('cls')
        print('loading...')
        time.sleep(0.3)
        os.system('cls')

#Input login mail
os.system('cls')
sender_email = input(str("Input your email \t: "))
sender_pass = getpass.getpass("Input your password \t: ")

#log in email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender_email, sender_pass)
os.system('cls')
animation()
print('Login Successfully!\n')

#Format sending
rec_email = input(str("Input receiver email \t: "))
subject = input(str("Input subject \t\t: "))
body = input(str('Input body \t\t: '))
message = f'Subject: {subject}\n\n{body}'
animation()

#mail
print('From : ', sender_email)
print("To : ", rec_email)
print('Subject : ', subject)
print('Body : ', body)

#sending mail
time.sleep(1)
os.system('cls')
animation()
server.sendmail(sender_email, rec_email, message)
server.close()
print('Email sent!')

#email : alphateamai@gmail.com
#pass : basicpython41