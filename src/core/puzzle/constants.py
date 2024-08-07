from enum import Enum, IntEnum


class Easy(IntEnum):
    LOW = 1
    HIGH = 10


class Advanced(IntEnum):
    LOW = 10
    HIGH = 50


class Expert(IntEnum):
    LOW = 10
    HIGH = 50


class Complexity(Enum):
    EASY = Easy
    ADVANCED = Advanced
    EXPERT = Expert
