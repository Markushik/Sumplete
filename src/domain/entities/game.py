from typing import List

from attr import define


@define(slots=True)
class Value:
    id: str
    value: str


@define(slots=True)
class Cell:
    id: str
    values: List[Value]
