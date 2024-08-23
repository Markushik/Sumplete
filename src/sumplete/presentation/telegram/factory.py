from typing import AsyncIterable

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage, DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisEventIsolation, RedisStorage
from aiogram_dialog import setup_dialogs
from dishka import AsyncContainer, provide, Provider, Scope
from dishka.integrations.aiogram import setup_dishka

from sumplete.shared.configuration.schemas import BotConfig
from sumplete.infrastructure.redis.factory import RedisFSM
from .dialogs import get_dialogs
from .dialogs.extras.i18n.loader import locales_loader
from .handlers import get_handlers
from .middlewares import setup_middlewares


def setup_routers(disp: Dispatcher):
    disp.include_routers(*get_handlers(), *get_dialogs())


class DispProvider(Provider):
    scope = Scope.APP

    @provide
    def create_dispatcher(
        self,
        container: AsyncContainer,
        storage: BaseStorage,
        event_isolation: BaseEventIsolation,
    ) -> Dispatcher:
        disp = Dispatcher(
            storage=storage,
            event_isolation=event_isolation,
        )

        setup_dishka(container=container, router=disp)
        setup_middlewares(disp=disp, loader=locales_loader())

        setup_routers(disp)
        setup_dialogs(disp)

        return disp

    @provide
    def create_storage(self, redis: RedisFSM) -> BaseStorage:
        return RedisStorage(
            redis=redis,
            key_builder=DefaultKeyBuilder(with_destiny=True),
        )

    @provide
    def get_event_isolation(self, redis: RedisFSM) -> BaseEventIsolation:
        return RedisEventIsolation(redis=redis)


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_bot(self, config: BotConfig) -> AsyncIterable[Bot]:
        async with Bot(
            token=config.token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
            ),
        ) as bot:
            # await bot.set_my_commands(
            #     [
            #         BotCommand(command="/start", description="⠀"),
            #         BotCommand(command="/play", description="⠀"),
            #     ],
            #     scope=BotCommandScopeDefault(),
            # )
            await bot.get_updates(offset=-1)
            yield bot
