import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

mail_from = 'xyz@outlook.com'  # sender's id
password = ''                 # passwrods of sender's id
mail_to = 'abc@gmail.com'		#receiver's mail

session = smtplib.SMTP('smtp.outlook.com', 587)
session.starttls()

message = MIMEMultipart()
message['From'] = mail_from
message['To'] = mail_to
message['Subject'] = 'hey,dear'     # subject of the mail
messagee=' bye'
message.attach(MIMEText(messagee, 'plain'))									# message body

file_path = r'C:\Users\MICROSOFT\OneDrive\Desktop\email task'
file_name = 'english.pdf'
file = open(file_path+'\\'+file_name, 'rb')
payload = MIMEBase('application','pdf')
payload.set_payload((file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition',"attachment", filename=file_name)
message.attach(payload)


session.login(mail_from, password) 
text = message.as_string()
session.sendmail(mail_from,mail_to, text)
session.quit()												#Closing the connection 
print('Mail Sent')