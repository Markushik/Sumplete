from adaptix.conversion import get_converter
from attrs import define, field

from new_src.sumplete.adapters.database.schemas import User
from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from new_src.sumplete.adapters.redis.adapter.implement import RedisAdapter
from ..base.usecase import Usecase


@define(slots=True, kw_only=True)
class UserDTO:
    user_id: int
    user_name: str = field(default=None)
    locale: str = field(default="en")
    anncmt: str = field(default="off")
    style: str = field(default="emoji")


class UserExist(Usecase[int, bool]):
    def __init__(self, cache: RedisAdapter):
        self.cache = cache

    async def __call__(self, user_id: int) -> bool:
        user = await self.cache.get_user(user_id)
        if user is None:
            return False
        return True


class UserCreate(Usecase[UserDTO, None]):
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


class UserHandler(Usecase[UserDTO, None]):
    def __init__(self, exist: UserExist, create: UserCreate):
        self.exist = exist
        self.create = create

    async def __call__(self, data: UserDTO) -> None:
        if not await self.exist(data.user_id):
            await self.create(data)


class UpdateLocale(Usecase[UserDTO, None]):
    def __init__(self, cache: RedisAdapter, uow: UnitOfWork):
        self.cache = cache
        self.uow = uow

    async def __call__(self, data: UserDTO) -> None:
        await self.cache.update_locale(user_id=data.user_id, locale=data.locale)
        await self.uow.user.update_locale(user_id=data.user_id, locale=data.locale)
        await self.uow.commit()
