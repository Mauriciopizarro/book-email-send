from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface


class AllEmailsSentService:

    def __init__(self, email_repo: EmailRepositoryInterface):
        self.email_repo = email_repo

    def get_all_emails_sent(self):
        return self.email_repo.get_all_emails_sent()