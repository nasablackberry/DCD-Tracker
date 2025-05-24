# whatsapp.py
from twilio.rest import Client
import os
from dotenv import load_dotenv

def send_whatsapp_message(body):
    load_dotenv()
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_number = os.getenv('TWILIO_FROM')
    to_number = os.getenv('WHATSAPP_TO')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number
    )
    return message.sid
