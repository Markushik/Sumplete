from aiogram_dialog import DialogManager

from src.domain.entities.menu import (
    Style,
    Language,
    Announcement,
    STYLES,
    LANGUAGES,
    ANNOUNCEMENTS,
)


async def getter(dialog_manager: DialogManager, **kwargs):
    l10n = dialog_manager.middleware_data.get("l10n")

    return {
        LANGUAGES: [
            Language("en_GB", "🇬🇧 English"),
            Language("ru_RU", "🇷🇺 Русский"),
        ],
        STYLES: [
            Style("format", l10n.format_value("format-btn")),
            Style("emoji", l10n.format_value("emoji-btn")),
        ],
        ANNOUNCEMENTS: [
            Announcement("on", l10n.format_value("on-btn")),
            Announcement("off", l10n.format_value("off-btn")),
        ],
    }
