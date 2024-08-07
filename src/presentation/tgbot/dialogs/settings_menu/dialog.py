from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, Radio, Row, SwitchTo, Toggle
from aiogram_dialog.widgets.text import Format

from src.domain.entities.menu import LANGUAGES, STYLES, TOGGLES
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
            I18nFormat('settings-message'),
            SwitchTo(I18nFormat('notify-btn'), id='notify_id', state=SettingsMenu.NOTIFY),
            Row(
                SwitchTo(I18nFormat('language-btn'), id='language_id', state=SettingsMenu.LANGUAGE),
                SwitchTo(I18nFormat('profile-btn'), id='language_id', state=SettingsMenu.PERSONAL),
            ),
            SwitchTo(I18nFormat('style-btn'), id='style_id', state=SettingsMenu.STYLE),
            Button(I18nFormat('back-to-main-btn'), id='back_to_main', on_click=on_click_back_to_main),
            state=SettingsMenu.SETTINGS,
        ),
        Window(
            I18nFormat('language-message'),
            Row(
                Radio(
                    Format('✓ {item.language}'),
                    Format('{item.language}'),
                    id='get_languages_id',
                    item_id_getter=lambda item: item.id,
                    items=LANGUAGES,
                    on_click=on_click_update_language,  # noqa
                )
            ),
            SwitchTo(I18nFormat('back-btn'), id='back_id', state=SettingsMenu.SETTINGS),
            state=SettingsMenu.LANGUAGE,
        ),
        Window(
            I18nFormat('style-message'),
            Row(
                Radio(
                    Format('✓ {item.style}'),
                    Format('{item.style}'),
                    id='get_styles_id',
                    item_id_getter=lambda item: item.id,
                    items=STYLES,
                    on_click=on_click_update_style,  # noqa
                )
            ),
            Button(I18nFormat('check-btn'), id='check_id'),  # SwitchTo
            SwitchTo(I18nFormat('back-btn'), id='back_id', state=SettingsMenu.SETTINGS),
            state=SettingsMenu.STYLE,
        ),
        Window(
            I18nFormat('notify-msg'),
            Toggle(
                text=Format('{item.toggle}'),
                id='get_toggles_id',
                items=TOGGLES,
                item_id_getter=lambda item: item.id,
                on_click=on_click_update_notify  # noqa
            ),
            SwitchTo(I18nFormat('back-btn'), id='back_id', state=SettingsMenu.SETTINGS),
            state=SettingsMenu.NOTIFY,
        ),
        getter=getter
    )
