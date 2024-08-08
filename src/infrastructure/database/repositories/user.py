from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.dto.user import UserDTO

from src.infrastructure.database.interfaces.user import IUserRepo
from src.infrastructure.database.models import User


class UserRepo(IUserRepo):
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.flush()

    async def update_lang(self, user: UserDTO) -> None:
        stmt = (
            update(User)
            .where(User.tg_id == user.tg_id)
            .values(language=user.language)
        )
        await self.session.execute(stmt)
        await self.session.flush()

    async def update_notify(self, tg_id: int, notify: bool) -> None:
        stmt = (
            update(User)
            .where(User.tg_id == tg_id)
            .values(notify=notify)
        )
        await self.session.execute(stmt)
        await self.session.flush()

    async def update_style(self, tg_id: int, style: str) -> None:
        stmt = (
            update(User).where(User.tg_id == tg_id).values(style=style)  # type: ignore
        )
        await self.session.execute(stmt)
        await self.session.flush()
