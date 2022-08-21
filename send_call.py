from twilio.rest import Client


def call(number="+46708792939"):

    client = Client("", "")
    call = client.calls.create(
        from_="+19705509127",
        to=number,
        url="https://handler.twilio.com/twiml/EH0a7d8e158960a9c59f7e2117a902637a"
    )
