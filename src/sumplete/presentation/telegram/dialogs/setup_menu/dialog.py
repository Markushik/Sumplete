from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Row, Select, Start
from aiogram_dialog.widgets.text import Const, Format

from .getters import get_menu, get_presets
from .handers import on_backspace, on_confirm, on_generate, on_input, on_menu, on_select
from .states import SetupMenu
from ..extras.i18n.format import I18nFormat
from ..mode_menu.states import ModeMenu


def setup_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("choose-msg"),
            Row(
                Button(
                    I18nFormat("back-btn"),
                    id="back_to_mode_menu",
                    on_click=on_menu,
                ),
                Button(
                    I18nFormat("confirm-btn"),
                    id="confirm",
                    on_click=on_generate,
                ),
            ),
            state=SetupMenu.GENERATE,
            getter=get_presets,
        ),
        Window(
            I18nFormat("id-msg"),
            MessageInput(func=on_input, content_types=ContentType.TEXT),
            Group(
                Select(
                    Format("{item}"),
                    id="select_id",
                    on_click=on_select,
                    items="digits",
                    item_id_getter=str,
                ),
                width=3,
            ),
            Row(
                Button(Const("←"), id="backspace", on_click=on_backspace),
                Button(Const("✓"), id="confirm", on_click=on_confirm),
            ),
            Start(I18nFormat("back-btn"), id="back", state=ModeMenu.UNFOLD),
            getter=get_menu,
            state=SetupMenu.SEARCH,
        ),
    )