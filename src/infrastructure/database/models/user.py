from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(64), default=None)
    username: Mapped[str] = mapped_column(String(32))
    language: Mapped[str] = mapped_column(String(5), default="en_GB")
    notify: Mapped[bool] = mapped_column(Boolean, default=False)
    style: Mapped[str] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"User(id={self.tg_id!r}, name={self.first_name!r})"
