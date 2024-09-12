from infrastructure.repository.mongo_repository import MongoRepository
from dependency_injector import containers, providers


class Injector(containers.DeclarativeContainer):

    purchase_repo = providers.Singleton(MongoRepository)



injector = Injector()
injector.wire(modules=["application.save_purchase_service"])
