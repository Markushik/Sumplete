from aiogram.fsm.state import State, StatesGroup


class ModeMenu(StatesGroup):
    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()
