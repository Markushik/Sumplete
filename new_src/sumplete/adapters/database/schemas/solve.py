from sqlalchemy import BigInteger, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseSchema


class Solve(BaseSchema):
    __tablename__ = "solved"

    solve_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.user_id"),
    )
    puzzle_id: Mapped[int] = mapped_column(Integer)
    size: Mapped[int] = mapped_column(SmallInteger)
