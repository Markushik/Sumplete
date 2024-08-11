import random
from enum import Enum
from string import ascii_letters, digits

import numpy
from adaptix import Retort
from numpy.random import choice, randint

from src.domain.constants import Complexity
from src.domain.dto.puzzle import PuzzleSetup, PuzzleDTO, GameField
from src.domain.entities.game import Value, Cell

retort = Retort()


class Emoji(Enum):
    DELETED = "❌"
    KEEP = "✅"


class Format(Enum):
    DELETED = ""
    KEEP = ""


class Marker(Enum):
    EMOJI = Emoji
    FORMAT = Format


def get_id_cell() -> str:
    return "".join(random.choices(ascii_letters + digits, k=6))


def get_id_value() -> str:
    return "".join(random.choices(ascii_letters + digits, k=4))


def pack_to_cell(
    arr: list,
    index: int,
    style: str,
    value: str,
) -> tuple[Cell, bool]:
    marker = Marker[style].value

    return (
        Cell(
            id=get_id_cell(),
            values=[
                Value(get_id_value(), value),
                Value(get_id_value(), marker.DELETED.value + value),
                Value(get_id_value(), marker.KEEP.value + value),
            ],
        ),
        True if arr[index] == 0 else False,
    )


def pack_sum_to_cell(
    arr: iter,
) -> Cell:
    return Cell(
        id=get_id_cell(),
        values=[
            Value(get_id_value(), next(arr)),
        ],
    )


def pack_to_field(
    style: str,
    size: int,
    zeroed_array: list[int],
    modified_array: list[int],
    horizontal_sums: list[int],
    vertical_sums: iter,
) -> GameField:
    cells: list = []
    solved: list = []
    unsolved: list = []

    print("modified_array", modified_array)
    print("zeroed_array: ", zeroed_array)
    print("vertical_sums", vertical_sums)
    print("horizontal_sums", horizontal_sums)
    print()

    for index in range(len(modified_array)):
        cell, res = pack_to_cell(zeroed_array, index, style, str(modified_array[index]))

        if (index != 0) and (index % size == 0):
            cells.append(pack_sum_to_cell(vertical_sums))
            if index != len(modified_array):
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
    cells.append(pack_sum_to_cell(vertical_sums))

    for item in horizontal_sums:
        cells.append(Cell(get_id_cell(), [Value(id=get_id_value(), value=str(item))]))
    cells.append(Cell(get_id_cell(), [Value(get_id_value(), "ㅤ")]))

    return GameField(id="game", cells=cells, solved=solved, unsolved=unsolved)


def calculate_score(modified_array: numpy.array) -> int:
    return numpy.sum(
        [
            modified_array[i] - min(modified_array)
            for i in numpy.arange(len(modified_array))
        ]
    )


class PuzzleGenerate:
    def __call__(self, data: PuzzleSetup) -> PuzzleDTO:
        setup = Complexity[data.complexity].value
        original_array = randint(low=setup.LOW, high=setup.HIGH, size=data.size**2)
        zeroed_array, modified_array = original_array.copy(), original_array.copy()

        index_sample = choice(
            a=len(original_array), size=randint(1, data.size**2 - 1), replace=False
        )
        zeroed_array[index_sample] = 0
        for index in index_sample:
            modified_array[index] = randint(
                setup.LOW, setup.HIGH
            )  # [1, 10] not [1, 10)

        zeroed_array = zeroed_array.reshape(data.size, data.size)
        horizontal_sums, vertical_sums = zeroed_array.sum(0), zeroed_array.sum(1)

        score: int = calculate_score(modified_array)

        return PuzzleDTO(
            score=int(score),
            size=data.size,
            complexity=data.complexity,
            index_sample=index_sample.tolist(),
            original_array=original_array.tolist(),
            zeroed_array=zeroed_array.ravel().tolist(),
            modified_array=modified_array.tolist(),
            vertical_sums=vertical_sums.tolist(),
            horizontal_sums=horizontal_sums.tolist(),
        )


if __name__ == "__main__":
    setup = PuzzleSetup(3, "EASY")  # maybe add style (emoji, format)
    puzzle = PuzzleGenerate()
    generate = puzzle(setup)

    fields = pack_to_field(
        style="EMOJI",
        size=generate.size,
        zeroed_array=generate.zeroed_array,
        modified_array=generate.modified_array,
        horizontal_sums=generate.horizontal_sums,
        vertical_sums=iter(generate.vertical_sums),
    )

    print(fields.cells)
    print("solved: ", fields.solved)
    print("unsolved: ", fields.unsolved)
