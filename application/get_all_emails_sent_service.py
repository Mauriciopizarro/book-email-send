from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface


class AllEmailsSentService:

    @inject
    def __init__(self, email_repo: EmailRepositoryInterface = Provide[Injector.email_repo]):
        self.email_repo = email_repo

    def get_all_emails_sent(self):
        return self.email_repo.get_all_emails_sent()