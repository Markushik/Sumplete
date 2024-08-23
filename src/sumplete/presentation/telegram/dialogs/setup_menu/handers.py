from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka

from sumplete.application.usecase.game import CreatePuzzle, SearchPuzzle, Setup
from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.shared.di.extras import inject_handler
from sumplete.presentation.telegram.dialogs.game_menu.states import GameMenu
from sumplete.presentation.telegram.dialogs.mode_menu.states import ModeMenu
from sumplete.presentation.telegram.dialogs.setup_menu.states import SetupMenu


async def on_menu(_, __, dialog_manager: DialogManager):
    await dialog_manager.start(state=ModeMenu.FOLD, mode=StartMode.RESET_STACK)


async def on_size(_, __, dialog_manager: DialogManager, size: str):
    dialog_manager.dialog_data["size"] = size
    await dialog_manager.switch_to(SetupMenu.GENERATE)


async def on_complexity(_, __, dialog_manager: DialogManager, complexity: str):
    dialog_manager.dialog_data["complexity"] = complexity
    await dialog_manager.switch_to(SetupMenu.GENERATE)


@inject_handler
async def on_generate(
    query: CallbackQuery,
    _,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    create: FromDishka[CreatePuzzle],
) -> None | bool:
    size = dialog_manager.dialog_data.get("size", "3")
    complexity = dialog_manager.dialog_data.get("complexity", "easy")

    user = await uow.user.get(dialog_manager.event.from_user.id)
    pzle = await create(
        Setup(
            locale=user.locale,
            style=user.style,
            size=int(size[0]),
            complexity=complexity.lower(),
        )
    )

    return await dialog_manager.start(
        state=GameMenu.START,
        data={"meta": pzle["meta"], "field": pzle["field"]},
        mode=StartMode.RESET_STACK,
    )


async def on_backspace(_, __, dialog_manager: DialogManager) -> None:
    dialog_manager.dialog_data["puzzle_id"] = dialog_manager.dialog_data.get(
        "puzzle_id", ""
    )[:-1]


async def on_select(
    query: CallbackQuery, _, dialog_manager: DialogManager, digit: str
) -> bool:
    l10n = dialog_manager.middleware_data["l10n"]
    puzzle_id = dialog_manager.dialog_data.get("puzzle_id", "")

    if len(puzzle_id) >= 10:
        return await query.answer(l10n.format_value("input-error-msg"))

    dialog_manager.dialog_data["puzzle_id"] = (
        dialog_manager.dialog_data.get("puzzle_id", "") + digit
    )


@inject_handler
async def on_confirm(
    query: CallbackQuery,
    _,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    search: FromDishka[SearchPuzzle],
) -> None:
    l10n = dialog_manager.middleware_data["l10n"]
    puzzle_id = dialog_manager.dialog_data["puzzle_id"]

    puzzle = await uow.puzzle.search(puzzle_id)
    if not puzzle:
        return await query.answer(l10n.format_value("search-error-msg"))

    solve = await uow.solve.check(
        user_id=dialog_manager.event.from_user.id, puzzle_id=int(puzzle_id)
    )
    if solve:
        return await dialog_manager.switch_to(SetupMenu.SOLVED)

    user = await uow.user.get(dialog_manager.event.from_user.id)
    pzle = await search(
        puzzle,
        Setup(
            locale=user.locale,
            style=user.style,
            size=puzzle.size,
            complexity=puzzle.complexity,
        ),
    )

    return await dialog_manager.start(
        state=GameMenu.START,
        data={"meta": pzle["meta"], "field": pzle["field"]},
        mode=StartMode.RESET_STACK,
    )


async def on_input(
    message: Message,
    _,
    dialog_manager: DialogManager,
) -> None:
    print(message.text)


async def on_no(
    message: Message,
    _,
    dialog_manager: DialogManager,
):
    await dialog_manager.switch_to(SetupMenu.SEARCH)

@inject_handler
async def on_yes(
    _,
    __,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    search: FromDishka[SearchPuzzle],
):
    puzzle_id = dialog_manager.dialog_data["puzzle_id"]
    puzzle = await uow.puzzle.search(puzzle_id)
    user = await uow.user.get(dialog_manager.event.from_user.id)
    pzle = await search(
        puzzle,
        Setup(
            locale=user.locale,
            style=user.style,
            size=puzzle.size,
            complexity=puzzle.complexity,
        ),
    )

    return await dialog_manager.start(
        state=GameMenu.START,
        data={"meta": pzle["meta"], "field": pzle["field"]},
        mode=StartMode.RESET_STACK,
    )
