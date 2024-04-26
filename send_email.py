from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def Send_Report_Email():
    File_Name =f'Benaa_Monthly_Report'

    sender_email = ''
    email_password = ''

    bcc = "a.kzem@tatbeek.com"

    receiver_email = ['abduallahkazem19@gmail.com']

    rcpt = bcc.split(",") + receiver_email

    subject = 'Shift Report by Tatbeek'

    email_server_host = 'smtp.gmail.com'
    Port = 587

    msg = MIMEMultipart()
    msg['From'] = 'Tatbeek Team'
    msg['To'] = ", ".join(receiver_email)
    msg['Subject'] = subject
    Body = f'''Monthly Report for: May'''
    msg.attach(MIMEText(Body, 'plain'))
    attach_file_name = File_Name + '.pdf'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=attach_file_name)
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    msg.attach(payload)

    server = smtplib.SMTP(host=email_server_host, port=Port)
    server.starttls()
    server.login(sender_email, email_password)
    server.sendmail(sender_email, rcpt, msg.as_string())
    server.close()


Send_Report_Email()
