from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka, inject

from sumplete.shared.models.user import UserDTO
from sumplete.application.usecase.user import UserHandler
from ..dialogs.main_menu.states import MainMenu
from ..dialogs.mode_menu.states import ModeMenu


@inject
async def command_start(
    _, dialog_manager: DialogManager, user_handler: FromDishka[UserHandler]
) -> None:
    await user_handler(
        UserDTO(
            user_id=dialog_manager.event.from_user.id,
            user_name=dialog_manager.event.from_user.first_name,
        )
    )
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


async def command_play(_, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=ModeMenu.FOLD, mode=StartMode.RESET_STACK)


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())
    router.message.register(command_play, Command("play"))

    return router
