from src.presentation.tgbot.dialogs.game_menu.dialog import game_menu
from src.presentation.tgbot.dialogs.main_menu.dialog import main_menu
from src.presentation.tgbot.dialogs.mode_menu.dialog import mode_menu
from src.presentation.tgbot.dialogs.settings_menu.dialog import settings_menu
from src.presentation.tgbot.dialogs.setup_menu.dialog import setup_menu


def get_dialogs() -> list:
    return [main_menu(), settings_menu(), mode_menu(), setup_menu(), game_menu()]
