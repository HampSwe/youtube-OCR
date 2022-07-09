from twilio.rest import Client

client = Client("AC98769180bc1c24a170f068c8b03b59d1", "56f6f56a9441de1fea5c7e59addb72f7")

to_number = "+46708792939"
from_number = "+19705509127"
message = "Hello from Python!"

client.messages.create(to=to_number, from_=from_number, body=message)