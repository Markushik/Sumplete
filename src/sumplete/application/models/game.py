from attrs import define


@define
class Setup:
    locale: str
    style: str
    size: int
    complexity: str


@define
class Value:
    id: str
    value: str


@define
class Cell:
    id: str
    values: list[Value]


@define
class Field:
    id: str
    cells: list[Cell]
    solved: list
    unsolved: list


@define
class Meta:
    locale: str
    puzzle_id: int
    size: int
    score: int
    complexity: str


@define
class Game:
    meta: Meta
    field: Field
