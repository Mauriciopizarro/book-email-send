from dependency_injector.wiring import Provide, inject
from domain.models.purchase import Purchase
from infrastructure.injector import Injector
from infrastructure.interfaces.mongo_repository_interface import MongoRepositoryInterface


class SavePurchaseService:

    @inject
    def __init__(self, purchase_repository: MongoRepositoryInterface = Provide[Injector.purchase_repo]):
        self.purchase_repository = purchase_repository


    def save_purchase(self, save_request_data):
        purchase = Purchase(**save_request_data)
        self.purchase_repository.save(purchase)