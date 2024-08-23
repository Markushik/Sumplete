from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Start, Url
from aiogram_dialog.widgets.text import Const

from .states import MainMenu
from ..constants import TELEGRAPH_LINK
from ..extras.i18n.format import I18nFormat
from ..ranking_menu.states import RankingMenu
from ..settings_menu.states import SettingsMenu


def main_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("start-msg"),
            Row(
                Url(I18nFormat("rules-btn"), id="rules", url=Const(TELEGRAPH_LINK)),
                Start(I18nFormat("ranking-btn"), id="ranking", state=RankingMenu.RANKS),
            ),
            Start(
                I18nFormat("settings-btn"),
                id="settings",
                state=SettingsMenu.SETTINGS,
            ),
            state=MainMenu.START,
        )
    )
