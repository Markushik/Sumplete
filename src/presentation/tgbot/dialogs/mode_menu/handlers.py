from adaptix.conversion import get_converter
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from attrs import asdict
from dishka.integrations.aiogram import FromDishka

from src.domain.dto.puzzle import PuzzleDTO
from src.infrastructure.database.models import Puzzle
from src.infrastructure.database.uow.impl import UnitOfWork
from src.main.di.extras import inject_handler
from src.presentation.tgbot.states.user import GameMenu, MainMenu, SetupMenu


async def on_click_back_to_main(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


@inject_handler
async def on_click_select_mode(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    item_id: str,
    uow: FromDishka[UnitOfWork],
) -> None:
    if item_id == "generate":  # generate puzzle
        await dialog_manager.start(state=SetupMenu.GENERATE, mode=StartMode.NORMAL)
    if item_id == "random":
        request = await uow.puzzle.random()
        converter = get_converter(Puzzle, PuzzleDTO)
        random = converter(request)

        await dialog_manager.start(
            state=GameMenu.PLAY,
            data={"action": asdict(random), "puzzle_id": random.puzzle_id},
            mode=StartMode.RESET_STACK,
        )
    if item_id == "daily":  # daily?
        await dialog_manager.start(state=SetupMenu.DAILY, mode=StartMode.NORMAL)
    if item_id == "search":  # search by id
        await dialog_manager.start(state=SetupMenu.SEARCH, mode=StartMode.NORMAL)
