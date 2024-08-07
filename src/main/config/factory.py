from dishka import provide, Provider, Scope

from src.main.config.models import (
    AppConfig,
    BotConfig,
    Config,
    DatabaseConfig,
    RedisConfig,
    TokenConfig,
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
    def get_token_config(self) -> TokenConfig:
        return self.config.token

    @provide
    def get_app_config(self) -> AppConfig:
        return self.config.app

    @provide
    def get_bot_config(self) -> BotConfig:
        return self.config.bot

    @provide
    def get_database_config(self) -> DatabaseConfig:
        return self.config.database

    @provide
    def get_redis_config(self) -> RedisConfig:
        return self.config.redis
