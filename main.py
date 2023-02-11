# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

#numbers = [os.getenv('rachelle'), os.getenv('ashley')]

#for number in numbers:
 #   message = client.messages \
  #      .create(
   #         body='This is the ship that made the Kessel Run in fourteen parsecs?',
    #        from_='+18334290085',
     #       to=number
      #  )

#print(message.sid)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'help!':
        msg = resp.message("Hi! Welcome to our recycling helper. We will help you determine how to recycle your plastic! Please locate the recycle icon on your plastic item. What number is it?")
        msg.media('https://media.makeameme.org/created/recycling-is-too-5c0bc5.jpg')
    elif body == '1':
        resp.message("1 is recycleable! please take to your nearest recycle facility")
    elif body == '2':
        resp.message("2 is recycleable! please take to your nearest recycle facility")
    elif body == '3':
        resp.message("3 is not recycleable!")
    elif body == '4':
        resp.message("4 is can sometimes be recycleable! please ask your local recycling facility")
    elif body == '5':
        resp.message("5 is can sometimes be recycleable! please ask your local recycling facility")
    elif body == '6':
        resp.message("6 is not recycleable!")
    elif body == '7':
        resp.message("7 is not recycleable!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)