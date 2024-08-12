from adaptix import Retort
from adaptix.conversion import get_converter
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from attrs import asdict
from dishka.integrations.aiogram import FromDishka

from src.core.puzzle.generate import PuzzleGenerate
from src.domain.dto.puzzle import PuzzleDTO, PuzzleSetup
from src.infrastructure.database.models import Puzzle
from src.infrastructure.database.uow.impl import UnitOfWork
from src.main.di.extras import inject_handler
from src.presentation.tgbot.states.user import GameMenu, ModeMenu

retort = Retort()


async def on_click_mode_menu(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ModeMenu.GENERATE, mode=StartMode.RESET_STACK)


@inject_handler
async def on_generate(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
) -> None | bool:
    l10n = dialog_manager.middleware_data.get("l10n")

    size = dialog_manager.find("sizes").get_checked()
    complexity = dialog_manager.find("complexities").get_checked()

    if (size is None) or (complexity is None):
        return await query.answer(l10n.format_value("parameters-error-msg"))

    setup = PuzzleSetup(int(size[0]), complexity.upper())
    puzzle = PuzzleGenerate()

    generate = puzzle(setup)
    converter = get_converter(PuzzleDTO, Puzzle)
    data = converter(generate)

    await uow.puzzle.create(data)
    await uow.commit()

    print(generate)
    return await dialog_manager.start(
        state=GameMenu.PLAY,
        data={"action": asdict(generate), "puzzle_id": 11},
        mode=StartMode.RESET_STACK,
    )


@inject_handler
async def on_random(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
) -> None:
    random = await uow.puzzle.random()
    print(random)

    await dialog_manager.start(
        state=GameMenu.PLAY,
        data={"action": asdict(random), "puzzle_id": random.puzzle_id},
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
