from aiogram.fsm.state import State, StatesGroup


class SetupMenu(StatesGroup):
    CONTROL = State()
    SELECTOR = State()

    SELECT_3x3 = State()
    SELECT_4x4 = State()
    SELECT_5x5 = State()
    SELECT_6x6 = State()
    SELECT_7x7 = State()

    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()
