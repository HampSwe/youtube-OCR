from twilio.rest import Client

client = Client("", "")

to_number = "+46708792939"
from_number = "+19705509127"
message = "Hello from Python!"

client.messages.create(to=to_number, from_=from_number, body=message)
