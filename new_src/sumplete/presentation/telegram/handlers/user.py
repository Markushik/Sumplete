from aiogram import Router
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import inject, FromDishka

from new_src.sumplete.domain.user.usecase import UserHandler, UserDTO
from ..states import MainMenu


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


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())

    return router
