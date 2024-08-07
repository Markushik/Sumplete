from typing import Protocol

from src.infrastructure.database.models import User


class IUserRepo(Protocol):
    async def create(self, user: User) -> None:
        ...

    async def update_lang(self, tg_id: int, language: str) -> None:
        ...

    async def update_notify(self, tg_id: int, notify: bool) -> None:
        ...

    async def update_style(self, tg_id: int, style: str) -> None:
        ...

