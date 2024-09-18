from infrastructure.interfaces.mailer_interface import MailerInterface
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector


class SendBulkEmailService:

    @inject
    def __init__(self, mailer: MailerInterface = Provide[Injector.mail]):
        self.mailer = mailer

    async def send_bulk_email(self, list_email):
        await self.mailer.send_bulk(list_email,"Compra recibida")