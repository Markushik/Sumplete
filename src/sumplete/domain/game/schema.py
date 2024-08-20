from attrs import define


@define(slots=True)
class Setup:
    locale: str
    style: str
    size: int
    complexity: str


@define(slots=True)
class Value:
    id: str
    value: str


@define(slots=True)
class Cell:
    id: str
    values: list[Value]


@define(slots=True)
class Field:
    id: str
    cells: list[Cell]
    solved: list
    unsolved: list


@define(slots=True)
class Meta:
    locale: str
    puzzle_id: int
    size: int
    score: int
    complexity: str


@define(slots=True)
class Game:
    meta: Meta
    field: Field
