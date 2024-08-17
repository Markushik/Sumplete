from typing import Protocol

from ...schemas.solve import Solve


class ISolveRepo(Protocol):
    async def add(self, data: Solve) -> None:
        raise NotImplementedError
