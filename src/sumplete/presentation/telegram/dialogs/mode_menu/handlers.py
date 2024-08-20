from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka
from numpy.random import choice, randint

from src.sumplete.adapters.database.uow.implement import UnitOfWork
from src.sumplete.common.di.extras import inject_handler
from src.sumplete.domain.constants import complexity_ranges
from src.sumplete.domain.game.schema import Setup
from src.sumplete.domain.game.usecase import CreatePuzzle
from ..game_menu.states import GameMenu
from ..main_menu.states import MainMenu
from ..setup_menu.states import SetupMenu


async def on_main(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


async def on_generate(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupMenu.GENERATE)


@inject_handler
async def on_random(
    _,
    __,
    dialog_manager: DialogManager,
    uow: FromDishka[UnitOfWork],
    create: FromDishka[CreatePuzzle],
) -> None:
    user = await uow.user.get(dialog_manager.event.from_user.id)
    pzle = await create(
        Setup(
            locale=user.locale,
            style=user.style,
            size=randint(3, 7 + 1),
            complexity=choice(list(complexity_ranges.keys())),
        )
    )

    await dialog_manager.start(
        state=GameMenu.START,
        data={"meta": pzle["meta"], "field": pzle["field"]},
        mode=StartMode.RESET_STACK,
    )


async def on_search(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=SetupMenu.SEARCH)


async def on_daily(_, __, dialog_manager: DialogManager) -> None: ...
