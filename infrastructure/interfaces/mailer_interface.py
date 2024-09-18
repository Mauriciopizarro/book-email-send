from abc import ABC, abstractmethod


class MailerInterface(ABC):

    @abstractmethod
    def send_email(self, email, subject):
        pass

    @abstractmethod
    def send_bulk(self, email_list, subject):
        pass
