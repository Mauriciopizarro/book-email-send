from abc import ABC, abstractmethod
from domain.models.email import Email


class EmailRepositoryInterface(ABC):

    @abstractmethod
    def save(self, email: Email):
        pass

    @abstractmethod
    def get_all_emails_sent(self):
        pass

    # @abstractmethod
    # def update(self, purchase: Purchase) -> Purchase:
    #     pass
