import requests, json, datetime, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen


def sendmail(msg, subject, toadressmail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #credentials of sender
    FROM = "ton email"
    PASSWORD = "ton mot de passe " #hidden password in other .py file

    #logging in
    server.login(FROM, PASSWORD)


    #template for recievers
    TOADDR = [f"{toadressmail}"]
    SUBJECT = str(subject)
    TEXT = str(msg)

    #MSG template

    FINAL_TO = [TOADDR]
    message = MIMEMultipart()
    message['From'] = "IpLocalisator <{}>".format(FROM)
    message['To'] = ', '.join(TOADDR)
    message['Subject'] = SUBJECT
    message.attach(MIMEText(TEXT))

    MSG = message.as_string()

    #Join reciever with CC
    FINAL_TO = [TOADDR]



    server.sendmail(FROM, FINAL_TO, MSG)

ip = input("Entrer ip ")
req = urlopen("http://ip-api.com/json/" + ip +"?lang=fr")
data = json.loads(req.read())
temp = (data['timezone'])
pays = (str('Nom du pays : '+ (data['country'])))
paycode = (str('pays : '+ (data['countryCode'])))
Region = (str("Region : "+ (data['regionName'])))
ville = (str("ville : "+(data['city'])))
code_postal = (str("code postal : "+ (data['zip'])))
total = f"{ip}\n{temp}\n{pays}\n{paycode}\n{Region}\n{ville}\n{code_postal}"
TIME = (str(datetime.datetime.now()).split('.')[0].split(':'))
TIME = str(TIME[0]+':'+TIME[1])
subject = (f"New IP ! {ip}, {format(TIME)}")
adressmail = "a qui ?"
sendmail(total, subject, adressmail)

with open("logs.txt", "a") as logs:
    logs.write(str("------------------------" + "\n" + subject + "\n" + temp + "\n" + pays + "\n" + paycode + "\n" + Region + "\n" + ville + "\n" + code_postal + "\n" + "------------------------" + "\n"))
