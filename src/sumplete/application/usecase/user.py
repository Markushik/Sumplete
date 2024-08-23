from adaptix.conversion import get_converter

from sumplete.shared.models.user import UserDTO
from sumplete.infrastructure.database.schemas import User
from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.infrastructure.redis.adapter.implement import RedisAdapter

from sumplete.application.usecase.base import Interactor


class UserExist(Interactor[int, bool]):
    def __init__(self, cache: RedisAdapter):
        self.cache = cache

    async def __call__(self, user_id: int) -> bool:
        user = await self.cache.get_user(user_id)
        if user is None:
            return False
        return True


class UserCreate(Interactor[UserDTO, None]):
    def __init__(self, cache: RedisAdapter, uow: UnitOfWork):
        self.cache = cache
        self.uow = uow

    async def __call__(self, data: UserDTO) -> None:
        converter = get_converter(UserDTO, User)
        user = converter(data)

        await self.cache.create_user(
            user_id=user.user_id, user_name=user.user_name, locale=user.locale
        )
        await self.uow.user.create(user)
        await self.uow.commit()


class UserHandler(Interactor[UserDTO, None]):
    def __init__(self, exist: UserExist, create: UserCreate):
        self.exist = exist
        self.create = create

    async def __call__(self, data: UserDTO) -> None:
        if not await self.exist(data.user_id):
            await self.create(data)


class UpdateLocale(Interactor[UserDTO, None]):
    def __init__(self, cache: RedisAdapter, uow: UnitOfWork):
        self.cache = cache
        self.uow = uow

    async def __call__(self, data: UserDTO) -> None:
        await self.cache.update_locale(user_id=data.user_id, locale=data.locale)
        await self.uow.user.update_locale(user_id=data.user_id, locale=data.locale)
        await self.uow.commit()
