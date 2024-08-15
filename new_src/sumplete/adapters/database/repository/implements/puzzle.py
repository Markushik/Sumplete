from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..interfaces.puzzle import IPuzzleRepo
from ...schemas.puzzle import Puzzle


class PuzzleRepo(IPuzzleRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, data: Puzzle) -> None:
        self.session.add(data)
        await self.session.flush()

    async def random(self) -> Puzzle:
        request = select(Puzzle).order_by(func.random()).limit(1)
        puzzle = await self.session.scalar(request)
        return puzzle

    async def search(self, puzzle_id: int) -> Puzzle | None:
        puzzle = await self.session.get(Puzzle, puzzle_id)
        return puzzle
