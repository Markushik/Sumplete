from typing import List

from dishka import AsyncContainer, make_async_container, Provider

from src.domain.factory import UsecaseProvider
from src.infrastructure.database.factory import DatabaseProvider
from src.infrastructure.redis.factory import RedisProvider
from src.main.config.factory import ConfigProvider
from src.main.config.loader import get_config
from src.presentation.tgbot.factory import BotProvider, DispProvider


def providers() -> List[Provider]:
    return [
        ConfigProvider(get_config()),
        RedisProvider(),
        DatabaseProvider(),
        UsecaseProvider(),
        BotProvider(),
        DispProvider(),
    ]


def setup_dishka() -> AsyncContainer:
    container = make_async_container(*providers())
    return container
