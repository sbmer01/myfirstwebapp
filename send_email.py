from email.mime.text import MIMEText
import smtplib

def send_email(name, usn, email):
    from_email=""
    from_password=""
    to_email=email

    subject="Welcome"
    message="Hey there " + name + ", welcome to my domain! Thank you for attending our seminar and workshop in Python programming."

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    smtp=smtplib.SMTP('smtp.live.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(from_email, from_password)
    smtp.send_message(msg)
