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


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'recycle':
        msg = resp.message("Hi! Welcome to our recycling helper. We will help you determine how to recycle your plastic! Please locate the recycle icon on your plastic item. What number is it?")
        msg.media('https://media.makeameme.org/created/recycling-is-too-5c0bc5.jpg')
    elif body == '1':
        resp.message("1 is recycleable! please take it to your nearest recycle facility. you are based in new brunswick! do you need help finding your nearest recycling center?")
    elif body == '2':
        resp.message("2 is recycleable! please take it to your nearest recycle facility. you are based in new brunswick! do you need help finding your nearest recycling center?")
    elif body == '3':
        resp.message("3 is not recycleable! do you need any more assistance? if so, please enter another plastic recycling number. if not, please type no.")
    elif body == '4':
        resp.message("4 is can sometimes be recycleable! please ask your local recycling facility. you are based in new brunswick! do you need help finding your nearest recycling center?")
    elif body == '5':
        resp.message("5 is can sometimes be recycleable! please ask your local recycling facility. you are based in new brunswick! do you need help finding your nearest recycling center?")
    elif body == '6':
        resp.message("6 is not recycleable! do you need any more assistance? if so, please enter another plastic recycling number. if not, please type no.")
    elif body == '7':
        resp.message("7 is not recycleable! do you need any more assistance? if so, please enter another plastic recycling number. if not, please type no.")
    elif body == 'yes':
        resp.message("the nearest recycling center is North America Recycling Inc. in New Brunswick, NJ. do you need any more assistance? if so, please enter another plastic recycling number. if not, please type no.")
        #resp.message("https://goo.gl/maps/ijxz23DaimL3RKpC9")
    elif body == 'no':
        msg = resp.message("thank you for doing your part for our planet :)")
        msg.media("https://cdn11.bigcommerce.com/s-1mxugrbmxo/products/956/images/1346/TYR__76033.1599842162.386.513.png?c=1")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)