from typing import Protocol

from ...schemas.rank import Rank


class IRankRepo(Protocol):
    async def add(self, data: Rank) -> None:
        raise NotImplementedError
