from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Button,
    Radio,
    Row,
    Select,
    SwitchTo,
    Toggle,
    Column,
)
from aiogram_dialog.widgets.text import Format

from .getters import getter
from .handlers import (
    on_main,
    on_language,
    on_anncmt,
    on_customzn,
    on_profile,
)
from ..extras.i18n.format import I18nFormat
from ...states import SettingsMenu

BACK_BTN: SwitchTo = SwitchTo(
    I18nFormat("back-btn"), id="to_back", state=SettingsMenu.SETTINGS
)


def settings_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("settings-msg"),
            SwitchTo(I18nFormat("anncmt-btn"), "anncmt", SettingsMenu.ANNCMT),
            Row(
                SwitchTo(
                    I18nFormat("profile-btn"),
                    "profile",
                    SettingsMenu.PROFILE,
                ),
                SwitchTo(
                    I18nFormat("language-btn"),
                    "language",
                    SettingsMenu.LANGUAGE,
                ),
            ),
            SwitchTo(I18nFormat("customzn-btn"), "customzn", SettingsMenu.CUSTOMZN),
            Button(
                I18nFormat("back-to-main-btn"),
                id="to_main",
                on_click=on_main,
            ),
            state=SettingsMenu.SETTINGS,
        ),
        Window(
            I18nFormat("language-msg"),
            Column(
                Select(
                    Format("{item.locale}"),
                    id="select_language",
                    item_id_getter=lambda item: item.id,
                    items="locales",
                    on_click=on_language,
                ),
                BACK_BTN,
            ),
            getter=getter,
            state=SettingsMenu.LANGUAGE,
        ),
        Window(
            I18nFormat("customzn-msg"),
            Row(
                Radio(
                    Format("✓ {item.style}"),
                    Format("{item.style}"),
                    id="radio_style",
                    item_id_getter=lambda item: item.id,
                    items="styles",
                    on_click=on_customzn,
                )
            ),
            Column(
                SwitchTo(I18nFormat("view-btn"), "view", SettingsMenu.VIEW),
                BACK_BTN,
            ),
            getter=getter,
            state=SettingsMenu.CUSTOMZN,
        ),
        Window(
            I18nFormat("anncmt-msg"),
            Toggle(
                text=Format("{item.switch}"),
                id="toggle_switch",
                items="switches",
                item_id_getter=lambda item: item.id,
                on_click=on_anncmt,
            ),
            BACK_BTN,
            getter=getter,
            state=SettingsMenu.ANNCMT,
        ),
        Window(
            I18nFormat("profile-msg"),
            Button(
                text=I18nFormat("delete-profile-btn"),
                id="delete_profile",
                on_click=on_profile,
            ),
            BACK_BTN,
            state=SettingsMenu.PROFILE,
        ),
    )
