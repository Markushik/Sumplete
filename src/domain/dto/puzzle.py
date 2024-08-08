from typing import List

from attr import field, dataclass

from src.domain.entities.game import Cell


@dataclass(slots=True)
class PuzzleSetup:
    use: bool = field(default=False)
    size: int | None = field(default=None)
    complexity: str | None = field(default=None)


@dataclass(slots=True)
class GameField:
    id: str
    cells: List[Cell]
