"""Sender email """
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from modelos import EMAIL_DEF


def send_email(recieve, recipients, certificate_files):
    """
        Function to send email with attachments of certificates.
        Send multiple certificates if needed. 
        Pay attention to email limits for attachments. 25MB per email on Gmail.
        Arguments:
            recieve : Name of the recipient
            recipients : Email address or list of email addresses
            certificate_files : List of certificate file paths to attach
    """
    load_dotenv()
    password = os.getenv('PASS')
    sender = os.getenv('EMAIL')
    message = MIMEMultipart()

    body_msg = MIMEText((EMAIL_DEF['email_body'] % recieve), 'html')
    message['From'] = sender
    message['To'] = recipients if isinstance(recipients, str) else ', '.join(recipients)
    message["Subject"] = EMAIL_DEF["emai_subject"]
    message.attach(body_msg)
    with open('log-sbf.png', 'rb') as fp:
        msg_image = MIMEImage(fp.read())
        msg_image.add_header('Content-ID', '<sbf_logo>')
        message.attach(msg_image)

    # section 1 to attach file
    for certificate_file in certificate_files:
        with open(certificate_file, 'rb') as file:
            # Attach the file with filename to the email
            name = os.path.basename(certificate_file).split('/')[-1]
            message.attach(
                MIMEApplication(file.read(),
                                Name=name)
                                )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, message.as_string())
    print("Message sent!")
