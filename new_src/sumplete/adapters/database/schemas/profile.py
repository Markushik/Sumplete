from sqlalchemy import Integer, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSchema


class Profile(BaseSchema):
    __tablename__ = "profile"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_id"), primary_key=True
    )
    scores: Mapped[int] = mapped_column(Integer)
    solved_3x3: Mapped[int] = mapped_column(Integer)
    solved_4x4: Mapped[int] = mapped_column(Integer)
    solved_5x5: Mapped[int] = mapped_column(Integer)
    solved_6x6: Mapped[int] = mapped_column(Integer)

    # user = relationship("User", back_populates="profile")

    def __repr__(self) -> str:
        return f"Profile: {self.user_id}:{self.scores}"
