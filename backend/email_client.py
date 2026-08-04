import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def send_email(to_address: str, subject: str, html_body: str):
    from_address = os.environ["EMAIL_ADDRESS"]
    app_password = os.environ["EMAIL_APP_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_address, app_password)
        server.sendmail(from_address, to_address, msg.as_string())
