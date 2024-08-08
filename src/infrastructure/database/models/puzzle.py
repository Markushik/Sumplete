from sqlalchemy import Integer, SmallInteger
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Puzzle(Base):
    __tablename__ = "puzzles"

    puzzle_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    size: Mapped[int] = mapped_column(SmallInteger)
    original: Mapped[list[int]] = mapped_column(ARRAY(SmallInteger, dimensions=2))
    modified: Mapped[list[int]] = mapped_column(ARRAY(SmallInteger, dimensions=2))
    sums: Mapped[list[int]] = mapped_column(ARRAY(SmallInteger, dimensions=2))
