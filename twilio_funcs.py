from twilio.rest import Client


def call(number="+46708792939"):

    client = Client("AC98769180bc1c24a170f068c8b03b59d1", "56f6f56a9441de1fea5c7e59addb72f7")
    call = client.calls.create(
        from_="+19705509127",
        to=number,
        url="https://handler.twilio.com/twiml/EH0a7d8e158960a9c59f7e2117a902637a"
    )


def text(msg, number="+46708792939"):

    client = Client("AC98769180bc1c24a170f068c8b03b59d1", "56f6f56a9441de1fea5c7e59addb72f7")

    to_number = number
    from_number = "+19705509127"
    message = msg

    client.messages.create(to=to_number, from_=from_number, body=message)