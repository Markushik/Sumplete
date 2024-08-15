from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka

from new_src.sumplete.adapters.database.uow.implement import UnitOfWork
from new_src.sumplete.common.di.extras import inject_handler
from ...states import MainMenu, SetupMenu


async def on_main(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


@inject_handler
async def on_mode(
    _,
    __,
    dialog_manager: DialogManager,
    action: str,
    uow: FromDishka[UnitOfWork],
) -> None:
    print(action)

    match action:
        case "generate":
            return await dialog_manager.start(state=SetupMenu.GENERATE)
        case "random":
            ...
        case "daily":
            ...
        case "search":
            ...

    # if item_id == "generate":  # generate puzzle
    #     await dialog_manager.start(state=SetupMenu.GENERATE, mode=StartMode.NORMAL)
    # if item_id == "random":
    #     request = await uow.puzzle.random()
    #     converter = get_converter(Puzzle, PuzzleDTO)
    #     random = converter(request)
    #
    #     await dialog_manager.start(
    #         state=GameMenu.PLAY,
    #         data={"action": asdict(random), "puzzle_id": random.puzzle_id},
    #         mode=StartMode.RESET_STACK,
    #     )
    # if item_id == "daily":  # daily?
    #     await dialog_manager.start(state=SetupMenu.DAILY, mode=StartMode.NORMAL)
    # if item_id == "search":  # search by id
    #     await dialog_manager.start(state=SetupMenu.SEARCH, mode=StartMode.NORMAL)
