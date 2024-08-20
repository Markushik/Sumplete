from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, Button, Row, SwitchTo

from ..extras.i18n.format import I18nFormat

from .handlers import on_generate, on_main, on_random, on_search
from .states import ModeMenu


def mode_menu() -> Dialog:
    return Dialog(
        Window(
            I18nFormat("Some message"),
            Button(I18nFormat("generate-btn"), "generate", on_click=on_generate),
            SwitchTo(
                I18nFormat("unfold-btn"),
                "unfold",
                state=ModeMenu.UNFOLD,
            ),
            Button(
                I18nFormat("back-to-main-btn"),
                "to_main",
                on_main,
            ),
            state=ModeMenu.FOLD,
        ),
        Window(
            I18nFormat("Some message"),
            Button(I18nFormat("generate-btn"), "generate", on_click=on_generate),
            Button(I18nFormat("random-btn"), "random", on_click=on_random),
            Row(
                Button(I18nFormat("daily-btn"), "daily"),
                Button(I18nFormat("search-btn"), "search", on_click=on_search),
            ),
            Back(
                I18nFormat("fold-btn"),
                "fold",
            ),
            # Button(
            #     I18nFormat("back-to-main-btn"),
            #     "to_main",
            #     on_main,
            # ),
            state=ModeMenu.UNFOLD,
        ),
    )
