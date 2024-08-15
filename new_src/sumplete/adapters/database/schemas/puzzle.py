from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseSchema


class Puzzle(BaseSchema):
    __tablename__ = "puzzles"
    __mapper_args__ = {"eager_defaults": True}  # database to return fill UserSchema

    puzzle_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    size: Mapped[int] = mapped_column(SmallInteger)
    score: Mapped[int] = mapped_column(SmallInteger)
    complexity: Mapped[str] = mapped_column(String(10))
    sample: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    original: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    zeroed: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    modified: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    vertical: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    horizontal: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )

    def __repr__(self) -> str:
        return f"Puzzle: {self.puzzle_id}:{self.size}:{self.complexity}"
