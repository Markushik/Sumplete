from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models import Puzzle


class PuzzleRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create(self, data: Puzzle) -> int:
        self.session.add(data)
        await self.session.flush()
        return data.puzzle_id

    async def random(self) -> None:  # a random puzzle
        stmt = select(Puzzle).order_by(func.random()).limit(1)
        return await self.session.scalar(stmt)

    async def search(self, puzzle_id: int):
        return await self.session.get(Puzzle, puzzle_id)
