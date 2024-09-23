import datetime
from domain.Exceptions import EmptyEmailException
from dependency_injector.wiring import Provide, inject
from domain.models.email import Email
from infrastructure.injector import Injector
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface
from infrastructure.interfaces.mailer_interface import MailerInterface

class SendEmailService:

    @inject
    def __init__(self, mailer: MailerInterface = Provide[Injector.mail],
                 email_repo: EmailRepositoryInterface = Provide[Injector.email_repo]):
        self.mailer = mailer
        self.email_repo = email_repo

    def send_single_email(self, email):
        if not email:
            raise EmptyEmailException

        self.mailer.send_email(email,"Compra recibida")
        date = datetime.datetime.now()
        mail =  Email(email_address=email, sent_date=date)
        self.email_repo.save(mail)
