from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...schemas.solve import Solve

from ..interfaces.solve import ISolveRepo


class SolveRepo(ISolveRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, data: Solve) -> None:
        self.session.add(data)
        await self.session.flush()

    async def check(self, user_id: int, puzzle_id: int):
        request = select(Solve.solve_id).where(
            Solve.user_id == user_id, Solve.puzzle_id == puzzle_id
        )
        return await self.session.scalar(request)
