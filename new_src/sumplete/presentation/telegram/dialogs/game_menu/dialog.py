from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, ListGroup, Row, Toggle
from aiogram_dialog.widgets.text import Const, Format
from magic_filter import F

from src.presentation.tgbot.dialogs.dialog_extras.group.custom import CustomGroup
from src.presentation.tgbot.dialogs.dialog_extras.i18n.format import I18nFormat
from .getter import getter
from ...states.game_menu import GameMenu


def game_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("puzzle-solved", when=~F["play"]),
            I18nFormat("play-msg", when=F["play"]),
            CustomGroup(
                ListGroup(
                    Toggle(
                        Format("{item[value]}"),
                        id="toggle_play",
                        item_id_getter=lambda item: item["id"],
                        items=lambda item: item["item"]["values"],
                    ),
                    id="lst_grp",
                    item_id_getter=lambda item: item["id"],
                    items="cells",
                    when=F["play"],
                ),
            ),
            Group(
                Row(
                    Button(Const("Check"), id="check"),
                    Button(Const("Hint"), id="check"),
                    Button(Const("Clear"), id="check"),
                ),
                Row(
                    Button(Const("Reveal"), id="check"),
                    Button(Const("Undo"), id="check"),
                ),
                when=F["play"],
            ),
            state=GameMenu.START,
            getter=getter,
        ),
    )