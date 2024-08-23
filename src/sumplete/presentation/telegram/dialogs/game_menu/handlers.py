from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka

from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.shared.di.extras import inject_handler
from sumplete.presentation.telegram.dialogs.game_menu.states import GameMenu
from sumplete.application.usecase.game import SearchPuzzle, Setup


@inject_handler
async def on_clear(
    _,
    __,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    search: FromDishka[SearchPuzzle],
) -> None:
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
