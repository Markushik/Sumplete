import random
from string import ascii_letters, digits

import numpy
from adaptix.conversion import get_converter
from attrs import define, field, asdict
from numpy.random import randint, choice

from new_src.sumplete.adapters.database.schemas import Puzzle, Solve, Rank
from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from .schema import Cell, Value, Field, Setup, Game, Meta
from ..base.usecase import Usecase
from ..constants import style_ranges, complexity_ranges


def get_value_id() -> str:
    return "".join(random.choices(ascii_letters + digits, k=4))


def get_cell_id() -> str:
    return "".join(random.choices(ascii_letters + digits, k=6))


def get_field_id() -> str:
    return "".join(random.choices(ascii_letters + digits, k=8))


def check_intersection(
    cells: list[str],
    solved: list[str],
    unsolved: list[str],
    finder,
) -> bool:
    local_solved, local_unsolved = [], []

    for cell in cells:
        for unsolve in unsolved:
            if finder.find_for_item("toggle_play", cell["id"]).is_checked(unsolve):
                local_unsolved.append(unsolve)
        for solve in solved:
            if finder.find_for_item("toggle_play", cell["id"]).is_checked(solve):
                local_solved.append(solve)

    if not list(set(local_unsolved) & set(unsolved)):
        if sorted(local_solved) == sorted(solved):
            return True

    return False


@define(slots=True)
class SolveDTO:
    user_id: int
    puzzle_id: int
    size: int


@define(slots=True)
class RankDTO:
    user_id: int
    score: int


@define(slots=True)
class ResultDTO:
    solve: SolveDTO
    rank: RankDTO


@define(slots=True, kw_only=True)
class PuzzleDTO:
    puzzle_id: int = field(default=None)
    size: int
    score: int
    complexity: str
    sample: list[int]
    original: list[int]
    zeroed: list[int]
    modified: list[int]
    vertical: list[int]
    horizontal: list[int]


def calculate_score(modified_array: numpy.array) -> int:
    return numpy.sum(
        [
            modified_array[i] - min(modified_array)
            for i in numpy.arange(len(modified_array))
        ],
        dtype=numpy.int_,
    )


def fill_value(
    arr: list,
    index: int,
    style: str,
    value: str,
) -> tuple[Cell, bool]:
    return (
        Cell(
            id=get_cell_id(),
            values=[
                Value(get_value_id(), value),
                Value(get_value_id(), style_ranges[style]["deleted"] + value),
                Value(get_value_id(), style_ranges[style]["keep"] + value),
            ],
        ),
        True if arr[index] == 0 else False,
    )


def fill_sum_value(
    arr: iter,
) -> Cell:
    return Cell(
        id=get_cell_id(),
        values=[
            Value(get_value_id(), next(arr)),
        ],
    )


def pack_to_meta(
    locale: str,
    puzzle_id: int,
    size: int,
    score: int,
    complexity: str,
) -> Meta:
    return Meta(
        locale=locale,
        puzzle_id=puzzle_id,
        size=size,
        score=score,
        complexity=complexity,
    )


def pack_to_fields(
    style: str,
    size: int,
    zeroed: list[int],
    modified: list[int],
    horizontal: list[int],
    vertical: iter,
) -> Field:
    cells: list = []
    solved, unsolved = [], []

    for index in range(len(modified)):
        cell, res = fill_value(zeroed, index, style, str(modified[index]))
        if (index != 0) and (index % size == 0):
            cells.append(fill_sum_value(vertical))
            if index != len(modified):
                if res is True:
                    cells.append(cell)
                    solved.append(cell.values[1].id)
                else:
                    cells.append(cell)
                    unsolved.append(cell.values[1].id)
        elif index % size != 0:
            if res is True:
                cells.append(cell)
                solved.append(cell.values[1].id)
            else:
                cells.append(cell)
                unsolved.append(cell.values[1].id)
        else:
            if res is True:
                cells.append(cell)
                solved.append(cell.values[1].id)
            else:
                cells.append(cell)
                unsolved.append(cell.values[1].id)
    cells.append(fill_sum_value(vertical))

    for item in horizontal:
        cells.append(Cell(get_cell_id(), [Value(id=get_value_id(), value=str(item))]))
    cells.append(Cell(get_cell_id(), [Value(get_value_id(), "ㅤ")]))

    return Field(id=get_field_id(), cells=cells, solved=solved, unsolved=unsolved)


def create_puzzle(data: Setup) -> PuzzleDTO:
    setup = complexity_ranges[data.complexity]

    original = randint(low=setup["low"], high=setup["high"], size=data.size**2)
    sample = choice(len(original), size=randint(1, data.size**2 - 1), replace=False)
    indices = numpy.arange(0, data.size * data.size + 1, data.size)

    zeroed, modified = (numpy.copy(original), numpy.copy(original))
    for index in sample:
        modified[index] = randint(low=setup["low"], high=setup["high"])
        zeroed[index] = 0

    vertical = numpy.add.reduceat(zeroed, indices[:-1])
    horizontal = numpy.add.reduceat(
        numpy.reshape(zeroed, newshape=(data.size, data.size)).transpose().ravel(),
        indices[:-1],
    )

    return PuzzleDTO(
        score=calculate_score(modified),
        size=data.size,
        complexity=data.complexity,
        sample=sample.tolist(),
        original=original.tolist(),
        zeroed=zeroed.tolist(),
        modified=modified.tolist(),
        vertical=vertical.tolist(),
        horizontal=horizontal.tolist(),
    )


class SaveField(Usecase[PuzzleDTO, Puzzle]):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def __call__(self, data: PuzzleDTO) -> Puzzle:
        converter = get_converter(PuzzleDTO, Puzzle)
        puzzle = converter(data)

        await self.uow.puzzle.create(puzzle)
        await self.uow.commit()

        return puzzle


class CreatePuzzle(Usecase[Setup, Game]):
    def __init__(self, save: SaveField):
        self.save = save

    async def __call__(self, setup: Setup) -> dict:
        create = create_puzzle(setup)
        puzzle = await self.save(create)

        meta = pack_to_meta(
            locale=setup.locale,
            puzzle_id=puzzle.puzzle_id,
            size=puzzle.size,
            score=int(puzzle.score),
            complexity=puzzle.complexity,
        )
        field = pack_to_fields(
            style=setup.style,
            size=create.size,
            zeroed=create.zeroed,
            modified=create.modified,
            horizontal=create.horizontal,
            vertical=iter(create.vertical),
        )
        data = Game(meta=meta, field=field)

        return asdict(data)


class SearchPuzzle(Usecase[..., Game]):
    def __init__(self): ...

    async def __call__(
        self,
        puzzle: Puzzle,
        setup: Setup,
    ) -> dict:
        meta = pack_to_meta(
            locale=setup.locale,
            puzzle_id=puzzle.puzzle_id,
            size=puzzle.size,
            score=int(puzzle.score),
            complexity=puzzle.complexity,
        )
        field = pack_to_fields(
            style=setup.style,
            size=puzzle.size,
            zeroed=puzzle.zeroed,
            modified=puzzle.modified,
            horizontal=puzzle.horizontal,
            vertical=iter(puzzle.vertical),
        )
        data = Game(meta=meta, field=field)

        return asdict(data)


class ResultPuzzle(Usecase[ResultDTO, ...]):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def __call__(self, data: ResultDTO):
        converter = get_converter(SolveDTO, Solve)
        solve = converter(data.solve)

        converter = get_converter(RankDTO, Rank)
        rank = converter(data.rank)

        await self.uow.solve.add(solve)
        await self.uow.rank.add(rank)
        await self.uow.commit()
