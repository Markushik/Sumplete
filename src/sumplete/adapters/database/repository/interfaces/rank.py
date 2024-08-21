from typing import Protocol

from ...schemas.rank import Rank


class IRankRepo(Protocol):
    async def write(self, data: ...) -> None: ...

    async def get(self, user_id: int) -> Rank | None: ...
