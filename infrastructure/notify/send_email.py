import ssl
from config import settings
import smtplib
from pydantic import BaseModel, EmailStr
from typing import List
from email.message import EmailMessage
from infrastructure.interfaces.mailer_interface import MailerInterface
from infrastructure.notify.templates.purchase_book_send_email import get_body_book_purchase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
import asyncio


class EmailRequest(BaseModel):
    email: EmailStr

class ListEmailRequest(BaseModel):
    email_list: List[EmailRequest]


class SendEmail(MailerInterface):

    def send_email(self, user_email, subject):
        """Method for send single email"""

        body = get_body_book_purchase()
        mail = EmailMessage()
        mail["From"] = settings.EMAIL
        mail["To"] = user_email
        mail["Subject"] = subject
        mail.set_content(body, subtype='html')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, port=settings.EMAIL_PORT, context=context) as smtp:
            smtp.login(settings.EMAIL, settings.EMAIL_PASSWORD)
            smtp.sendmail(settings.EMAIL, user_email, mail.as_string())

    async def send_bulk(self, list_mails: List[EmailRequest], subject: str):
        loop = asyncio.get_event_loop()
        tasks = []
        for recipient in list_mails:
            tasks.append(loop.run_in_executor(None, SendEmail.send_bulk_mail, recipient.email, subject))

        await asyncio.gather(*tasks)

    @staticmethod
    def send_bulk_mail(recipient: EmailRequest, subject: str):
        """Static method for send bulk emails"""

        body = get_body_book_purchase()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=ssl.create_default_context(),
                              timeout=10) as server:
            try:
                server.login(settings.EMAIL, settings.EMAIL_PASSWORD)
                msg = MIMEMultipart()
                msg['From'] = settings.EMAIL
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'html'))

                server.sendmail(settings.EMAIL, recipient, msg.as_string())

            except Exception as e:
                print(f"Cannot send email to {recipient}. Error: {e}")
