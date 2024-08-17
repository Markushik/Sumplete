from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka

from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from new_src.sumplete.common.di.extras import inject_handler
from new_src.sumplete.domain.game.schema import Setup
from new_src.sumplete.domain.game.usecase import CreatePuzzle, SearchPuzzle
from ...states import GameMenu, ModeMenu


async def on_menu(_, __, dialog_manager: DialogManager):
    await dialog_manager.start(state=ModeMenu.FOLD, mode=StartMode.RESET_STACK)


@inject_handler
async def on_generate(
    query: CallbackQuery,
    _,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    create: FromDishka[CreatePuzzle],
) -> None | bool:
    l10n = dialog_manager.middleware_data["l10n"]

    size = dialog_manager.find("select_size").get_checked()
    complexity = dialog_manager.find("select_complexity").get_checked()

    if (size is None) or (complexity is None):
        return await query.answer(l10n.format_value("parameters-error-msg"))

    user = await uow.user.get(dialog_manager.event.from_user.id)
    pzle = await create(
        Setup(
            locale=user.locale,
            style=user.style,
            size=int(size[0]),
            complexity=complexity,
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
