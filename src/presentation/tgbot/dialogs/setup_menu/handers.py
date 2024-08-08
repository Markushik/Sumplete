from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, DialogProtocol, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from src.presentation.tgbot.states.user import GameMenu, ModeMenu, SetupMenu


async def on_click_to_mode_menu(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ModeMenu.GENERATE, mode=StartMode.RESET_STACK)


async def on_click_play_generate(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    size = dialog_manager.find("sizes_id").get_checked()
    complexity = dialog_manager.find("complexities_id").get_checked()

    if not (size is None) and not (complexity is None):
        return await dialog_manager.start(
            state=GameMenu.GENERATE,
            data={"size": size[0], "complexity": complexity[:-3].upper()},
            mode=StartMode.RESET_STACK,
        )

    await query.answer("🚫 Error: Not all parameters are selected")


async def on_confirm(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    actual = dialog_manager.dialog_data.get("pin")
    print(actual)


async def on_backspace(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    dialog_data = dialog_manager.dialog_data
    dialog_data["pin"] = dialog_data.get("pin", "")[:-1]


async def on_select(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager, data: str
) -> None:
    dialog_data = dialog_manager.dialog_data
    dialog_data["pin"] = dialog_data.get("pin", "") + data


async def on_input(
    message: Message,
    input: MessageInput,
    dialog_manager: DialogManager,
) -> None:
    print(message.text)
