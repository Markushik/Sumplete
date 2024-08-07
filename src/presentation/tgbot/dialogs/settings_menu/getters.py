from aiogram_dialog import DialogManager

from src.domain.entities.menu import Customization, Localization, Notification, LANGUAGES, STYLES, TOGGLES


async def getter(dialog_manager: DialogManager, **kwargs):  # noqa
    l10n = dialog_manager.middleware_data.get('l10n')

    return {
        LANGUAGES: [
            Localization('en_GB_id', '🇬🇧 English', 'en_GB'),
            Localization('ru_RU_id', '🇷🇺 Русский', 'ru_RU'),
        ],
        STYLES: [
            Customization('format_id', l10n.format_value('format-btn')),
            Customization('emoji_id', l10n.format_value('emoji-btn')),
        ],
        TOGGLES: [
            Notification('on_id', l10n.format_value('on-btn')),
            Notification('off_id', l10n.format_value('off-btn')),
        ]
    }
