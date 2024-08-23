from adaptix.conversion import get_converter
from attrs import asdict

from sumplete.application.models.game import Setup, Game
from sumplete.application.services.game import (
    pack_to_meta,
    create_puzzle,
    pack_to_field,
)
from sumplete.application.usecase.base import Interactor
from sumplete.infrastructure.database.schemas import Solve, Rank, Puzzle
from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.shared.models.game import PuzzleDTO


class SaveField(Interactor[PuzzleDTO, Puzzle]):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def __call__(self, data: PuzzleDTO) -> Puzzle:
        converter = get_converter(PuzzleDTO, Puzzle)
        puzzle = converter(data)

        await self.uow.puzzle.create(puzzle)
        await self.uow.commit()

        return puzzle


class CreatePuzzle(Interactor[Setup, Game]):
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
        field = pack_to_field(
            style=setup.style,
            size=create.size,
            zeroed=create.zeroed,
            modified=create.modified,
            horizontal=create.horizontal,
            vertical=iter(create.vertical),
        )
        data = Game(meta=meta, field=field)

        return asdict(data)


class SearchPuzzle(Interactor[..., Game]):
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
        field = pack_to_field(
            style=setup.style,
            size=puzzle.size,
            zeroed=puzzle.zeroed,
            modified=puzzle.modified,
            horizontal=puzzle.horizontal,
            vertical=iter(puzzle.vertical),
        )
        data = Game(meta=meta, field=field)

        return asdict(data)


class ResultPuzzle(Interactor[..., None]):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def __call__(
        self, user_id: int, puzzle_id: int, size: int, score: int
    ) -> None:
        rank = await self.uow.rank.get(user_id)

        if rank is None:
            await self.uow.rank.create(Rank(user_id=user_id, score=0))

        await self.uow.rank.update(user_id=user_id, score=score)
        await self.uow.solve.create(
            Solve(user_id=user_id, puzzle_id=puzzle_id, size=size)
        )
        await self.uow.commit()
