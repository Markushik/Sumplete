from aiogram.fsm.state import StatesGroup, State


class SettingsMenu(StatesGroup):
    SETTINGS = State()
    CUSTOMZN = State()
    VIEW = State()
    LANGUAGE = State()
    ANNCMT = State()
    PROFILE = State()

