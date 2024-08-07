from itertools import cycle

from adaptix import Retort
from numpy.random import choice, randint

from src.core.puzzle.constants import Complexity
from src.domain.dto.puzzle import GameField, PuzzleSetup
from src.domain.entities.game import Cell, Value

retort = Retort()


class PuzzleGenerate:
    def __call__(self, data: PuzzleSetup) -> GameField:
        if not data.use:
            print("dont use")

        setup = Complexity[data.complexity].value

        o_array = randint(setup.LOW, setup.HIGH, data.size**2)  # original array
        z_array, r_array = o_array.copy(), o_array.copy()  # zero array & random array

        index_sample = choice(len(o_array), randint(1, data.size**2 - 1), False)
        z_array[index_sample] = 0
        for i in index_sample:
            r_array[i] = randint(setup.LOW, setup.HIGH)  # [1, 10] not [1, 10)

        z_array = z_array.reshape(data.size, data.size)
        v_sum, h_sum = z_array.sum(0), cycle(z_array.sum(1))

        cells: list = []
        count: int = 0
        id = 0

        for i in r_array:
            if count % data.size == 0 and count != 0:
                id += 1
                cells.append(
                    Cell(
                        str(id),
                        [
                            Value(str(id + 200), str(next(h_sum))),
                            Value(str(id + 400), "test1"),
                        ],
                    )
                )
            if count % data.size != 0:
                id += 1
                cells.append(
                    Cell(
                        str(id),
                        [Value(str(id + 200), str(i)), Value(str(id + 400), "test2")],
                    )
                )
            else:
                id += 1
                cells.append(
                    Cell(
                        str(id),
                        [Value(str(id + 200), str(i)), Value(str(id + 400), "test3")],
                    )
                )
            count += 1
            if count == len(r_array):
                id += 1
                cells.append(
                    Cell(
                        str(id),
                        [
                            Value(str(id + 200), str(next(h_sum))),
                            Value(str(id + 400), "test4"),
                        ],
                    )
                )
        for i in v_sum:
            id += 1
            cells.append(
                Cell(
                    str(id),
                    [Value(str(id + 200), str(i)), Value(str(id + 400), "test5")],
                )
            )

        id += 1
        cells.append(
            Cell(str(id), [Value(str(id + 200), "ㅤ"), Value(str(id + 400), "ㅤ")])
        )

        return GameField(id="game_id", cells=cells)
