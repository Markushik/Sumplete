from sqlalchemy import Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Puzzle(Base):
    __tablename__ = "puzzles"

    puzzle_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    score: Mapped[int] = mapped_column(SmallInteger)
    size: Mapped[int] = mapped_column(SmallInteger)
    complexity: Mapped[str] = mapped_column(String(10))

    index_sample: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    original_array: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    zeroed_array: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    modified_array: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    vertical_sums: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
    horizontal_sums: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger, dimensions=1, zero_indexes=True)
    )
