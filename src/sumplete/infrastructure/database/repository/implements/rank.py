from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, func, select

from ...schemas.rank import Rank

from ..interfaces.rank import IRankRepo


class RankRepo(IRankRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def get(self, user_id: int) -> Rank | None:
        rank = await self.session.get(Rank, user_id)
        return rank

    async def create(self, rank: Rank) -> None:
        self.session.add(rank)
        await self.session.flush()

    async def update(self, user_id: int, score: int) -> None:
        request = (
            update(Rank).where(Rank.user_id == user_id).values(score=Rank.score + score)
        )
        await self.session.execute(request)
        await self.session.flush()

    async def sampling(self):
        request = select(Rank).order_by(Rank.score.desc()).limit(10)
        ranks = await self.session.scalars(request)
        return ranks
