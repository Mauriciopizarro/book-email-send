from abc import ABC, abstractmethod
from domain.models.purchase import Purchase


class MongoRepositoryInterface(ABC):

    @abstractmethod
    def save(self, purchase: Purchase):
        pass

    # @abstractmethod
    # def get(self, identification_number: int) -> Purchase:
    #     pass

    # @abstractmethod
    # def update(self, purchase: Purchase) -> Purchase:
    #     pass
