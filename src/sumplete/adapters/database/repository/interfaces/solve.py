from typing import Protocol

from ...schemas.solve import Solve


class ISolveRepo(Protocol):
    async def create(self, data: Solve) -> None:
        raise NotImplementedError
