import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def loginEmail(email, password, type):
    if type == 'o':
        try:
            s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
            s.starttls()
            if '@gmail'in email:
                return  'fail'
            s.login(email, password)
            return 'success'
        except:
            return "fail"
    elif type == 'g':
        try:
            if '@outlook'in email:
                return 'fail'
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(email, password)
            return 'success'
        except:
            return 'fail'
    else:
        return "fail"


def send_email(email,password,to , subject , body , type):

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] =to
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(body, 'plain'))
    if type == 'o':
        try:
            s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
            s.starttls()
            s.login(email, password)
            s.send_message(msg)
            return 'success'
        except:
            return "fail"
    elif type == 'g':
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(email, password)
                server.send_message(msg)
            return 'success'
        except:
            return 'fail'
    else:
        return "fail"
