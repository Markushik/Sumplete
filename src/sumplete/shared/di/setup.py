from typing import List

from dishka import AsyncContainer, make_async_container, Provider

from sumplete.shared.configuration.factory import ConfigProvider
from sumplete.shared.configuration.loader import get_config
from sumplete.presentation.telegram.factory import DispProvider, BotProvider
from sumplete.application.factory import UsecaseProvider
from sumplete.infrastructure.database.factory import DatabaseProvider
from sumplete.infrastructure.redis.factory import RedisProvider


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
