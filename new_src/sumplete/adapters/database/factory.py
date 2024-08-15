from typing import AsyncIterable

from dishka import provide, Provider, Scope
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from new_src.sumplete.common.builder.url import build_database_url
from .uow.implement import UnitOfWork
from new_src.sumplete.common.config.schemas import DatabaseConfig


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_async_engine(
        self, config: DatabaseConfig
    ) -> AsyncIterable[AsyncEngine]:
        async_engine = create_async_engine(url=build_database_url(config), echo=True)
        yield async_engine
        await async_engine.dispose()

    @provide(scope=Scope.APP)
    async def get_session_maker(
        self, async_engine: AsyncEngine
    ) -> AsyncIterable[async_sessionmaker]:
        yield async_sessionmaker(
            bind=async_engine, autoflush=False, expire_on_commit=False
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, async_session_maker: async_sessionmaker
    ) -> AsyncIterable[AsyncSession]:
        async with async_session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def get_uow(self, session: AsyncSession) -> UnitOfWork:
        async with UnitOfWork(session=session) as uow:
            return uow
