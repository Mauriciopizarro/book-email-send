from infrastructure.repository.email_repository import EmailRepository
from infrastructure.repository.purchase_repository import PurchaseRepository
from dependency_injector import containers, providers
from infrastructure.notify.send_email import SendEmail


class Injector(containers.DeclarativeContainer):

    purchase_repo = providers.Singleton(PurchaseRepository)
    email_repo = providers.Singleton(EmailRepository)
    mail = providers.Singleton(SendEmail)



injector = Injector()
injector.wire(modules=["application.save_purchase_service",
                       "application.send_bulk_email_service",
                       "application.send_email_service",
                       "application.get_all_emails_sent_service"
                       ])
