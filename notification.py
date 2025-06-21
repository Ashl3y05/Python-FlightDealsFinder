import os
from twilio.rest import Client

FROM = os.environ["WHATSAPP_FROM"]
TO = os.environ["WHATSAPP_TO"]
class SendNotification:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_SID"]
        self.auth_token = os.environ["TWILIO_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)
        self.from_num = FROM
        self.to_num = TO

    def send_message(self, message: str):
        message = self.client.messages.create(
            body=message,
            from_=self.from_num,
            to=self.to_num,
        )

        print(message.body)