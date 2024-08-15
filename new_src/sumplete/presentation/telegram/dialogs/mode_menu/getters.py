from aiogram_dialog import DialogManager

from new_src.sumplete.domain.mode.schema import Mode


async def getter(dialog_manager: DialogManager, **kwargs):
    l10n = dialog_manager.middleware_data.get("l10n")

    return {
        "modes": [
            Mode(
                "generate",
                l10n.format_value("generate-btn"),
                l10n.format_value("generate-msg"),
            ),
            Mode(
                "random",
                l10n.format_value("random-btn"),
                l10n.format_value("random-msg"),
            ),
            Mode(
                "daily",
                l10n.format_value("daily-btn"),
                l10n.format_value("daily-msg"),
            ),
            Mode(
                "search",
                l10n.format_value("search-btn"),
                l10n.format_value("search-msg"),
            ),
        ]
    }
