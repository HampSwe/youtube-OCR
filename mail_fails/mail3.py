import yagmail

client_id = "905792212334-b4bs4enla1j1l0hrbhmsh0otaqneqrr3.apps.googleusercontent.com"
client_secret = "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"


sender_email = "auto.hampswe@gmail.com"
password = "kebabrulle"

receiver = "hampus.serneke@gmail.com"
subject = "Test"
text = "Hej! Det här är ett test."
  
yag = yagmail.SMTP(sender_email, password, oauth2_file="oauth.json")
yag.send(receiver, subject, text)