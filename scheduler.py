import time
import atexit

from flask import Flask
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def timeToSendEmail():
    a = 1
    if a == 1 :

        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = ''
        app.config['MAIL_PASSWORD'] = ''
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)

        msg = Message('Hello', sender = '', recipients = [''])
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail.send(msg)
            
        mail.send(msg)

        print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

scheduler = BackgroundScheduler()
scheduler.add_job(func=timeToSendEmail, trigger="interval", seconds=55)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())