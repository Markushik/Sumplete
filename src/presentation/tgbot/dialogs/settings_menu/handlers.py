from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from src.domain.dto.user import UserDTO
from src.domain.usecases.user import UpdateLanguage

from src.infrastructure.database.uow.impl import UnitOfWork
from src.main.di.extras import inject_handler
from src.presentation.tgbot.dialogs.dialog_extras.i18n.updater import update_format_key
from src.presentation.tgbot.states.user import MainMenu


async def on_click_back_to_main(
    query: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(state=MainMenu.START, mode=StartMode.RESET_STACK)


@inject_handler
async def on_click_update_language(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    item_id: str,
    update_language: FromDishka[UpdateLanguage],
) -> None:
    language = item_id[:-3]

    await update_language(
        UserDTO(tg_id=dialog_manager.event.from_user.id, language=language)
    )
    await update_format_key(dialog_manager, language)


@inject_handler
async def on_click_update_notify(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    item_id: bool,
    uow: FromDishka[UnitOfWork],
) -> None:
    l10n = dialog_manager.middleware_data.get("l10n")
    flag = False if item_id != "on_id" else True

    await uow.user_repo.update_notify(dialog_manager.event.from_user.id, flag)
    await uow.commit()

    await query.answer(
        l10n.format_value("on-msg") if flag else l10n.format_value("off-msg")
    )


@inject_handler
async def on_click_update_style(
    query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    item_id: str,
    uow: FromDishka[UnitOfWork],
) -> None:
    l10n = dialog_manager.middleware_data.get("l10n")

    style = item_id[:-3]
    text = ...

    if style == "format":
        text = l10n.format_value("format-msg")
    elif style == "emoji":
        text = l10n.format_value("emoji-msg")

    await uow.user_repo.update_style(dialog_manager.event.from_user.id, style)
    await uow.commit()

    await query.answer(text)
