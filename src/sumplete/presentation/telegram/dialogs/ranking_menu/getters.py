from aiogram_dialog import DialogManager
from dishka.integrations.aiogram import FromDishka

from src.sumplete.adapters.database.uow.implement import UnitOfWork
from sumplete.common.di.extras import inject_getter


@inject_getter
async def getter(dialog_manager: DialogManager, uow: FromDishka[UnitOfWork], **kwargs):
    l10n = dialog_manager.middleware_data["l10n"]

    ranks = await uow.rank.sampling()

    return {"ranks": ranks, "l10n": l10n}
