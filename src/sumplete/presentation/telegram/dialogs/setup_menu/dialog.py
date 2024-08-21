from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Button,
    Group,
    Row,
    Select,
    Start,
    SwitchTo,
    Column,
)
from aiogram_dialog.widgets.text import Const, Format, Jinja

from .getters import get_menu, get_presets
from .handers import (
    on_backspace,
    on_confirm,
    on_generate,
    on_input,
    on_menu,
    on_select,
    on_size,
    on_complexity,
)
from .states import SetupMenu
from ..extras.i18n.format import I18nFormat
from ..mode_menu.states import ModeMenu


def setup_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("choose-msg"),
            SwitchTo(
                Jinja("› {{ dialog_data.get('size', '3×3') }} ‹"),
                id="size",
                state=SetupMenu.SELECT_SIZE,
            ),
            SwitchTo(
                Jinja("› {{ dialog_data.get('complexity', 'Easy') }} ‹"),
                id="complexity",
                state=SetupMenu.SELECT_COMPLEXITY,
            ),
            Row(
                Button(
                    I18nFormat("back-btn"),
                    id="to_mode",
                    on_click=on_menu,
                ),
                Button(
                    I18nFormat("confirm-btn"),
                    id="confirm",
                    on_click=on_generate,
                ),
            ),
            state=SetupMenu.GENERATE,
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
        Window(
            Format("..."),
            Column(
                Select(
                    Format("{item}"),
                    id="select_size",
                    item_id_getter=str,
                    items="sizes",
                    on_click=on_size,
                ),
            ),
            SwitchTo(I18nFormat("back-btn"), id="back", state=SetupMenu.GENERATE),
            getter=get_presets,
            state=SetupMenu.SELECT_SIZE,
        ),
        Window(
            Format("..."),
            Column(
                Select(
                    Format("{item}"),
                    id="select_complexity",
                    item_id_getter=str,
                    items="complexities",
                    on_click=on_complexity,
                ),
            ),
            SwitchTo(I18nFormat("back-btn"), id="back", state=SetupMenu.GENERATE),
            getter=get_presets,
            state=SetupMenu.SELECT_COMPLEXITY,
        ),
    )
