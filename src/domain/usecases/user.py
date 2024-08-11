from adaptix.conversion import get_converter

from src.domain.dto.user import UserDTO
from src.infrastructure.database.models.user import User
from src.infrastructure.database.uow.impl import UnitOfWork
from src.infrastructure.redis.gateways.user import UserCacheGateway
from .base import Usecase


class CreateUser(Usecase[UserDTO, None]):
    def __init__(self, uow: UnitOfWork, cache: UserCacheGateway):
        self.uow = uow
        self.cache = cache

    async def __call__(self, data: UserDTO) -> None:
        converter = get_converter(UserDTO, User)
        user = converter(data)

        await self.cache.create(data)
        await self.uow.user.create(user)
        await self.uow.commit()


class UpdateLanguage(Usecase[UserDTO, None]):
    def __init__(self, uow: UnitOfWork, cache: UserCacheGateway):
        self.uow = uow
        self.cache = cache

    async def __call__(self, data: UserDTO) -> None:
        await self.cache.update_lang(data)
        await self.uow.user.update_lang(data)
        await self.uow.commit()
