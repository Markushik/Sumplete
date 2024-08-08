from enum import StrEnum
from typing import Final

TELEGRAPH_LINK: Final[str] = "https://telegra.ph/Sumplete---Rules-07-17"
TELEGRAM_LINK: Final[str] = "tg://user?id=878406427"
DEFAULT_LOCALE: Final[str] = "en_GB"


class LocalesEnum(StrEnum):
    ENGLISH = "en_GB"
    RUSSIAN = "ru_RU"
