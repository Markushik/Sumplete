import numpy
from numpy.random import choice, randint

from src.domain.constants import Complexity
from src.domain.dto.puzzle import PuzzleDTO, PuzzleSetup


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
