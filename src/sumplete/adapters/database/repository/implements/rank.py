from sqlalchemy.ext.asyncio import AsyncSession

from ...schemas.rank import Rank

from ..interfaces.rank import IRankRepo


class RankRepo(IRankRepo):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    ...
