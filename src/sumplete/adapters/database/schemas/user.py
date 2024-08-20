from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseSchema


class User(BaseSchema):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    locale: Mapped[str] = mapped_column(String(2), default="en")
    anncmt: Mapped[str] = mapped_column(String(5), default="off")
    style: Mapped[str] = mapped_column(String(10), default="emoji")

    def __repr__(self) -> str:
        return f"User: {self.user_id}:{self.user_name}"
