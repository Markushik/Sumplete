from random import choice, randint, random

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from src.presentation.tgbot.states.user import GameMenu, MainMenu, SetupMenu

complexity_dict = {
    "easy": {"low": 1, "high": 10},
    "medium": {"low": 10, "high": 50},
    "hard": {"low": 50, "high": 100},
}


async def on_click_back_to_main(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


async def on_click_select_mode(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    item: str,
) -> None:
    if item == "generate_id":
        await dialog_manager.start(state=SetupMenu.GENERATE, mode=StartMode.NORMAL)
    if item == "random_id":
        await dialog_manager.start(
            state=GameMenu.GENERATE,
            data={
                "size": randint(3, 6),
                "complexity": choice(tuple(complexity_dict.keys())),
            },
            mode=StartMode.RESET_STACK,
        )
    if item == "daily_id":
        await dialog_manager.start(state=SetupMenu.DAILY, mode=StartMode.NORMAL)
    if item == "search_id":
        await dialog_manager.start(state=SetupMenu.SEARCH, mode=StartMode.NORMAL)
