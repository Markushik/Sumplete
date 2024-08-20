from typing import Protocol

from ...schemas.rank import Rank


class IRankRepo(Protocol):
    async def create(self, data: ...) -> Rank: ...

    async def update_(self, user_id: int, score: int): ...

    async def get(self) -> Rank: ...
