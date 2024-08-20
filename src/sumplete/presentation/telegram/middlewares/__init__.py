from aiogram import Dispatcher


def setup_middlewares(disp: Dispatcher, loader):
    disp.message.middleware(loader)
    disp.callback_query.middleware(loader)
