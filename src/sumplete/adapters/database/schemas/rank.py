from sqlalchemy import BigInteger, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseSchema


class Rank(BaseSchema):
    __tablename__ = "ranking"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_id"), primary_key=True
    )
    score: Mapped[int] = mapped_column(Integer)
