# import packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os


# load the email and password(from two-step verification) variables using the enviroment variables.
load_dotenv()
smtp_username = os.getenv('DB_USER')
smtp_password = os.getenv('DB_PASSWORD')


def send_mail(sender, recipient, subject, body):
    # SMTP (Simple Mail Transfer Protocolo) server settings
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    # Create the message object
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Connect to the SMTP server and send the message
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    print('Email sent successfully.')

if __name__ == '__main__':

    # Email contents
    sender = 'sakhilembane2@gmail.com'
    recipient = 'sakhile.mbane@warnermusic.com'
    subject = 'WMG-SA finance department: Checklist Reminder'
    body = f"""
    <html>
    <head></head>
    <body>
        <h1>{subject}</h1>
        <p> Hello {recipient.split('.')[0]} {recipient.split('.')[1].split('@')[0]},</p>
        <p>I hope this mail finds you well.</p>
        <p>I just wanted to drop a quick note to remind you that ... in respect to our credit card, uber, social media checklist has been submitted.</p>
        <ul>
        <li>items</li>
        </ul>

        <p>Please contact Thato Chiloane regarding the outstanding documents. Your responses will be appreciated. </p>
        <p>Best Regards.</p>
        <p>Sakhile Mbane - Bot reminder</p>
    </body>
    </html>
    """

    send_mail(sender=sender,recipient= recipient, subject= subject, body =body)
    print(f"""Email has been sent to {recipient}""")

