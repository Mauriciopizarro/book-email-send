from infrastructure.repository.mongo_repository import MongoRepository
from dependency_injector import containers, providers
from infrastructure.notify.send_email import SendEmail


class Injector(containers.DeclarativeContainer):

    purchase_repo = providers.Singleton(MongoRepository)
    mail = providers.Singleton(SendEmail)



injector = Injector()
injector.wire(modules=["application.save_purchase_service",
                       "application.send_bulk_email_service",
                       "application.send_email_service"])
