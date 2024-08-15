from attrs import define

from new_src.sumplete.domain.base.schema import BaseSchema


@define(slots=True)
class BotConfig(BaseSchema):
    token: str
    database: int


@define(slots=True)
class CommonConfig(BaseSchema):
    level: str


@define(slots=True)
class DatabaseConfig(BaseSchema):
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str


@define(slots=True)
class RedisConfig(BaseSchema):
    host: str
    port: int
    database: int


@define(slots=True)
class NatsConfig(BaseSchema):
    host: str
    port: int


@define(slots=True)
class Config(BaseSchema):
    bot: BotConfig
    common: CommonConfig
    database: DatabaseConfig
    redis: RedisConfig
    nats: NatsConfig
