from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from src.presentation.tgbot.states.user import GameMenu, ModeMenu


async def on_click_to_mode_menu(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ModeMenu.GENERATE, mode=StartMode.RESET_STACK)


async def on_click_play_generate(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> bool:
    l10n = dialog_manager.middleware_data.get("l10n")

    size = dialog_manager.find("sizes").get_checked()
    complexity = dialog_manager.find("complexities").get_checked()

    if (size is None) or (complexity is None):
        return await query.answer(l10n.format_value("parameters-error-msg"))

    await dialog_manager.start(
        state=GameMenu.GENERATE,
        data={"size": size[0], "complexity": complexity.upper()},
        mode=StartMode.RESET_STACK,
    )


async def on_confirm(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    print(dialog_manager.dialog_data.get("puzzle_id"))


async def on_backspace(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    dialog_data = dialog_manager.dialog_data
    dialog_data["puzzle_id"] = dialog_data.get("puzzle_id", "")[:-1]


async def on_select(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str
) -> bool:
    l10n = dialog_manager.middleware_data.get("l10n")
    puzzle_id = dialog_manager.dialog_data.get("puzzle_id", "")

    if len(puzzle_id) >= 10:
        return await query.answer(l10n.format_value("input-error-msg"))

    dialog_data = dialog_manager.dialog_data
    dialog_data["puzzle_id"] = dialog_data.get("puzzle_id", "") + data


async def on_input(
    message: Message,
    input_message: MessageInput,
    dialog_manager: DialogManager,
) -> None:
    print(message.text)
