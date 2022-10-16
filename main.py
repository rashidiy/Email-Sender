import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_EMAIL = 'your_email@example.com'
APP_PASSWORD = 'your_app_password'


class Email:
    def __init__(self, from_email, app_password):
        self.MY_EMAIL = from_email
        self.APP_PASSWORD = app_password

    def send_text(self, to_email, text, subject: str = None, type_: str = 'plain'):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.MY_EMAIL
        msg['To'] = to_email
        msg.attach(MIMEText(text, type_))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(MY_EMAIL, self.APP_PASSWORD)
            smtp.send_message(msg)

    def send_file(self, to_email: str, file_path: str, subject: str = None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.MY_EMAIL
        msg['To'] = to_email
        filename = file_path
        with open(filename) as file:
            attachment = MIMEText(file.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attachment)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.MY_EMAIL, self.APP_PASSWORD)
            smtp.send_message(msg)
