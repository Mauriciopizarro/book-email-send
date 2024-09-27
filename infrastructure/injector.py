from application.get_all_emails_sent_service import AllEmailsSentService
from application.save_purchase_service import SavePurchaseService
from application.send_bulk_email_service import SendBulkEmailService
from application.send_email_service import SendEmailService
from infrastructure.repository.email_repository import EmailRepository
from infrastructure.repository.purchase_repository import PurchaseRepository
from dependency_injector import containers, providers
from infrastructure.notify.send_email import SendEmail


class Injector(containers.DeclarativeContainer):

    purchase_repo = providers.Singleton(PurchaseRepository)
    email_repo = providers.Singleton(EmailRepository)
    mail = providers.Singleton(SendEmail)

    #services injection
    send_bulk_email_service = providers.Factory(SendBulkEmailService, mailer=mail, email_repo=email_repo)
    send_email_service = providers.Factory(SendEmailService, mailer=mail, email_repo=email_repo)
    save_purchase_service = providers.Factory(SavePurchaseService, purchase_repository=purchase_repo)
    get_all_emails_service = providers.Factory(AllEmailsSentService, email_repo=email_repo)

    wiring_config = containers.WiringConfiguration(modules=["infrastructure.controllers.send_bulk_email_controller",
                                                            "infrastructure.controllers.send_single_email_controller",
                                                            "infrastructure.controllers.save_purchase_controller",
                                                            "infrastructure.controllers.get_all_emails_sent_controller"
                                                            ])


# injector = Injector()
# injector.wire(modules=["application.save_purchase_service",
#                        "infrastructure.controllers.send_bulk_email_controller",
#                        "application.send_email_service",
#                        "application.get_all_emails_sent_service"
#                        ])
