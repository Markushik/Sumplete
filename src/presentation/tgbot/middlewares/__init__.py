from aiogram import Dispatcher

from src.presentation.tgbot.middlewares.i18n import I18nMiddleware
from src.presentation.tgbot.middlewares.user import UserMiddleware


def setup_middlewares(disp: Dispatcher, loader):
    disp.message.middleware(UserMiddleware())

    disp.message.middleware(loader)
    disp.callback_query.middleware(loader)

