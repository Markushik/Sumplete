from sqlalchemy.ext.asyncio import AsyncSession

from ..interfaces.rank import IRankRepo
from ...schemas.rank import Rank


class RankRepo(IRankRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def add(self, data: Rank) -> None:
        await self.session.merge(data)
        await self.session.flush()
