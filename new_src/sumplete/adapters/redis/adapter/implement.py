from redis.asyncio import Redis

from .interface import IRedisAdapter


class RedisAdapter(IRedisAdapter):
    def __init__(self, redis: Redis):
        self.redis = redis

    async def create_user(self, user_id: int, user_name: str, locale: str) -> None:
        await self.redis.hset(
            name=str(user_id),
            mapping={"locale": locale, "user_name": user_name},
        )

    async def get_user(self, user_id: int) -> str | None:
        return await self.redis.hget(str(user_id), "user_name")

    async def update_locale(self, user_id: int, locale: str) -> None:
        await self.redis.hset(name=str(user_id), mapping={"locale": locale})

    async def get_locale(self, user_id: int) -> str | None:
        return await self.redis.hget(str(user_id), "locale")
