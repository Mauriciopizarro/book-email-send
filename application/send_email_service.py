from domain.Exceptions import EmptyEmailException
from infrastructure.notify.send_email import *


class SendEmailService:

    # injection

    def send_single_email(self, email):
        mail = SendEmail()
        if not email:
            raise EmptyEmailException

        mail.send_email(
            user_email=email,
            subject="Compra recibida",
            body=mail.get_purchase_book_email()
        )