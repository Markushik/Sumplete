from typing import Protocol


class IRedisAdapter(Protocol):
    async def create_user(self, user_id: int, user_name: str, locale: str) -> None:
        raise NotImplementedError

    async def get_user(self, tg_id: int) -> str | None:
        raise NotImplementedError

    async def update_locale(self, user_id: int, locale: str) -> None:
        raise NotImplementedError

    async def get_locale(self, tg_id: int) -> str | None:
        raise NotImplementedError
