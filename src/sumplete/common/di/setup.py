from typing import List

from dishka import AsyncContainer, make_async_container, Provider

from src.sumplete.adapters.database.factory import DatabaseProvider
from src.sumplete.adapters.redis.factory import RedisProvider
from src.sumplete.common.config.loader import get_config
from src.sumplete.common.factory import ConfigProvider
from src.sumplete.domain.factory import UsecaseProvider
from src.sumplete.presentation.telegram.factory import BotProvider, DispProvider


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
