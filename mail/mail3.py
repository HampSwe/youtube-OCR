import yagmail

sender_email = "auto.hampswe@gmail.com"

receiver = "hampus.serneke@gmail.com"
subject = "Test"
text = "Hej! Det här är ett test."
  
yag = yagmail.SMTP(sender_email, password, oauth2_file="oauth.json")
yag.send(receiver, subject, text)
