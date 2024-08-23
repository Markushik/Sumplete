from typing import Protocol

from ...schemas.puzzle import Puzzle


class IPuzzleRepo(Protocol):
    async def create(self, data: Puzzle) -> None:
        raise NotImplementedError

    async def random(self) -> Puzzle:
        raise NotImplementedError

    async def search(self, puzzle_id: int) -> Puzzle | None:
        raise NotImplementedError
