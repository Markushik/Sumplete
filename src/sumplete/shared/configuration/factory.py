from dishka import provide, Provider, Scope

from sumplete.shared.configuration.schemas import (
    BotConfig,
    Config,
    DatabaseConfig,
    NatsConfig,
    RedisConfig,
)


class ConfigProvider(Provider):
    scope = Scope.APP

    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @provide
    def get_config(self) -> Config:
        return self.config

    @provide
    def get_bot_config(self) -> BotConfig:
        return self.config.bot

    @provide
    def get_database_config(self) -> DatabaseConfig:
        return self.config.database

    @provide
    def get_redis_config(self) -> RedisConfig:
        return self.config.redis

    @provide
    def get_nats_config(self) -> NatsConfig:
        return self.config.nats
