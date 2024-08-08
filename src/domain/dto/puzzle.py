from typing import List

from attr import define, field

from src.domain.entities.game import Cell


@define(slots=True)
class PuzzleSetup:
    use: bool = field(default=False)
    size: int | None = field(default=None)
    complexity: str | None = field(default=None)


@define(slots=True)
class GameField:
    id: str
    cells: List[Cell]
