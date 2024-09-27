from infrastructure.interfaces.mailer_interface import MailerInterface
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface
import datetime
from domain.models.email import Email


class SendBulkEmailService:

    def __init__(self, mailer: MailerInterface , email_repo: EmailRepositoryInterface):
        self.mailer = mailer
        self.email_repo = email_repo

    async def send_bulk_email(self, list_email):
        await self.mailer.send_bulk(list_email,"Compra recibida")
        for email in list_email:
            date = datetime.datetime.now()
            mail = Email(email_address=email.email, sent_date=date)
            self.email_repo.save(mail)