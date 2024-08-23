import sqlalchemy as sa
from yarl import URL

from sumplete.shared.configuration.schemas import DatabaseConfig, NatsConfig, RedisConfig


def build_database_url(config: DatabaseConfig) -> sa.URL:
    return sa.URL.create(
        drivername=config.driver,
        username=config.username,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database,
    )


def build_redis_url(config: RedisConfig) -> str:
    url = URL.build(
        scheme="redis", host=config.host, port=config.port, path=f"/{config.database}"
    )
    return url.human_repr()


def build_nats_url(config: NatsConfig) -> str:
    url = URL.build(scheme="nats", host=config.host, port=config.port)
    return url.human_repr()
