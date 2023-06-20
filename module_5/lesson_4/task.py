from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import time
import celery

app = celery.Celery('hello', broker='redis://localhost:6379/0')


@app.task
def send_file(gmail):
    mail_content = '''Hello,
    This is a test mail.
    In this mail we are sending some attachments.
    The mail is sent using Python SMTP library.
    Thank You
    '''
    sender = 'absaitovdev@gmail.com'
    password = 'xqvmseglngdupwrf'
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = gmail
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'

    message.attach(MIMEText(mail_content, 'plain'))
    with open('main.py', 'rb') as attach_file1:
        payload1 = MIMEBase('application', 'octate-stream')
        payload1.set_payload((attach_file1).read())
        encoders.encode_base64(payload1)
    payload1.add_header('Content-Decomposition', 'attachment', filename='main.py')
    message.attach(payload1)
    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(sender, password)
        text = message.as_string()

        session.sendmail(sender, gmail, text)
        session.quit()
        print('Mail Sent')


@app.task
def request_save_data():
    pass


@app.task
def send_message(bot, message, chat_id):
    bot.send_message(chat_id , message)


