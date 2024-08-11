from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from src.core.puzzle.generate import PuzzleGenerate
from src.domain.dto.puzzle import PuzzleSetup, PuzzleDTO, GameField
from src.infrastructure.database.models import Puzzle
from src.infrastructure.database.uow.impl import UnitOfWork
from src.main.di.extras import inject_handler
from src.presentation.tgbot.states.user import GameMenu, MainMenu, SetupMenu
from adaptix.conversion import get_converter
from dishka.integrations.aiogram import FromDishka
from attrs import asdict

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

    # await uow.puzzle.create(puzzle)
    # await uow.commit()

    if item_id == "generate":  # generate puzzle
        await dialog_manager.start(state=SetupMenu.GENERATE, mode=StartMode.NORMAL)
    if item_id == "random":  # request from database randint len last puzzle_id
        await dialog_manager.start(state=GameMenu.GENERATE, mode=StartMode.NORMAL)
    if item_id == "daily":  # daily?
        await dialog_manager.start(state=SetupMenu.DAILY, mode=StartMode.NORMAL)
    if item_id == "search":  # search by id
        await dialog_manager.start(state=SetupMenu.SEARCH, mode=StartMode.NORMAL)
