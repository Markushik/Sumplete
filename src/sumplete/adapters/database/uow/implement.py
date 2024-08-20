from sqlalchemy.ext.asyncio import AsyncSession

from ..repository.implements.puzzle import PuzzleRepo
from ..repository.implements.rank import RankRepo
from ..repository.implements.solve import SolveRepo
from ..repository.implements.user import UserRepo

from .interface import IUoW


class UnitOfWork(IUoW):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self):
        self.user = UserRepo(self.session)
        self.puzzle = PuzzleRepo(self.session)
        self.rank = RankRepo(self.session)
        self.solve = SolveRepo(self.session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
