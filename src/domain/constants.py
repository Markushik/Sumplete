from enum import Enum, IntEnum, StrEnum
from typing import Final

TELEGRAPH_LINK: Final[str] = "https://telegra.ph/Sumplete---Rules-07-17"
TELEGRAM_LINK: Final[str] = "tg://user?id=878406427"
DEFAULT_LOCALE: Final[str] = "en_GB"


class LocalesEnum(StrEnum):
    ENGLISH = "en_GB"
    RUSSIAN = "ru_RU"


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

class Emoji(Enum):
    DELETED = "❌"
    KEEP = "✅"


class Format(Enum):
    DELETED = ""
    KEEP = ""


class Marker(Enum):
    EMOJI = Emoji
    FORMAT = Format
