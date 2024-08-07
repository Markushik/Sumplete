from adaptix.conversion import get_converter

from src.domain.dto.user import UserDTO
from src.infrastructure.database.uow.impl import UnitOfWork
from src.infrastructure.redis.gateways.user import UserCacheGateway
from .base import Usecase
from ...infrastructure.database.models import User


class CreateUser(Usecase[UserDTO, None]):
    def __init__(self, uow: UnitOfWork, cache: UserCacheGateway):
        self.uow = uow
        self.cache = cache

    async def __call__(self, data: UserDTO) -> None:
        converter = get_converter(UserDTO, User)
        user = converter(data)

        await self.cache.create(data)
        await self.uow.user_repo.create(user)
        await self.uow.commit()


class UpdateLanguage(Usecase):
    def __init__(
            self, uow: UnitOfWork, cache: UserCacheGateway
    ):
        self.uow = uow
        self.cache = cache

    async def __call__(self, data: UserDTO) -> None:
        await self.cache.update_lang(data)
        await self.uow.user_repo.update_lang(data)
        await self.uow.commit()
