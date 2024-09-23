from infrastructure.interfaces.mailer_interface import MailerInterface
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
import datetime
from domain.models.email import Email


class SendBulkEmailService:

    @inject
    def __init__(self, mailer: MailerInterface = Provide[Injector.mail],
                 email_repo: EmailRepositoryInterface = Provide[Injector.email_repo]):
        self.mailer = mailer
        self.email_repo = email_repo

    async def send_bulk_email(self, list_email):
        await self.mailer.send_bulk(list_email,"Compra recibida")
        for email in list_email:
            date = datetime.datetime.now()
            mail = Email(email_address=email.email, sent_date=date)
            self.email_repo.save(mail)