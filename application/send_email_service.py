import datetime
from domain.models.email import Email
from domain.Exceptions.MailAlreadySentException import MailAlreadySentException
from domain.Exceptions.EmptyEmailException import EmptyEmailException
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface
from infrastructure.interfaces.mailer_interface import MailerInterface

class SendEmailService:

    def __init__(self, mailer: MailerInterface, email_repo: EmailRepositoryInterface):
        self.mailer = mailer
        self.email_repo = email_repo

    def send_single_email(self, email, has_force: bool):
        if not email:
            raise EmptyEmailException()
        if not has_force:
            has_email_already_sent = self.email_repo.get_by_email(email)
            if has_email_already_sent:
                raise MailAlreadySentException()
        self.mailer.send_email(email,"Compra recibida")
        date = datetime.datetime.now()
        mail = Email(email_address=email, sent_date=date)
        self.email_repo.save(mail)
