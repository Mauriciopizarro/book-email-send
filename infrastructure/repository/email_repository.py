from domain.models.email import Email
from infrastructure.interfaces.mail_repository_interface import EmailRepositoryInterface
from infrastructure.interfaces.purchase_repository_interface import PurchaseRepositoryInterface
from config import settings
from pymongo import MongoClient


class EmailRepository(EmailRepositoryInterface):

    instance = None

    def __init__(self):
        self.db = self.get_database()

    # singleton pattern
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    @staticmethod
    def get_database():
        client = MongoClient(settings.DATABASE_MONGO_URL)
        return client['books']["email"]

    def save(self, email: Email):
        email_dict = email.dict()
        self.db.insert_one(email_dict)

    def get_all_emails_sent(self):
        all_sent_emails = list(self.db.find({}))
        return all_sent_emails