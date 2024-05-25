from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'email@gmail.com'
email_pass = password #gmailpassword

email_reciever = '' #mail to sending to

subject = 'suscribe'

body = ' watch'

em = EmailMesaage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subejct'] = subject
em.setcontent(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',456,context=context) as smtp:
    smtp.login(email_sender,email_pass)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
