from aiogram_dialog import DialogManager


async def update_format_key(dialog_manager: DialogManager, language: str) -> None:
    l10n = dialog_manager.middleware_data["l10ns"][language]
    dialog_manager.middleware_data["aiogd_i18n_format"] = l10n.format_value
