from aiogram_dialog import DialogManager

from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from new_src.sumplete.domain.settings.schemas import Locale, Style, Announcement


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
