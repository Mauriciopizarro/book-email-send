from domain.models.purchase import Purchase
from infrastructure.interfaces.purchase_repository_interface import PurchaseRepositoryInterface
from config import settings
from pymongo import MongoClient


class PurchaseRepository(PurchaseRepositoryInterface):

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
        return client['books']["purchase"]

    def save(self, purchase: Purchase):
        purchase_dict = purchase.dict()
        self.db.insert_one(purchase_dict)
