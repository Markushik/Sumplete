from typing import AsyncIterable

from dishka import provide, Provider, Scope
from redis.asyncio import ConnectionPool, Redis

from src.infrastructure.redis.gateways.user import UserCacheGateway
from src.main.builders import create_redis_url
from src.main.config.models import RedisConfig


class RedisFSM(Redis):
    pass


class ConnectionPoolFSM(ConnectionPool):
    pass


class RedisProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_pool(self, config: RedisConfig) -> AsyncIterable[ConnectionPool]:
        pool = ConnectionPool.from_url(
            create_redis_url(config), decode_responses=True, protocol=3
        )
        yield pool

        await pool.aclose()

    @provide(scope=Scope.APP)
    async def create_redis(self, pool: ConnectionPool) -> Redis:
        redis = Redis(connection_pool=pool)
        return redis

    @provide(scope=Scope.REQUEST)
    async def create_adapter(self, redis: Redis) -> UserCacheGateway:
        return UserCacheGateway(redis=redis)

    @provide(scope=Scope.APP)
    async def create_fsm_pool(self, config: RedisConfig) -> AsyncIterable[ConnectionPoolFSM]:
        pool = ConnectionPoolFSM(
            host=config.host, port=config.port, db=config.database_fsm,
        )
        yield pool

        await pool.aclose()

    @provide(scope=Scope.APP)
    async def create_fsm_redis(self, pool: ConnectionPoolFSM) -> RedisFSM:
        return RedisFSM(connection_pool=pool)
