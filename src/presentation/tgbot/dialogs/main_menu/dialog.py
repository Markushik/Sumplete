from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Start, Url
from aiogram_dialog.widgets.text import Const

from src.domain.constants import TELEGRAM_LINK, TELEGRAPH_LINK
from src.presentation.tgbot.dialogs.dialog_extras.i18n.format import I18nFormat
from src.presentation.tgbot.states.user import (
    MainMenu,
    ModeMenu,
    RankingMenu,
    SettingsMenu,
)


def main_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("start-message"),
            Start(I18nFormat("play-btn"), id="play", state=ModeMenu.GENERATE),
            Group(
                Url(I18nFormat("rules-btn"), id="rules", url=Const(TELEGRAPH_LINK)),
                Start(I18nFormat("ranking-btn"), id="ranking", state=RankingMenu.NONE),
                Start(
                    I18nFormat("settings-btn"),
                    id="settings",
                    state=SettingsMenu.SETTINGS,
                ),
                Url(I18nFormat("support-btn"), id="support", url=Const(TELEGRAM_LINK)),
                width=2,
            ),
            state=MainMenu.START,
        )
    )
