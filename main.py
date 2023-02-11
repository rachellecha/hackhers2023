# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

numbers = [os.getenv('rachelle'), os.getenv('ashley')]

for number in numbers:
    message = client.messages \
        .create(
            body='This is the ship that made the Kessel Run in fourteen parsecs?',
            from_='+18334290085',
            to=number
        )

print(message.sid)
