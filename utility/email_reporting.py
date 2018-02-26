import os
import smtplib
import sys
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_date = str(datetime.datetime.now())


def email_connection():
    gmail_user = 'test.adityaridha@gmail.com'
    gmail_password = 'ZXasqw12'

    outer = MIMEMultipart()
    outer['From'] = gmail_user
    outer['To'] = 'adityaridharrahman@gmail.com'
    outer['Subject'] = "Mentifi Web Automation Test Report {}".format(current_date[:-10])

    email_body = "Hi," \
                 "\n\nAttached the latest automation report" \
                 "\nif you have any questions or report any problem, please contact : aditya.ridharrahman@geekseat.com.au" \
                 "\n\nThank you"

    outer.attach(MIMEText(email_body,'plain'))

    # List of attachments
    path = os.getcwd()
    attachments = [path + "\\test_report\\report.html"]

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_addr='test.adityaridha@gmail.com', to_addrs='aditya.ridharrahman@geekseat.com.au', msg=composed)
        server.close()
        print("Automation report sent")
    except:
        print("something when wrong")


