from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import (
    Button,
    CurrentPage,
    NextPage,
    PrevPage,
    Row,
    ScrollingGroup,
    Select,
)
from aiogram_dialog.widgets.text import Format, List

from .getters import getter
from .handlers import on_main, on_mode
from ..extras.i18n.format import I18nFormat
from ...states import ModeMenu


def mode_menu() -> Dialog:
    return Dialog(
        Window(
            List(
                Format("{item.message}"),
                items="modes",
                id="list_scroll",
                page_size=1,
            ),
            ScrollingGroup(
                Select(
                    Format("{item.mode}"),
                    id="select_mode",
                    items="modes",
                    item_id_getter=lambda item: item.id,
                    on_click=on_mode,
                ),
                width=1,
                height=1,
                hide_pager=True,
                id="scroll_no_pager",
                on_page_changed=sync_scroll("list_scroll"),
            ),
            Row(
                PrevPage(scroll="scroll_no_pager", text=Format("←")),
                CurrentPage(
                    scroll="scroll_no_pager",
                    text=Format("{current_page1} / 4"),
                ),
                NextPage(scroll="scroll_no_pager", text=Format("→")),
            ),
            Button(
                I18nFormat("back-to-main-btn"),
                "to_main",
                on_main,
            ),
            getter=getter,
            state=ModeMenu.GENERATE,
        ),
    )
