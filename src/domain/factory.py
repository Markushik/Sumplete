from dishka import provide, Provider, Scope

from src.infrastructure.database.uow.impl import UnitOfWork
from src.infrastructure.redis.gateways.user import UserCacheGateway
from src.domain.usecases.user import CreateUser, UpdateLanguage


class UsecaseProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def create_user(self, uow: UnitOfWork, cache: UserCacheGateway) -> CreateUser:
        return CreateUser(uow, cache)

    @provide
    async def update_language(self, uow: UnitOfWork, cache: UserCacheGateway) -> UpdateLanguage:
        return UpdateLanguage(uow, cache)
