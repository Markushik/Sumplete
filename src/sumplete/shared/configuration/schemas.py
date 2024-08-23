from attrs import define


@define
class BotConfig:
    token: str
    database: int


@define
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str


@define
class RedisConfig:
    host: str
    port: int
    database: int


@define
class NatsConfig:
    host: str
    port: int


@define
class Config:
    bot: BotConfig
    database: DatabaseConfig
    redis: RedisConfig
    nats: NatsConfig
