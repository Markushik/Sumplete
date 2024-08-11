from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models import Puzzle


class PuzzleRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create(self, puzzle: Puzzle) -> None:
        self.session.add(puzzle)
        await self.session.flush()
