from aiogram_dialog import DialogManager, StartMode
from dishka import FromDishka

from sumplete.shared.models.user import UserDTO
from sumplete.application.usecase.user import UpdateLocale
from sumplete.infrastructure.database.uow.implement import UnitOfWork
from sumplete.shared.di.extras import inject_handler
from ..extras.i18n.updater import update_format
from ..main_menu.states import MainMenu


async def on_main(_, __, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


@inject_handler
async def on_language(
    _,
    __,
    dialog_manager: DialogManager,
    locale: str,
    update_locale: FromDishka[UpdateLocale],
) -> None:
    await update_locale(
        UserDTO(user_id=dialog_manager.event.from_user.id, locale=locale)
    )
    await update_format(dialog_manager=dialog_manager, locale=locale)


@inject_handler
async def on_anncmt(
    _,
    __,
    dialog_manager: DialogManager,
    switch: str,
    uow: FromDishka[UnitOfWork],
) -> None:
    await uow.user.update_anncmt(
        user_id=dialog_manager.event.from_user.id, anncmt=switch
    )
    await uow.commit()


@inject_handler
async def on_customzn(
    _,
    __,
    dialog_manager: DialogManager,
    style: str,
    uow: FromDishka[UnitOfWork],
) -> None:
    await uow.user.update_style(user_id=dialog_manager.event.from_user.id, style=style)
    await uow.commit()
