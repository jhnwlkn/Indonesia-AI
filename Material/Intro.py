 # Mengoutputkan Hello World
 #print("Hello World")
'''
ini
bisa
buat 
comment
'''

'''
Operasi

n = "John"
k = "Basic"
print(n + " " + k)
print(type(n))
+  = tambah
-  = kurang
*  = kali
/  = bagi
** = eksponensial   Ex. x**y = x pangkat y
'''

'''
Python Casting

Ex. 
    x = 2.8
    x merupakan float
    namun apabila di casting maka bisa di ubah tipe datanya
    print(int(x))
    print(char(x))
'''
# Import library
import smtplib
import ssl

from email.mime.text import MIMEText
from email.utils import formataddr

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from getpass import getpass

email_txt = open("email_list.txt", "r")
email_list = (email_txt.read().splitlines())

email_name = []
for email in email_list:
    name = email.split("@")
    email_name.append(name[0])

# User configuration
sender_email = 'nihaopython21@gmail.com'
sender_name = 'Nihao Python'

receiver_emails = email_list
receiver_names = email_name


# Input password
password = getpass(prompt='Please, type your password: ')

# Email body
email_html = open('email.html')
email_body = email_html.read()

# Send image
filename = "cat.gif"

for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
    print("Sending the email ...")
    # Configurating the email information
    msg = MIMEMultipart()
    msg['To'] = formataddr((receiver_name, receiver_email))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = 'Hello, my best friend ' + receiver_name

    msg.attach(MIMEText(email_body, 'html'))

    try:
        with open(filename, 'rb') as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        msg.attach(part)
    except:
        print(f"Oh no! We didn't found the attachment!\n{e}")

    try:
        # Creating a SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Encryps the email
        context = ssl.create_default_context()
        server.starttls(context=context)
        # We log in into our Gmail account
        server.login(sender_email, password)
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent')
    except:
        print(f"Oh no! Something bad happened!\n{e}")
    finally:
        print('Closing the server....')
        server.quit()