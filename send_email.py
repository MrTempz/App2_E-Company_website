import smtplib
import ssl
import mail_credentials

def send_email(message):

    host = 'smtp.gmail.com'
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(mail_credentials.username, mail_credentials.password)
        server.sendmail(mail_credentials.username, mail_credentials.receiver, message)
