from attrs import define, field


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
