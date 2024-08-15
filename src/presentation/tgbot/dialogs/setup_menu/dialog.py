from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Radio, Row, Select, Start
from aiogram_dialog.widgets.text import Const, Format

from src.domain.entities.menu import COMPLEXITIES, SIZES
from src.presentation.tgbot.dialogs.dialog_extras.i18n.format import I18nFormat
from src.presentation.tgbot.states.user import ModeMenu, SetupMenu

from .getters import get_pincode_data, get_setups
from .handers import (
    on_backspace,
    on_click_mode_menu,
    on_confirm,
    on_generate,
    on_input,
    on_random,
    on_select,
)


def setup_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("choose-msg"),
            Row(
                Radio(
                    Format("✓ {item.size}"),
                    Format("{item.size}"),
                    id="sizes",
                    item_id_getter=lambda item: item.id,
                    items=SIZES,
                ),
            ),
            Row(
                Radio(
                    Format("✓ {item.complexity}"),
                    Format("{item.complexity}"),
                    id="complexities",
                    item_id_getter=lambda item: item.id,
                    items=COMPLEXITIES,
                ),
            ),
            Button(
                I18nFormat("confirm-btn"),
                id="apply",
                on_click=on_generate,
            ),
            Button(
                I18nFormat("back-btn"),
                id="back_to_mode_menu",
                on_click=on_click_mode_menu,
            ),
            state=SetupMenu.GENERATE,
            getter=get_setups,
        ),
        Window(
            I18nFormat("id-msg"),  # TODO: if human clicked 4096 once :D
            MessageInput(func=on_input, content_types=ContentType.TEXT),
            Group(
                Select(
                    Format("{item}"),
                    id="select_id",
                    on_click=on_select,
                    items=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    item_id_getter=str,
                ),
                width=3,
            ),
            Row(
                Button(Const("←"), id="backspace", on_click=on_backspace),
                Button(Const("✓"), id="apply", on_click=on_random),
            ),
            Start(I18nFormat("back-btn"), id="back", state=ModeMenu.GENERATE),
            getter=get_pincode_data,
            state=SetupMenu.SEARCH,
        ),
    )
