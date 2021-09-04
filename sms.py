import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "YourEmail"

password = "Password"

sms_gateway = "recipients_number@vtext.com"

smtp = "smtp.office365.com"

port = 587

server = smtplib.SMTP(smtp, port)

server.starttls()

server.login(email, password)

message = MIMEMultipart()

message['From'] = email

message['To'] = sms_gateway

message['Subject'] = "Test 1 20210323\n"

body = "(INSERT MESSAGE HERE)\n"

message.attach(MIMEText(body, 'plain'))

sms = message.as_string()

server.sendmail(email, sms_gateway, sms)

server.quit()
