from aiogram.fsm.state import State, StatesGroup


class SettingsMenu(StatesGroup):
    SETTINGS = State()
    CUSTOMZN = State()
    VIEW = State()
    LANGUAGE = State()
    ANNCMT = State()
    PROFILE = State()
