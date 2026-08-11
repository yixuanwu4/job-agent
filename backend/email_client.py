import os

import requests
from dotenv import load_dotenv

load_dotenv()

def send_email(to_address: str, subject: str, html_body: str, text_body: str):
    api_key = os.environ["RESEND_API_KEY"]
    from_address = os.environ["EMAIL_ADDRESS"]

    response = requests.post(
        "https://api.resend.com/emails",
        headers = {"Authorization": f"Bearer {api_key}"},
        json = {
            "from": from_address,
            "to": [to_address],
            "subject": subject,
            "html": html_body,
            "text": text_body,
        }
    )
    response.raise_for_status()