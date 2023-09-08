import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
username = os.getenv('MY_USERNAME')
password = os.getenv('MY_PASSWORD')


def send_mail(text="Email body", subject="Hello Wolrd", from_email="Zajjaj Khan <20b-012-ce@students.uit.edu>", to_emails=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart("alternative")
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    html_part = MIMEText('<h1>This is a Heading</h1>', 'html')

#     msg.attach(html_part) // this is a html part if you wana include that...
    msg_str = msg.as_string()
    # Login to my smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
