# /services/whatsapp_client.py
import os
from twilio.rest import Client

class WhatsAppClient:
    """A client to interact with the Twilio WhatsApp API."""
    def __init__(self):
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")
        
        if not all([account_sid, auth_token, self.twilio_number]):
            raise ValueError("Twilio environment variables not set.")
            
        self.client = Client(account_sid, auth_token)

    def send_message(self, to_number: str, body: str):
        """Sends a text message to a WhatsApp number."""
        try:
            self.client.messages.create(
                from_=self.twilio_number,
                body=body,
                to=to_number
            )
        except Exception as e:
            print(f"Error sending message: {e}")

    def send_media(self, to_number: str, file_url: str, caption: str):
        """Sends a media file to a WhatsApp number."""
        try:
            self.client.messages.create(
                from_=self.twilio_number,
                media_url=[file_url],
                body=caption,
                to=to_number
            )
        except Exception as e:
            print(f"Error sending media: {e}")
