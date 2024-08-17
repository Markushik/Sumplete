from sqlalchemy.ext.asyncio import AsyncSession

from ..interfaces.solve import ISolveRepo
from ...schemas.solve import Solve


class SolveRepo(ISolveRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def add(self, data: Solve) -> None:
        self.session.add(data)
        await self.session.flush()
