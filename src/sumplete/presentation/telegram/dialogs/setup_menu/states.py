from aiogram.fsm.state import State, StatesGroup


class SetupMenu(StatesGroup):
    CONTROL = State()
    SELECT_SIZE = State()
    SELECT_COMPLEXITY = State()


    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()
