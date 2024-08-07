from dataclasses import dataclass


@dataclass(slots=True)
class TokenConfig:
    token: str


@dataclass(slots=True)
class AppConfig:
    level: str  # level logging


@dataclass(slots=True)
class BotConfig:
    storage: str
    # parse_mode: str


@dataclass(slots=True)
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    driver: str = "postgresql+asyncpg"


@dataclass(slots=True)
class RedisConfig:
    host: str
    port: int
    database: int
    database_fsm: int


@dataclass(slots=True)
class Config:
    token: TokenConfig
    app: AppConfig
    bot: BotConfig
    database: DatabaseConfig
    redis: RedisConfig
