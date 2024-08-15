from aiogram_dialog import DialogManager


async def update_format(dialog_manager: DialogManager, locale: str) -> None:
    l10n = dialog_manager.middleware_data["l10ns"][locale]
    dialog_manager.middleware_data["aiogd_i18n_format"] = l10n.format_value
