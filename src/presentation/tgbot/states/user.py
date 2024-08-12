from aiogram.fsm.state import State, StatesGroup


class MainMenu(StatesGroup):
    START = State()


class SettingsMenu(StatesGroup):
    SETTINGS = State()
    STYLE = State()
    LANGUAGE = State()
    NOTIFY = State()
    PROFILE = State()


class ModeMenu(StatesGroup):
    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()


class SetupMenu(StatesGroup):
    CONTROL = State()

    GENERATE = State()
    RANDOM = State()
    DAILY = State()
    SEARCH = State()


class RankingMenu(StatesGroup):
    NONE = State()


class GameMenu(StatesGroup):
    PLAY = State()