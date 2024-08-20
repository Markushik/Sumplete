from aiogram.fsm.state import State, StatesGroup


class ModeMenu(StatesGroup):
    FOLD = State()
    UNFOLD = State()

    GENERATE = State()  # maybe delete
    RANDOM = State()
    DAILY = State()
    SEARCH = State()
