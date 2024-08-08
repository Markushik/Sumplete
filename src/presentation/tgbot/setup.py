from aiogram import Dispatcher

from src.presentation.tgbot.dialogs import get_dialogs
from src.presentation.tgbot.handlers import get_handlers


def setup_routers(disp: Dispatcher):
    disp.include_routers(*get_handlers(), *get_dialogs())
