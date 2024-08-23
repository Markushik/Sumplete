from dishka import provide, Provider, Scope


from sumplete.application.usecase.game import CreatePuzzle, SaveField, SearchPuzzle, ResultPuzzle
from sumplete.application.usecase.user import UpdateLocale, UserCreate, UserExist, UserHandler
from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.infrastructure.redis.adapter.implement import RedisAdapter


class UsecaseProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def user_create(self, cache: RedisAdapter, uow: UnitOfWork) -> UserCreate:
        return UserCreate(cache=cache, uow=uow)

    @provide
    async def user_exist(self, cache: RedisAdapter) -> UserExist:
        return UserExist(cache=cache)

    @provide
    async def user_handler(self, exist: UserExist, create: UserCreate) -> UserHandler:
        return UserHandler(exist=exist, create=create)

    @provide
    async def update_locale(self, cache: RedisAdapter, uow: UnitOfWork) -> UpdateLocale:
        return UpdateLocale(cache=cache, uow=uow)

    @provide
    async def field_save(self, uow: UnitOfWork) -> SaveField:
        return SaveField(uow=uow)

    @provide
    async def puzzle_create(self, save: SaveField) -> CreatePuzzle:
        return CreatePuzzle(save=save)

    @provide
    async def puzzle_search(self) -> SearchPuzzle:
        return SearchPuzzle()

    @provide
    async def puzzle_result(self, uow: UnitOfWork) -> ResultPuzzle:
        return ResultPuzzle(uow=uow)
