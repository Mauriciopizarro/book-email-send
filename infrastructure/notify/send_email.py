import ssl
from config import settings
import smtplib
from email.message import EmailMessage
from infrastructure.notify.templates.purchase_book_send_email import get_body_book_purchase


class SendEmail:

    def __init__(self):
        self.email_sender = settings.EMAIL
        self.email_password = settings.EMAIL_PASSWORD

    def send_email(self, user_email, subject, body):
        mail = EmailMessage()
        mail["From"] = self.email_sender
        mail["To"] = user_email
        mail["Subject"] = subject
        mail.set_content(body, subtype='html')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, port=settings.EMAIL_PORT, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, user_email, mail.as_string())

    @staticmethod
    def get_purchase_book_email():
        return get_body_book_purchase()
