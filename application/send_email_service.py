from domain.Exceptions import EmptyEmailException
from infrastructure.interfaces.mailer_interface import MailerInterface
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector


class SendEmailService:

    @inject
    def __init__(self, mailer: MailerInterface = Provide[Injector.mail]):
        self.mailer = mailer

    def send_single_email(self, email):
        if not email:
            raise EmptyEmailException
        self.mailer.send_email(email,"Compra recibida",)