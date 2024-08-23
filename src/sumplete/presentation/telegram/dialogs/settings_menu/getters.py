from aiogram_dialog import DialogManager
from attrs import define

from sumplete.infrastructure.database.uow.implement import UnitOfWork


@define(slots=True)
class Locale:
    id: str
    locale: str


@define(slots=True)
class Style:
    id: str
    style: str


@define(slots=True)
class Announcement:
    id: str
    switch: str


async def getter(dialog_manager: DialogManager, **kwargs):
    l10n = dialog_manager.middleware_data["l10n"]
    dishka = dialog_manager.middleware_data["dishka_container"]

    uow = await dishka.get(UnitOfWork)
    user = await uow.user.get(dialog_manager.event.from_user.id)

    await dialog_manager.find("radio_style").set_checked(user.style.lower())

    switches = [
        Announcement("on", l10n.format_value("on-btn")),
        Announcement("off", l10n.format_value("off-btn")),
    ]

    return {
        "locales": [
            Locale("en", "🇬🇧 English"),
            Locale("ru", "🇷🇺 Русский"),
        ],
        "styles": [
            Style("format", l10n.format_value("format-btn")),
            Style("emoji", l10n.format_value("emoji-btn")),
        ],
        "switches": switches if user.anncmt else switches[::-1],
    }
