from string import ascii_letters, digits

import numpy
from numpy.random import choice, randint

from sumplete.application.models.game import Value, Cell, Meta, Field, Setup
from sumplete.shared.constants.constants import style_ranges, complexity_ranges
from sumplete.shared.models.game import PuzzleDTO


def create_value_id() -> str:
    return "".join(choice(list(ascii_letters + digits), size=4))


def create_cell_id() -> str:
    return "".join(choice(list(ascii_letters + digits), size=6))


def create_field_id() -> str:
    return "".join(choice(list(ascii_letters + digits), size=8))


def calculation_points(modified_array: numpy.array) -> int:
    return numpy.sum(
        modified_array - modified_array.min(keepdims=True), dtype=numpy.int_
    )


def fill_regular_value(
    arr: list,
    index: int,
    style: str,
    value: str,
) -> tuple[Cell, bool]:
    return (
        Cell(
            id=create_cell_id(),
            values=[
                Value(create_value_id(), value),
                Value(create_value_id(), style_ranges[style]["deleted"] + value),
                Value(create_value_id(), style_ranges[style]["keep"] + value),
            ],
        ),
        True if arr[index] == 0 else False,
    )


def fill_summed_value(
    arr: iter,
) -> Cell:
    return Cell(
        id=create_cell_id(),
        values=[
            Value(create_value_id(), next(arr)),
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


def pack_to_field(
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
        cell, res = fill_regular_value(zeroed, index, style, str(modified[index]))
        if (index != 0) and (index % size == 0):
            cells.append(fill_summed_value(vertical))
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
    cells.append(fill_summed_value(vertical))

    for item in horizontal:
        cells.append(Cell(create_cell_id(), [Value(id=create_value_id(), value=str(item))]))
    cells.append(Cell(create_cell_id(), [Value(create_value_id(), "ㅤ")]))

    return Field(id=create_field_id(), cells=cells, solved=solved, unsolved=unsolved)


# @njit
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
        score=calculation_points(modified),
        size=data.size,
        complexity=data.complexity,
        sample=sample.tolist(),
        original=original.tolist(),
        zeroed=zeroed.tolist(),
        modified=modified.tolist(),
        vertical=vertical.tolist(),
        horizontal=horizontal.tolist(),
    )
