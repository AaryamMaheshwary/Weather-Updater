import smtplib


carriers = {
  "att": "@mms.att.net",
  "verizon": "@vtext.com",
  "tmobile": "@tmomail.net",
  "sprint": "@messaging.sprintpcs.com",
  "boost": "@myboostmobile.com",
  "cellular_one": "@mobile.celloneusa.com",
  "cricket": "@mms.mycricket.com",
  "metro_pcs": "@mymetropcs.com"
}


def send_text_message(to_number, to_carrier, from_email, from_password, message, number=1):
    to_number = to_number + carriers[to_carrier]
    auth = (from_email, from_password)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(auth[0], auth[1])
    for i in range(number):
        server.sendmail(auth[0], to_number, message)
