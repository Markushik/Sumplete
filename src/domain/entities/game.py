from typing import List

from attr import dataclass


@dataclass(slots=True)
class Value:
    id: str
    value: str


@dataclass(slots=True)
class Cell:
    id: str
    values: List[Value]
