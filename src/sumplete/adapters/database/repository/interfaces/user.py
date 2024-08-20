from typing import Protocol

from ...schemas.user import User


class IUserRepo(Protocol):
    async def create(self, user: User) -> None:
        raise NotImplementedError

    async def get(self, user_id: int) -> User | None:
        raise NotImplementedError

    async def update_locale(self, user_id: int, locale: str) -> None:
        raise NotImplementedError

    async def update_anncmt(self, user_id: int, anncmt: bool) -> None:
        raise NotImplementedError

    async def update_style(self, user_id: int, style: str) -> None:
        raise NotImplementedError

    async def get_style(self, user_id: int) -> str | None:
        raise NotImplementedError
