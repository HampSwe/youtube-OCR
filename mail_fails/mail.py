import smtplib

sender = "auto.hampswe@gmail.com"
receivers = ["hampus.serneke@gmail.com"]

message = """From: From Person <auto.hampswe@gmail.com>
To: To Person <hampus.serneke@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP("localhost")
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except Exception as e:
   print("Error: unable to send email")
   print(e)