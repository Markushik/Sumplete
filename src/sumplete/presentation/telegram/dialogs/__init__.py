from .game_menu.dialog import game_menu
from .main_menu.dialog import main_menu
from .mode_menu.dialog import mode_menu
from .ranking_menu.dialog import ranking_menu
from .settings_menu.dialog import settings_menu
from .setup_menu.dialog import setup_menu


def get_dialogs() -> list:
    return [
        main_menu(),
        settings_menu(),
        mode_menu(),
        setup_menu(),
        game_menu(),
        ranking_menu(),
    ]
