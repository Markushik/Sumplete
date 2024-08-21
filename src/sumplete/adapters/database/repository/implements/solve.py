from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas.solve import Solve

from ..interfaces.solve import ISolveRepo


class SolveRepo(ISolveRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def create(self, data: Solve) -> None:
        self.session.add(data)
        await self.session.flush()
