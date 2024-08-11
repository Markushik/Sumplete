from typing import List

from attrs import field, define

from src.domain.entities.game import Cell


@define(slots=True, kw_only=True)
class PuzzleDTO:
    puzzle_id: int = field(default=None)
    size: int
    score: int
    complexity: str
    index_sample: list[int]
    original_array: list[int]
    zeroed_array: list[int]
    modified_array: list[int]
    vertical_sums: list[int]
    horizontal_sums: list[int]


@define(slots=True)  # todo: to entity
class PuzzleSetup:
    size: int
    complexity: str


@define(slots=True)
class GameField:
    id: str
    cells: List[Cell]
    solved: list
    unsolved: list
