import sqlalchemy as sa
from yarl import URL

from src.main.config.models import DatabaseConfig, RedisConfig


def create_database_url(config: DatabaseConfig) -> sa.URL:
    return sa.URL.create(
        drivername=config.driver, username=config.username, password=config.password,
        host=config.host, port=config.port, database=config.database
    )


def create_redis_url(config: RedisConfig) -> str:
    url = URL.build(
        scheme='redis', host=config.host,
        port=config.port, path=f'/{config.database}'
    )
    return url.human_repr()
