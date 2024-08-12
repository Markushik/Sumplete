from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Radio, Row, Select, SwitchTo, Toggle
from aiogram_dialog.widgets.text import Format

from src.domain.entities.menu import ANNOUNCEMENTS, LANGUAGES, STYLES
from src.presentation.tgbot.dialogs.dialog_extras.i18n.format import I18nFormat
from src.presentation.tgbot.dialogs.settings_menu.getters import getter
from src.presentation.tgbot.dialogs.settings_menu.handlers import (
    on_click_back_to_main,
    on_click_update_language,
    on_click_update_notify,
    on_click_update_style,
)
from src.presentation.tgbot.states.user import SettingsMenu


def settings_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("settings-message"),
            SwitchTo(I18nFormat("notify-btn"), id="notify", state=SettingsMenu.NOTIFY),
            Row(
                SwitchTo(
                    I18nFormat("language-btn"),
                    id="language",
                    state=SettingsMenu.LANGUAGE,
                ),
                SwitchTo(
                    I18nFormat("profile-btn"),
                    id="profile",
                    state=SettingsMenu.PROFILE,
                ),
            ),
            SwitchTo(I18nFormat("style-btn"), id="style", state=SettingsMenu.STYLE),
            Button(
                I18nFormat("back-to-main-btn"),
                id="back_to_main",
                on_click=on_click_back_to_main,
            ),
            state=SettingsMenu.SETTINGS,
        ),
        Window(
            I18nFormat("language-message"),
            Select(
                Format("{item.language}"),
                id="select_language",
                item_id_getter=lambda item: item.id,
                items=LANGUAGES,
                on_click=on_click_update_language,
            ),
            SwitchTo(I18nFormat("back-btn"), id="back", state=SettingsMenu.SETTINGS),
            state=SettingsMenu.LANGUAGE,
        ),
        Window(
            I18nFormat("style-message"),
            Row(
                Radio(
                    Format("✓ {item.style}"),
                    Format("{item.style}"),
                    id="radio_style",
                    item_id_getter=lambda item: item.id,
                    items=STYLES,
                    on_click=on_click_update_style,
                )
            ),
            Button(I18nFormat("check-btn"), id="check"),  # SwitchTo
            SwitchTo(I18nFormat("back-btn"), id="back", state=SettingsMenu.SETTINGS),
            state=SettingsMenu.STYLE,
        ),
        Window(
            I18nFormat("notify-msg"),
            Toggle(
                text=Format("{item.switch}"),
                id="radio_toggle",
                items=ANNOUNCEMENTS,
                item_id_getter=lambda item: item.id,
                on_click=on_click_update_notify,
            ),
            SwitchTo(I18nFormat("back-btn"), id="back", state=SettingsMenu.SETTINGS),
            state=SettingsMenu.NOTIFY,
        ),
        Window(
            I18nFormat("profile-msg"),
            Button(I18nFormat("delete-profile-btn"), id="delete_profile"),
            SwitchTo(I18nFormat("back-btn"), id="back", state=SettingsMenu.SETTINGS),
            state=SettingsMenu.PROFILE,
        ),
        getter=getter,
    )
