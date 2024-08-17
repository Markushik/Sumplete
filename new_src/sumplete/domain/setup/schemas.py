from attrs import define


@define(slots=True)
class Size:
    id: str
    size: str


@define(slots=True)
class Complexity:
    id: str
    complexity: str
