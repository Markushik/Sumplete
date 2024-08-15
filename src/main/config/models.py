from attrs import define


@define(slots=True)
class BotConfig:
    token: str
    database: int


@define(slots=True)
class CommonConfig:
    level: str


@define(slots=True)
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str


@define(slots=True)
class RedisConfig:
    host: str
    port: int
    database: int


@define(slots=True)
class NatsConfig:
    host: str
    port: int


@define(slots=True)
class Config:
    bot: BotConfig
    common: CommonConfig
    database: DatabaseConfig
    redis: RedisConfig
    nats: NatsConfig
