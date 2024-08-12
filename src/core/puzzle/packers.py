import random
from string import ascii_letters, digits

from src.domain.constants import Marker
from src.domain.dto.puzzle import GameField
from src.domain.entities.game import Cell, Value


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
