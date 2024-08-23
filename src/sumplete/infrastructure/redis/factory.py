from typing import AsyncIterable

from dishka import provide, Provider, Scope
from redis.asyncio import ConnectionPool, Redis

from sumplete.infrastructure.builder.url import build_redis_url
from sumplete.shared.configuration.schemas import Config, RedisConfig
from sumplete.infrastructure.redis.adapter.implement import RedisAdapter


class RedisFSM(Redis): ...


class ConnectionPoolFSM(ConnectionPool): ...


class RedisProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_pool(self, config: RedisConfig) -> AsyncIterable[ConnectionPool]:
        pool = ConnectionPool.from_url(
            build_redis_url(config), decode_responses=True, protocol=3
        )
        yield pool
        await pool.aclose()

    @provide(scope=Scope.APP)
    async def create_redis(self, pool: ConnectionPool) -> Redis:
        redis = Redis(connection_pool=pool)
        return redis

    @provide(scope=Scope.REQUEST)
    async def create_adapter(self, redis: Redis) -> RedisAdapter:
        return RedisAdapter(redis=redis)

    @provide(scope=Scope.APP)
    async def create_fsm_pool(self, config: Config) -> AsyncIterable[ConnectionPoolFSM]:
        pool = ConnectionPoolFSM(
            host=config.redis.host,
            port=config.redis.port,
            db=config.bot.database,
        )
        yield pool
        await pool.aclose()

    @provide(scope=Scope.APP)
    async def create_fsm_redis(self, pool: ConnectionPoolFSM) -> RedisFSM:
        return RedisFSM(connection_pool=pool)
