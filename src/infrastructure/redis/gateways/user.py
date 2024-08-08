from redis.asyncio import Redis

from src.domain.dto.user import UserDTO


class UserCacheGateway:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def create(self, data: UserDTO):
        await self.redis.hset(
            name=str(data.tg_id),
            mapping={"lang": data.language, "first_name": data.first_name},
        )

    async def get(self, tg_id: int) -> str | None:
        return await self.redis.hget(str(tg_id), "first_name")

    async def get_lang(self, tg_id: int):
        return await self.redis.hget(str(tg_id), "lang")

    async def update_lang(self, data: UserDTO):
        return await self.redis.hset(
            name=str(data.tg_id), mapping={"lang": data.language}
        )
